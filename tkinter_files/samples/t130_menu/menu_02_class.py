"""
tkinter クラスベースでのメニュー例
"""
import tkinter as tk
from tkinter import messagebox


class MenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Menuの例（クラスベース）")
        self.geometry("400x300")
        
        self.create_menu()
        self.create_widgets()
    
    def create_menu(self):
        # メニューバーを作成
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        
        # ファイルメニューを作成
        file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="ファイル", menu=file_menu)
        file_menu.add_command(label="新規", command=self.new_file)
        file_menu.add_command(label="開く", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="終了", command=self.quit)
        
        # 編集メニューを作成
        edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="編集", menu=edit_menu)
        edit_menu.add_command(label="元に戻す", command=self.undo)
        edit_menu.add_command(label="やり直し", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="コピー", command=self.copy)
        edit_menu.add_command(label="貼り付け", command=self.paste)

    def create_widgets(self):
        # メインエリア
        self.text_area = tk.Text(self, wrap=tk.WORD, font=("Arial", 11), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.text_area.insert(1.0, "メニューバーの機能を試してください。\n編集メニューでテキストを操作できます。")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        messagebox.showinfo("新規", "新しいファイルを作成しました")
    
    def open_file(self):
        messagebox.showinfo("開く", "ファイルを開く機能（未実装）")
    
    def undo(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            messagebox.showinfo("元に戻す", "元に戻す操作がありません")
    
    def redo(self):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            messagebox.showinfo("やり直し", "やり直す操作がありません")
    
    def copy(self):
        try:
            # 選択されたテキストがあるか確認
            selection = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.text_area.event_generate("<<Copy>>")
            messagebox.showinfo("コピー", f"選択したテキストをコピーしました: {selection[:20]}...")
        except tk.TclError:
            messagebox.showwarning("コピー", "コピーするテキストを選択してください")
    
    def paste(self):
        self.text_area.event_generate("<<Paste>>")
        messagebox.showinfo("貼り付け", "テキストを貼り付けました")

if __name__ == "__main__":
    app = MenuApp()
    app.mainloop() 