"""
tkinter 基本的なウィンドウの作成
"""
import tkinter as tk

# ルートウィンドウの作成
app = tk.Tk()

# ウィンドウのタイトルを設定
app.title("シンプルなウィンドウ")

# ウィンドウのサイズを設定 (幅x高さ)
app.geometry("300x200")

# イベントループを開始
app.mainloop()
