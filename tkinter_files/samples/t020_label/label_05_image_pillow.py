"""
tkinter 画像の表示（ダミー画像使用）
"""
import os
import tkinter as tk


class ImageLabelApp(tk.Tk):
   def __init__(self):
       super().__init__()
       
       self.title("画像ラベル")
       self.photo_image = None  # 画像の参照を保持するための属性
       
       self.load_image()
       self.create_widgets()
   
   def load_image(self):
        """画像を読み込む"""
        # tkinterが標準でサポートしているのはGIFとPGM/PPM形式です。
        # PNGやJPEGなどを扱うには、Pillowライブラリ(pip install Pillow)が必要です。
        # 以下では、 gif を読み込むコードを示しています。
        try:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            self.photo_image = tk.PhotoImage(file=os.path.join(dir_path, "img/img.png"))
        except tk.TclError:
            self.photo_image = None
            print("画像ファイルが見つからないか、非対応の形式です。")
   
   def create_widgets(self):
       """ウィジェットを作成・配置"""
       if self.photo_image:
           self.label = tk.Label(self, image=self.photo_image)
           # 参照を保持（ガベージコレクション防止）
           self.label.image = self.photo_image
           self.label.pack(pady=20)
       else:
           self.label = tk.Label(self, text="画像を表示できませんでした")
           self.label.pack(pady=20)

if __name__ == "__main__":
   app = ImageLabelApp()
   app.mainloop()