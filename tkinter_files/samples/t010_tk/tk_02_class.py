"""
tkinter クラスベースでの作成例
"""
import tkinter as tk


class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # ウィンドウの設定
        self.title("シンプルなウィンドウ（クラスベース）")
        self.geometry("300x200")


if __name__ == "__main__":
    app = SimpleApp()
    app.mainloop() 