"""
tkinter クラスベースでのスケール例
"""
import tkinter as tk


class ScaleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Scaleの例（クラスベース）")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.scale_var = tk.IntVar(value=50)
        
        # 水平スケールの作成
        self.scale = tk.Scale(
            self, 
            from_=0, 
            to=100, 
            orient=tk.HORIZONTAL,
            variable=self.scale_var,
            command=self.on_scale_change
        )
        self.scale.pack(pady=20)
        
        self.label = tk.Label(self, text="現在の値: 50")
        self.label.pack()
    
    def on_scale_change(self, value):
        self.label.config(text=f"現在の値: {self.scale_var.get()}")

if __name__ == "__main__":
    app = ScaleApp()
    app.mainloop() 