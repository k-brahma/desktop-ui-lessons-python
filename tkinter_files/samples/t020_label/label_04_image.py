"""
tkinter 画像の表示（ダミー画像使用）
"""
import tkinter as tk


class ImageLabelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("画像ラベル")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        try:
            # ダミーの画像を作成（50x50ピクセルの赤い正方形）
            # 実際の使用時は実在の画像ファイルを指定してください
            self.photo_image = tk.PhotoImage(width=50, height=50)
            
            # 画像全体を赤色で塗りつぶし
            for x in range(50):
                for y in range(50):
                    self.photo_image.put("#FF0000", (x, y))
            
            self.label = tk.Label(self, image=self.photo_image)
            self.label.pack(pady=20)
            
            self.info_label = tk.Label(self, text="ダミー画像 (50x50 赤色)", font=("Arial", 12))
            self.info_label.pack()
            
        except Exception as e:
            # 画像を表示できない場合のフォールバック
            self.label = tk.Label(self, text="画像を表示できませんでした")
            self.label.pack(pady=20)
            
            self.error_label = tk.Label(self, text=f"エラー: {str(e)}", fg="red")
            self.error_label.pack()

if __name__ == "__main__":
    app = ImageLabelApp()
    app.mainloop() 