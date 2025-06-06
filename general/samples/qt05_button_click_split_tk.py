import tkinter as tk
from datetime import datetime
from tkinter import font


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self._setup_main_window()
        self._setup_label()
        self._setup_button()

    def _setup_main_window(self):
        """メインウィンドウの設定"""
        self.root.title("ボタンクリックデモ")
        self.root.geometry("400x300+100+100")

    def _setup_label(self):
        """ラベルの作成"""
        self.result_label = tk.Label(
            self.root,
            text="結果がここに表示されます",
            bg="black",
            fg="white",
            font=("Arial", 20)
        )
        self.result_label.pack(expand=True)

    def _setup_button(self):
        """ボタンの作成"""
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