import tkinter as tk
from tkinter import font


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ボタンクリックデモ")
        self.root.geometry("400x300+100+100")

        # ラベルの作成
        self.result_label = tk.Label(
            self.root,
            text="こんにちはようこそ！",
            bg="black",
            fg="white",
            font=("Arial", 20)
        )
        self.result_label.pack(expand=True)


if __name__ == "__main__":
    window = MainWindow()
    window.root.mainloop() 