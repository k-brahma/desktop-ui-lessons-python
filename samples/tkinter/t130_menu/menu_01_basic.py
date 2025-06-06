"""
tkinter 基本的なメニュー
"""
import tkinter as tk
from tkinter import messagebox


class BasicMenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Menuの例")
        self.geometry("400x300")
        
        self.create_menu()
        self.create_widgets()
    
    def create_menu(self):
        # メニューバーを作成
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # ファイルメニューを作成
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="ファイル", menu=file_menu)
        file_menu.add_command(label="新規", command=self.new_file)
        file_menu.add_command(label="開く", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="終了", command=self.quit)

    def create_widgets(self):
        # メインエリア
        label = tk.Label(self, text="メニューバーの項目を選択してください", font=("Arial", 12))
        label.pack(expand=True)

    def new_file(self):
        messagebox.showinfo("新規", "新しいファイルを作成します")

    def open_file(self):
        messagebox.showinfo("開く", "ファイルを開きます")

if __name__ == "__main__":
    app = BasicMenuApp()
    app.mainloop() 