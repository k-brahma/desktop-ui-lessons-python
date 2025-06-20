"""
tkinter ウィンドウ終了の確認
"""
import tkinter as tk
from tkinter import messagebox


class CloseConfirmApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("終了確認")
        self.geometry("300x200")
        
        # ウィンドウの閉じるボタンにカスタム関数をバインド
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        if messagebox.askokcancel("終了", "本当に終了しますか？"):
            self.destroy()

if __name__ == "__main__":
    app = CloseConfirmApp()
    app.mainloop() 