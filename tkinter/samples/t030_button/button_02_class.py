"""
tkinter クラスベースでのボタン作成例
"""
import tkinter as tk


class ButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Buttonの例（クラスベース）")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.button = tk.Button(self, text="クリックしてください", command=self.button_clicked)
        self.button.pack(pady=20)
    
    def button_clicked(self):
        print("ボタンがクリックされました！")

if __name__ == "__main__":
    app = ButtonApp()
    app.mainloop() 