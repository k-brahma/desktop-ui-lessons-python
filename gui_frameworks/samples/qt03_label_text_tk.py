import tkinter as tk
from datetime import datetime


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ボタンクリックデモ")
        self.root.geometry("400x300+100+100")

        # ラベルの作成
        current_datetime = datetime.now()
        self.result_label = tk.Label(
            self.root,
            text=current_datetime.strftime("%Y/%m/%d %H:%M:%S")
        )
        self.result_label.pack(expand=True)


if __name__ == "__main__":
    window = MainWindow()
    window.root.mainloop() 