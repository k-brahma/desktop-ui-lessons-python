"""
tkinter 画像付きボタン（ダミー画像使用）
"""
import tkinter as tk
from tkinter import messagebox


class ImageButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("画像ボタンの例")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        try:
            # ダミーの画像を作成（32x32ピクセルの青い正方形）
            self.photo = tk.PhotoImage(width=32, height=32)
            
            # 画像全体を青色で塗りつぶし
            for x in range(32):
                for y in range(32):
                    self.photo.put("#0000FF", (x, y))
            
            # 画像付きボタン
            self.image_button = tk.Button(
                self, 
                text="画像ボタン", 
                image=self.photo, 
                compound=tk.LEFT,  # 画像をテキストの左に配置
                command=self.image_button_clicked,
                font=("Arial", 12)
            )
            self.image_button.pack(pady=20)
            
            # 通常のテキストボタン
            self.text_button = tk.Button(
                self,
                text="テキストボタン",
                command=self.text_button_clicked,
                bg="lightgray",
                font=("Arial", 12)
            )
            self.text_button.pack(pady=10)
            
        except Exception as e:
            # 画像を作成できない場合のフォールバック
            self.error_button = tk.Button(
                self,
                text="画像ボタン（エラー）",
                command=self.error_button_clicked,
                bg="lightcoral",
                font=("Arial", 12)
            )
            self.error_button.pack(pady=20)
    
    def image_button_clicked(self):
        messagebox.showinfo("画像ボタン", "画像付きボタンがクリックされました！")
    
    def text_button_clicked(self):
        messagebox.showinfo("テキストボタン", "テキストボタンがクリックされました！")
    
    def error_button_clicked(self):
        messagebox.showerror("エラー", "画像を作成できませんでした")

if __name__ == "__main__":
    app = ImageButtonApp()
    app.mainloop() 