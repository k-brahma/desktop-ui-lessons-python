import tkinter as tk
from datetime import datetime


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ボタンクリックデモ")
        self.root.geometry("400x300+100+100")

        # ラベルの作成
        self.result_label = tk.Label(
            self.root,
            text="結果がここに表示されます"
        )
        self.result_label.pack(expand=True)

        # ボタンの作成
        self.click_button = tk.Button(
            self.root,
            text="クリックしてください",
            command=self.on_button_click
        )
        self.click_button.pack(expand=True)

    def on_button_click(self):
        """今の日付時刻を表示する"""
        current_datetime = datetime.now()
        result = current_datetime.strftime("%Y/%m/%d %H:%M:%S")
        self.result_label.config(text=result)


if __name__ == "__main__":
    window = MainWindow()
    window.root.mainloop() 