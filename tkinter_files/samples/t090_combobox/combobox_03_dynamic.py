"""
tkinter 動的コンボボックス
"""
import tkinter as tk
from tkinter import ttk


class DynamicComboboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("動的コンボボックス")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # カテゴリ選択
        tk.Label(self, text="カテゴリを選択:", font=("Arial", 12)).pack(pady=10)
        
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(
            self, 
            textvariable=self.category_var,
            values=["果物", "野菜", "肉類", "魚類"],
            state="readonly"
        )
        self.category_combo.bind("<<ComboboxSelected>>", self.on_category_changed)
        self.category_combo.pack(pady=5)
        
        # 商品選択
        tk.Label(self, text="商品を選択:", font=("Arial", 12)).pack(pady=(20, 10))
        
        self.product_var = tk.StringVar()
        self.product_combo = ttk.Combobox(
            self, 
            textvariable=self.product_var,
            state="disabled"
        )
        self.product_combo.bind("<<ComboboxSelected>>", self.on_product_selected)
        self.product_combo.pack(pady=5)
        
        # 結果表示
        self.result_label = tk.Label(self, text="", font=("Arial", 11), fg="blue")
        self.result_label.pack(pady=20)
        
        # 商品データ
        self.products = {
            "果物": ["りんご", "みかん", "バナナ", "ぶどう", "いちご"],
            "野菜": ["キャベツ", "人参", "玉ねぎ", "じゃがいも", "トマト"],
            "肉類": ["牛肉", "豚肉", "鶏肉", "ラム肉"],
            "魚類": ["サーモン", "マグロ", "アジ", "サバ", "イワシ"]
        }
    
    def on_category_changed(self, event):
        category = self.category_var.get()
        if category in self.products:
            # 商品選択肢を更新
            self.product_combo.configure(values=self.products[category])
            self.product_combo.set("")  # 選択をリセット
            self.product_combo.configure(state="readonly")
            self.result_label.config(text="")
    
    def on_product_selected(self, event):
        category = self.category_var.get()
        product = self.product_var.get()
        self.result_label.config(text=f"選択: {category} - {product}")

if __name__ == "__main__":
    app = DynamicComboboxApp()
    app.mainloop() 