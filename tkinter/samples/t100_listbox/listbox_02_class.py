"""
tkinter クラスベースでのリストボックス例
"""
import tkinter as tk


class ListboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Listboxの例（クラスベース）")
        self.geometry("300x250")
        
        self.create_widgets()
    
    def create_widgets(self):
        # リストボックスの作成
        self.listbox = tk.Listbox(self, height=6)
        self.listbox.pack(pady=20)
        
        # 項目を追加
        items = ["りんご", "みかん", "バナナ", "ぶどう", "いちご", "メロン", "スイカ"]
        for item in items:
            self.listbox.insert(tk.END, item)
        
        # 選択イベントをバインド
        self.listbox.bind("<<ListboxSelect>>", self.on_selection)
    
    def on_selection(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            value = self.listbox.get(index)
            print(f"選択された項目: {value} (インデックス: {index})")

if __name__ == "__main__":
    app = ListboxApp()
    app.mainloop() 