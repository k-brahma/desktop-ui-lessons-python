"""
tkinter クラスベースでのコンボボックス例
"""
import tkinter as tk
from tkinter import ttk


class ComboboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Comboboxの例（クラスベース）")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        # コンボボックスの作成
        values = ["りんご", "みかん", "バナナ", "ぶどう", "いちご"]
        self.combobox = ttk.Combobox(self, values=values)
        self.combobox.set("りんご")  # 初期値を設定
        self.combobox.bind("<<ComboboxSelected>>", self.on_selection)
        self.combobox.pack(pady=20)
    
    def on_selection(self, event):
        selection = self.combobox.get()
        print(f"選択された項目: {selection}")

if __name__ == "__main__":
    app = ComboboxApp()
    app.mainloop() 