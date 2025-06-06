"""
tkinter 基本的なメッセージボックス
"""
import tkinter as tk
from tkinter import messagebox


class BasicMessageboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Messageboxの例")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="メッセージボックスのテスト", font=("Arial", 14, "bold")).pack(pady=20)
        
        tk.Button(self, text="情報を表示", command=self.show_info, width=15).pack(pady=5)
        tk.Button(self, text="警告を表示", command=self.show_warning, width=15).pack(pady=5)
        tk.Button(self, text="エラーを表示", command=self.show_error, width=15).pack(pady=5)

    def show_info(self):
        messagebox.showinfo("情報", "これは情報メッセージです。")

    def show_warning(self):
        messagebox.showwarning("警告", "これは警告メッセージです。")

    def show_error(self):
        messagebox.showerror("エラー", "これはエラーメッセージです。")

if __name__ == "__main__":
    app = BasicMessageboxApp()
    app.mainloop() 