"""
tkinter ウィンドウ位置の指定
"""
import tkinter as tk


class LocationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("位置指定ウィンドウ")
        
        # 幅 400, 高さ 300, 画面の (100, 200) の位置に表示
        self.geometry("400x300+100+200")

if __name__ == "__main__":
    app = LocationApp()
    app.mainloop() 