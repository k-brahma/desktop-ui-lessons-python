"""
tkinter クラスベースでのテキストエディタ例
"""
import tkinter as tk


class TextApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Textの例（クラスベース）")
        self.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.text_widget = tk.Text(self, width=60, height=15)
        self.text_widget.pack(pady=20)
        
        self.button = tk.Button(self, text="テキストを取得", command=self.get_text)
        self.button.pack()
    
    def get_text(self):
        content = self.text_widget.get("1.0", tk.END)
        print(f"テキストの内容:\n{content}")

if __name__ == "__main__":
    app = TextApp()
    app.mainloop() 