"""
tkinter 基本的なテキスト入力
"""
import tkinter as tk


class BasicEntryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Entryの例")
        self.geometry("400x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.entry = tk.Entry(self, width=30)
        self.entry.pack(pady=20)
        
        self.button = tk.Button(self, text="テキストを取得", command=self.get_text)
        self.button.pack()
    
    def get_text(self):
        text = self.entry.get()
        print(f"入力されたテキスト: {text}")

if __name__ == "__main__":
    app = BasicEntryApp()
    app.mainloop() 