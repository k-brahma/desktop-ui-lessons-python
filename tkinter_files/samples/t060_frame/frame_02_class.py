"""
tkinter クラスベースでのフレーム作成例
"""
import tkinter as tk


class FrameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Frameの例（クラスベース）")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # メインフレーム
        self.main_frame = tk.Frame(self, bg="lightblue", relief=tk.RAISED, bd=2)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # フレーム内にウィジェットを配置
        self.label = tk.Label(self.main_frame, text="フレーム内のラベル", bg="lightblue")
        self.label.pack(pady=10)
        
        self.button = tk.Button(self.main_frame, text="フレーム内のボタン")
        self.button.pack(pady=5)

if __name__ == "__main__":
    app = FrameApp()
    app.mainloop() 