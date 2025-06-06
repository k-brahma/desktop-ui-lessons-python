"""
tkinter 実用的なメッセージボックス例
"""
import os
import tkinter as tk
from tkinter import filedialog, messagebox


class PracticalMessageboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("実用的なメッセージボックス例")
        self.geometry("500x400")
        
        self.current_file = None
        self.is_modified = False
        self.create_widgets()
    
    def create_widgets(self):
        # メニューバー
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # ファイルメニュー
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="ファイル", menu=file_menu)
        file_menu.add_command(label="新規", command=self.new_file)
        file_menu.add_command(label="開く", command=self.open_file)
        file_menu.add_command(label="保存", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="終了", command=self.quit_app)
        
        # ツールバー
        toolbar = tk.Frame(self, relief=tk.RAISED, bd=1)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        tk.Button(toolbar, text="新規", command=self.new_file, width=8).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="開く", command=self.open_file, width=8).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="保存", command=self.save_file, width=8).pack(side=tk.LEFT, padx=2, pady=2)
        
        # 区切り線
        tk.Frame(toolbar, width=2, bg="gray").pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        # 危険な操作ボタン
        tk.Button(toolbar, text="全削除", command=self.clear_all, bg="red", fg="white", width=8).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="設定リセット", command=self.reset_settings, bg="orange", fg="white", width=10).pack(side=tk.LEFT, padx=2, pady=2)
        
        # テキストエリア
        text_frame = tk.Frame(self)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.text_area = tk.Text(text_frame, wrap=tk.WORD, font=("Consolas", 11), undo=True)
        scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # テキスト変更の監視
        self.text_area.bind("<KeyPress>", self.on_text_change)
        self.text_area.bind("<Button-1>", self.on_text_change)
        
        # ステータスバー
        self.status_bar = tk.Label(self, text="準備完了", relief=tk.SUNKEN, anchor=tk.W, bg="lightgray")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 初期テキスト
        self.text_area.insert(1.0, "新しいドキュメント\n\nここにテキストを入力してください。\nファイル操作でメッセージボックスの動作を確認できます。")
        self.is_modified = False
        self.update_title()
    
    def on_text_change(self, event=None):
        if not self.is_modified:
            self.is_modified = True
            self.update_title()
    
    def update_title(self):
        title = "実用的なメッセージボックス例"
        if self.current_file:
            title += f" - {os.path.basename(self.current_file)}"
        if self.is_modified:
            title += " *"
        self.title(title)
    
    def check_unsaved_changes(self):
        """未保存の変更があるかチェックし、保存するか確認"""
        if not self.is_modified:
            return True
        
        result = messagebox.askyesnocancel(
            "未保存の変更",
            "ドキュメントに未保存の変更があります。\n保存しますか？",
            icon="warning"
        )
        
        if result is True:  # はい
            return self.save_file()
        elif result is False:  # いいえ
            return True
        else:  # キャンセル
            return False
    
    def new_file(self):
        if self.check_unsaved_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.is_modified = False
            self.update_title()
            self.status_bar.config(text="新しいドキュメントを作成しました")
            messagebox.showinfo("新規作成", "新しいドキュメントを作成しました。")
    
    def open_file(self):
        if self.check_unsaved_changes():
            filename = filedialog.askopenfilename(
                title="ファイルを開く",
                filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")]
            )
            if filename:
                try:
                    with open(filename, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.text_area.delete(1.0, tk.END)
                        self.text_area.insert(1.0, content)
                        self.current_file = filename
                        self.is_modified = False
                        self.update_title()
                        self.status_bar.config(text=f"ファイルを開きました: {os.path.basename(filename)}")
                        messagebox.showinfo("ファイルを開く", f"ファイルを開きました:\n{os.path.basename(filename)}")
                except Exception as e:
                    messagebox.showerror("エラー", f"ファイルを開けませんでした:\n{str(e)}")
    
    def save_file(self):
        if not self.current_file:
            return self.save_as_file()
        
        try:
            content = self.text_area.get(1.0, tk.END)
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(content)
            self.is_modified = False
            self.update_title()
            self.status_bar.config(text=f"ファイルを保存しました: {os.path.basename(self.current_file)}")
            messagebox.showinfo("保存完了", f"ファイルを保存しました:\n{os.path.basename(self.current_file)}")
            return True
        except Exception as e:
            messagebox.showerror("保存エラー", f"ファイルを保存できませんでした:\n{str(e)}")
            return False
    
    def save_as_file(self):
        filename = filedialog.asksaveasfilename(
            title="名前を付けて保存",
            defaultextension=".txt",
            filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")]
        )
        if filename:
            self.current_file = filename
            return self.save_file()
        return False
    
    def clear_all(self):
        # 段階的な確認
        if messagebox.askokcancel("確認", "本当にすべてのテキストを削除しますか？", icon="warning"):
            if messagebox.askyesno("最終確認", "この操作は元に戻せません。\n本当に削除しますか？", icon="warning"):
                self.text_area.delete(1.0, tk.END)
                self.is_modified = True
                self.update_title()
                self.status_bar.config(text="すべてのテキストを削除しました")
                messagebox.showinfo("削除完了", "すべてのテキストを削除しました。")
    
    def reset_settings(self):
        result = messagebox.askyesnocancel(
            "設定リセット",
            "アプリケーションの設定をリセットしますか？\n\n・ウィンドウサイズがリセットされます\n・フォント設定がリセットされます\n・最近使用したファイルがクリアされます",
            icon="question"
        )
        
        if result is True:
            # 設定リセットの実行
            self.geometry("500x400")
            self.text_area.config(font=("Consolas", 11))
            messagebox.showinfo("リセット完了", "設定をリセットしました。")
            self.status_bar.config(text="設定をリセットしました")
        elif result is False:
            messagebox.showinfo("キャンセル", "設定のリセットをキャンセルしました。")
        # None の場合は何もしない
    
    def quit_app(self):
        if self.check_unsaved_changes():
            if messagebox.askokcancel("終了確認", "アプリケーションを終了しますか？"):
                self.quit()

if __name__ == "__main__":
    app = PracticalMessageboxApp()
    app.mainloop() 