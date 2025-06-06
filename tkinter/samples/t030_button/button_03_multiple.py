"""
tkinter 複数のボタンを持つアプリケーション
"""
import tkinter as tk
from tkinter import messagebox


class MultipleButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ボタンアプリケーション")
        self.geometry("400x300")
        
        self.counter = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        # カウンター表示用ラベル
        self.counter_label = tk.Label(self, text=f"カウント: {self.counter}", font=("Arial", 14))
        self.counter_label.pack(pady=10)
        
        # カウンターを増やすボタン
        self.increment_button = tk.Button(
            self, 
            text="カウント+1", 
            command=self.increment_counter,
            bg="lightblue",
            font=("Arial", 12)
        )
        self.increment_button.pack(pady=5)
        
        # カウンターをリセットするボタン
        self.reset_button = tk.Button(
            self, 
            text="リセット", 
            command=self.reset_counter,
            bg="orange",
            font=("Arial", 12)
        )
        self.reset_button.pack(pady=5)
        
        # 確認ダイアログを表示するボタン
        self.dialog_button = tk.Button(
            self, 
            text="確認ダイアログ", 
            command=self.show_dialog,
            bg="lightgreen",
            font=("Arial", 12)
        )
        self.dialog_button.pack(pady=5)
        
        # 無効化/有効化ボタン
        self.toggle_button = tk.Button(
            self, 
            text="ボタンを無効化", 
            command=self.toggle_buttons,
            bg="lightcoral",
            font=("Arial", 12)
        )
        self.toggle_button.pack(pady=5)
    
    def increment_counter(self):
        self.counter += 1
        self.counter_label.config(text=f"カウント: {self.counter}")
    
    def reset_counter(self):
        self.counter = 0
        self.counter_label.config(text=f"カウント: {self.counter}")
    
    def show_dialog(self):
        messagebox.showinfo("情報", f"現在のカウント: {self.counter}")
    
    def toggle_buttons(self):
        current_state = self.increment_button['state']
        if current_state == 'normal':
            # ボタンを無効化
            self.increment_button.config(state='disabled')
            self.reset_button.config(state='disabled')
            self.dialog_button.config(state='disabled')
            self.toggle_button.config(text="ボタンを有効化")
        else:
            # ボタンを有効化
            self.increment_button.config(state='normal')
            self.reset_button.config(state='normal')
            self.dialog_button.config(state='normal')
            self.toggle_button.config(text="ボタンを無効化")

if __name__ == "__main__":
    app = MultipleButtonApp()
    app.mainloop() 