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
        print("show_infoがはじまります！")
        messagebox.showinfo("情報", "これは情報メッセージです。")
        print("show_infoが終わります！")

    def show_warning(self):
        print("show_warningがはじまりまず")
        messagebox.showwarning("警告", "これは警告メッセージです。")
        print("show_warningがおまります")

    def show_error(self):
        print("show_errorがはじまります")
        messagebox.showerror("エラー", "これはエラーメッセージです。")
        print("show_errorがおまります")

if __name__ == "__main__":
    app = BasicMessageboxApp()
    app.mainloop() 