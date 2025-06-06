"""
tkinter 実践的なクラスベースアプリケーション
"""
import tkinter as tk
from tkinter import messagebox


class PracticalApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("クラスベースのアプリ")
        self.geometry("400x300")

        self.create_widgets()
        
        # ウィンドウの閉じるボタンの挙動を設定
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        # ラベルの作成
        self.label = tk.Label(self, text="これはクラスベースのtkinterアプリケーションです。")
        self.label.pack(pady=20)

        # ボタンの作成
        self.greet_button = tk.Button(self, text="挨拶", command=self.say_hello)
        self.greet_button.pack()
        
        # 終了ボタン
        self.quit_button = tk.Button(self, text="終了", command=self.on_closing)
        self.quit_button.pack(pady=10)

    def say_hello(self):
        messagebox.showinfo("挨拶", "こんにちは！")
        
    def on_closing(self):
        if messagebox.askokcancel("終了確認", "本当にアプリケーションを終了しますか？"):
            self.destroy()

if __name__ == "__main__":
    app = PracticalApp()
    app.mainloop() 