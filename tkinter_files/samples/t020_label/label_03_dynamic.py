"""
tkinter テキストの動的更新
"""
import random
import tkinter as tk


class DynamicLabelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("動的ラベル")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        # StringVarを作成
        self.text_variable = tk.StringVar()
        self.text_variable.set("ボタンを押してください")
        
        self.label = tk.Label(
            self, 
            textvariable=self.text_variable,
            font=("Helvetica", 14),
            pady=20
        )
        self.label.pack()
        
        self.button = tk.Button(self, text="更新", command=self.update_text)
        self.button.pack()
    
    def update_text(self):
        # StringVarの値を更新すると、ラベルの表示も変わる
        random_number = random.randint(1, 100)
        self.text_variable.set(f"ランダムな数字: {random_number}")

if __name__ == "__main__":
    app = DynamicLabelApp()
    app.mainloop() 