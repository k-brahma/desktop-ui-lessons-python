"""
tkinter クラスベースでのレイアウト例（Grid）
"""
import tkinter as tk
from tkinter import messagebox


class GridLayoutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Grid レイアウトの例（クラスベース）")
        self.geometry("450x400")
        
        self.create_widgets()
        self.configure_grid()
    
    def create_widgets(self):
        # ヘッダー（複数列にわたって配置）
        header_label = tk.Label(
            self, 
            text="ユーザー登録フォーム", 
            bg="darkblue", 
            fg="white", 
            font=("Arial", 16, "bold"),
            height=2
        )
        header_label.grid(row=0, column=0, columnspan=3, sticky="ew", pady=5)
        
        # フォームのラベル
        tk.Label(self, text="名前:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=8)
        tk.Label(self, text="メール:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=10, pady=8)
        tk.Label(self, text="年齢:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=10, pady=8)
        tk.Label(self, text="性別:", font=("Arial", 12)).grid(row=4, column=0, sticky="e", padx=10, pady=8)
        tk.Label(self, text="自己紹介:", font=("Arial", 12)).grid(row=5, column=0, sticky="ne", padx=10, pady=8)
        
        # 入力フィールド
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name_var, width=25, font=("Arial", 11))
        self.name_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=8)
        
        self.email_var = tk.StringVar()
        self.email_entry = tk.Entry(self, textvariable=self.email_var, width=25, font=("Arial", 11))
        self.email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=8)
        
        self.age_var = tk.StringVar()
        self.age_entry = tk.Entry(self, textvariable=self.age_var, width=25, font=("Arial", 11))
        self.age_entry.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=8)
        
        # 性別選択（ラジオボタン）
        self.gender_var = tk.StringVar(value="male")
        gender_frame = tk.Frame(self)
        gender_frame.grid(row=4, column=1, columnspan=2, sticky="w", padx=10, pady=8)
        
        tk.Radiobutton(gender_frame, text="男性", variable=self.gender_var, value="male").pack(side=tk.LEFT)
        tk.Radiobutton(gender_frame, text="女性", variable=self.gender_var, value="female").pack(side=tk.LEFT, padx=(20, 0))
        tk.Radiobutton(gender_frame, text="その他", variable=self.gender_var, value="other").pack(side=tk.LEFT, padx=(20, 0))
        
        # 自己紹介（テキストエリア）
        self.intro_text = tk.Text(self, width=30, height=6, font=("Arial", 11), wrap=tk.WORD)
        self.intro_text.grid(row=5, column=1, columnspan=2, sticky="nsew", padx=10, pady=8)
        
        # ボタン
        button_frame = tk.Frame(self)
        button_frame.grid(row=6, column=0, columnspan=3, pady=20)
        
        tk.Button(button_frame, text="登録", command=self.submit_form, bg="green", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="クリア", command=self.clear_form, bg="orange", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="キャンセル", command=self.cancel, bg="red", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        
        # 初期フォーカス
        self.name_entry.focus()
    
    def configure_grid(self):
        # 列の重みを設定（リサイズ時の動作）
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        # 行の重みを設定（自己紹介欄が拡張される）
        self.grid_rowconfigure(5, weight=1)
    
    def submit_form(self):
        # フォームの内容を取得
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        age = self.age_var.get().strip()
        gender = self.gender_var.get()
        intro = self.intro_text.get(1.0, tk.END).strip()
        
        # 簡単なバリデーション
        if not name:
            messagebox.showerror("エラー", "名前を入力してください。")
            self.name_entry.focus()
            return
        
        if not email:
            messagebox.showerror("エラー", "メールアドレスを入力してください。")
            self.email_entry.focus()
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
        
        # 登録成功メッセージ
        gender_text = {"male": "男性", "female": "女性", "other": "その他"}[gender]
        message = f"登録情報:\n名前: {name}\nメール: {email}\n年齢: {age}\n性別: {gender_text}"
        if intro:
            message += f"\n自己紹介: {intro[:50]}..."
        
        messagebox.showinfo("登録完了", message)
    
    def clear_form(self):
        if messagebox.askyesno("確認", "フォームの内容をクリアしますか？"):
            self.name_var.set("")
            self.email_var.set("")
            self.age_var.set("")
            self.gender_var.set("male")
            self.intro_text.delete(1.0, tk.END)
            self.name_entry.focus()
    
    def cancel(self):
        if messagebox.askyesno("確認", "入力を中止しますか？"):
            self.quit()

if __name__ == "__main__":
    app = GridLayoutApp()
    app.mainloop() 