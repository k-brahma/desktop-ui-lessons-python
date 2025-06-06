"""
tkinter スクロールバー付きテキストエディタ
"""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("テキストエディタ")
        self.geometry("700x500")
        
        self.filename = None
        self.create_widgets()
        self.create_menu()
    
    def create_widgets(self):
        # スクロールバー付きテキストウィジェット
        self.text_area = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            width=80,
            height=25,
            font=("Consolas", 11),
            undo=True  # アンドゥ機能を有効化
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ステータスバー
        self.status_bar = tk.Label(
            self, 
            text="準備完了", 
            anchor=tk.W, 
            relief=tk.SUNKEN,
            bg="lightgray"
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # カーソル位置の更新をバインド
        self.text_area.bind('<KeyRelease>', self.update_cursor_position)
        self.text_area.bind('<Button-1>', self.update_cursor_position)
    
    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # ファイルメニュー
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="ファイル", menu=file_menu)
        file_menu.add_command(label="新規", command=self.new_file)
        file_menu.add_command(label="開く", command=self.open_file)
        file_menu.add_command(label="保存", command=self.save_file)
        file_menu.add_command(label="名前を付けて保存", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="終了", command=self.quit)
        
        # 編集メニュー
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="編集", menu=edit_menu)
        edit_menu.add_command(label="元に戻す", command=lambda: self.text_area.edit_undo())
        edit_menu.add_command(label="やり直し", command=lambda: self.text_area.edit_redo())
        edit_menu.add_separator()
        edit_menu.add_command(label="切り取り", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="コピー", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="貼り付け", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_command(label="すべて選択", command=lambda: self.text_area.tag_add(tk.SEL, "1.0", tk.END))
    
    def new_file(self):
        if messagebox.askokcancel("新規ファイル", "現在の内容は失われます。続行しますか？"):
            self.text_area.delete("1.0", tk.END)
            self.filename = None
            self.title("テキストエディタ - 新規ファイル")
    
    def open_file(self):
        filename = filedialog.askopenfilename(
            title="ファイルを開く",
            filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert("1.0", content)
                    self.filename = filename
                    self.title(f"テキストエディタ - {filename}")
            except Exception as e:
                messagebox.showerror("エラー", f"ファイルを開けませんでした:\n{e}")
    
    def save_file(self):
        if self.filename:
            self.save_to_file(self.filename)
        else:
            self.save_as_file()
    
    def save_as_file(self):
        filename = filedialog.asksaveasfilename(
            title="名前を付けて保存",
            defaultextension=".txt",
            filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")]
        )
        if filename:
            self.save_to_file(filename)
            self.filename = filename
            self.title(f"テキストエディタ - {filename}")
    
    def save_to_file(self, filename):
        try:
            content = self.text_area.get("1.0", tk.END)
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            self.status_bar.config(text=f"保存しました: {filename}")
        except Exception as e:
            messagebox.showerror("エラー", f"ファイルを保存できませんでした:\n{e}")
    
    def update_cursor_position(self, event=None):
        # カーソルの現在位置を取得
        cursor_position = self.text_area.index(tk.INSERT)
        line, column = cursor_position.split('.')
        self.status_bar.config(text=f"行: {line}, 列: {column}")

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop() 