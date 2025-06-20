"""
tkinter フォームアプリケーション
"""
import tkinter as tk
from tkinter import messagebox


class FormApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("フォーム入力")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # 名前入力
        tk.Label(self, text="名前:", font=("Arial", 12)).pack(pady=(20, 5))
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name_var, width=30, font=("Arial", 11))
        self.name_entry.pack()
        
        # 年齢入力
        tk.Label(self, text="年齢:", font=("Arial", 12)).pack(pady=(10, 5))
        self.age_var = tk.StringVar()
        self.age_entry = tk.Entry(self, textvariable=self.age_var, width=30, font=("Arial", 11))
        self.age_entry.pack()
        
        # パスワード入力
        tk.Label(self, text="パスワード:", font=("Arial", 12)).pack(pady=(10, 5))
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            self, 
            textvariable=self.password_var, 
            width=30, 
            font=("Arial", 11),
            show="*"  # パスワードを隠す
        )
        self.password_entry.pack()
        
        # ボタン
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        submit_button = tk.Button(button_frame, text="送信", command=self.submit_form)
        submit_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(button_frame, text="クリア", command=self.clear_form)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # 初期フォーカスを名前入力に設定
        self.name_entry.focus()
    
    def submit_form(self):
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        password = self.password_var.get()
        
        if not name:
            messagebox.showerror("エラー", "名前を入力してください。")
            self.name_entry.focus()
            return
        
        if not age:
            messagebox.showerror("エラー", "年齢を入力してください。")
            self.age_entry.focus()
            return
        
        try:
            age_int = int(age)
            if age_int < 0 or age_int > 150:
                raise ValueError
        except ValueError:
            messagebox.showerror("エラー", "有効な年齢を入力してください。")
            self.age_entry.focus()
            return
        
        if not password:
            messagebox.showerror("エラー", "パスワードを入力してください。")
            self.password_entry.focus()
            return
        
        messagebox.showinfo("送信完了", f"名前: {name}\n年齢: {age}\nパスワードは設定されました。")
    
    def clear_form(self):
        self.name_var.set("")
        self.age_var.set("")
        self.password_var.set("")
        self.name_entry.focus()

if __name__ == "__main__":
    app = FormApp()
    app.mainloop()