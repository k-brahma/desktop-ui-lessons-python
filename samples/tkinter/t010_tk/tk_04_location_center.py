"""
tkinter ウィンドウの中央表示
"""
import tkinter as tk


class CenterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("中央表示ウィンドウ")
        
        window_width = 400
        window_height = 300
        
        # 画面の解像度を取得
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # 中央に表示するための座標を計算
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

if __name__ == "__main__":
    app = CenterApp()
    app.mainloop() 