"""
tkinter 基本的なスケール
"""
import tkinter as tk


class BasicScaleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Scaleの例")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        # 水平スケールの作成
        self.scale = tk.Scale(
            self, 
            from_=0, 
            to=100, 
            orient=tk.HORIZONTAL,
            command=self.on_scale_change
        )
        self.scale.set(50)  # 初期値を設定
        self.scale.pack(pady=20)
        
        self.value_label = tk.Label(self, text="値: 50")
        self.value_label.pack()
    
    def on_scale_change(self, value):
        self.value_label.config(text=f"値: {value}")

if __name__ == "__main__":
    app = BasicScaleApp()
    app.mainloop() 