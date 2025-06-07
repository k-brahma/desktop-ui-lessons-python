"""
tkinter 基本的なテキストラベル
"""
import tkinter as tk


class BasicLabelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Labelの例")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        # ラベルを作成し、ウィンドウに配置
        self.label = tk.Label(self, text="こんにちは, tkinter!")
        self.label.pack(pady=20)

if __name__ == "__main__":
    app = BasicLabelApp()
    app.mainloop()