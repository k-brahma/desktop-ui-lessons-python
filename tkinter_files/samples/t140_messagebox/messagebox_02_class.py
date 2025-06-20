"""
tkinter クラスベースでのメッセージボックス例
"""
import tkinter as tk
from tkinter import messagebox


class MessageboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Messageboxの例（クラスベース）")
        self.geometry("350x350")
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="メッセージボックスの種類", font=("Arial", 14, "bold")).pack(pady=20)
        
        # 情報表示系
        info_frame = tk.Frame(self)
        info_frame.pack(pady=10)
        tk.Label(info_frame, text="情報表示:", font=("Arial", 10, "bold")).pack()
        tk.Button(info_frame, text="情報", command=self.show_info, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(info_frame, text="警告", command=self.show_warning, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(info_frame, text="エラー", command=self.show_error, width=12).pack(side=tk.LEFT, padx=2)
        
        # 確認系
        confirm_frame = tk.Frame(self)
        confirm_frame.pack(pady=10)
        tk.Label(confirm_frame, text="確認ダイアログ:", font=("Arial", 10, "bold")).pack()
        tk.Button(confirm_frame, text="はい/いいえ", command=self.show_question, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(confirm_frame, text="OK/キャンセル", command=self.show_okcancel, width=12).pack(side=tk.LEFT, padx=2)
        
        # 複雑な確認
        complex_frame = tk.Frame(self)
        complex_frame.pack(pady=10)
        tk.Label(complex_frame, text="3択ダイアログ:", font=("Arial", 10, "bold")).pack()
        tk.Button(complex_frame, text="はい/いいえ/キャンセル", command=self.show_yesnocancel, width=20).pack()
        
        # 結果表示エリア
        tk.Label(self, text="結果:", font=("Arial", 10, "bold")).pack(pady=(20, 5))
        self.result_label = tk.Label(self, text="ボタンを押して結果を確認してください", fg="blue", font=("Arial", 10))
        self.result_label.pack()
    
    def show_info(self):
        messagebox.showinfo("情報", "これは情報メッセージです。")
        self.result_label.config(text="情報ダイアログを表示しました")
    
    def show_warning(self):
        messagebox.showwarning("警告", "これは警告メッセージです。")
        self.result_label.config(text="警告ダイアログを表示しました")
    
    def show_error(self):
        messagebox.showerror("エラー", "これはエラーメッセージです。")
        self.result_label.config(text="エラーダイアログを表示しました")
    
    def show_question(self):
        result = messagebox.askyesno("確認", "本当に実行しますか？")
        if result:
            self.result_label.config(text="結果: 「はい」が選択されました")
        else:
            self.result_label.config(text="結果: 「いいえ」が選択されました")
    
    def show_okcancel(self):
        result = messagebox.askokcancel("確認", "続行しますか？")
        if result:
            self.result_label.config(text="結果: 「OK」が選択されました")
        else:
            self.result_label.config(text="結果: 「キャンセル」が選択されました")
    
    def show_yesnocancel(self):
        result = messagebox.askyesnocancel("保存確認", "変更を保存しますか？")
        if result is True:
            self.result_label.config(text="結果: 「はい」が選択されました")
        elif result is False:
            self.result_label.config(text="結果: 「いいえ」が選択されました")
        else:  # None
            self.result_label.config(text="結果: 「キャンセル」が選択されました")

if __name__ == "__main__":
    app = MessageboxApp()
    app.mainloop() 