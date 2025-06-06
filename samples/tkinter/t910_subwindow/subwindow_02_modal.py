"""
tkinter モーダルダイアログ
"""
import tkinter as tk
from tkinter import messagebox


class SimpleModalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("シンプルなモーダルダイアログ")
        self.geometry("300x200")
        
        # ダイアログ管理用
        self.current_dialog = None
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="モーダルダイアログテスト", font=("Arial", 14, "bold")).pack(pady=20)
        
        tk.Label(self, text="モーダル = このボタンを押すと\n他の操作ができなくなります", 
                justify=tk.CENTER).pack(pady=10)
        
        self.open_button = tk.Button(
            self, 
            text="モーダルダイアログを開く", 
            command=self.open_modal_dialog,
            bg="lightblue",
            width=20,
            height=2
        )
        self.open_button.pack(pady=20)
        
        # 操作テスト用
        tk.Label(self, text="↓ダイアログが開いている間はクリックできません").pack()
        tk.Button(self, text="テストボタン", command=lambda: messagebox.showinfo("テスト", "クリックできました！")).pack()
    
    def open_modal_dialog(self):
        # 重複開防止
        if self.current_dialog and self.current_dialog.winfo_exists():
            self.current_dialog.lift()  # 既存ダイアログを前面に
            return
        
        # モーダルダイアログを作成
        dialog = SimpleDialog(self)
        self.current_dialog = dialog
        
        # ボタンを無効化（視覚的フィードバック）
        self.open_button.config(state=tk.DISABLED)
        
        # モーダル待機
        self.wait_window(dialog)
        
        # ダイアログが閉じられた後の処理
        self.current_dialog = None
        self.open_button.config(state=tk.NORMAL)
        
        # 結果を確認
        if hasattr(dialog, 'result') and dialog.result:
            messagebox.showinfo("結果", f"入力されたテキスト: {dialog.result}")

class SimpleDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title("モーダルダイアログ")
        self.geometry("250x150")
        self.resizable(False, False)
        
        # モーダルにする重要な設定
        self.transient(parent)  # 親に関連付け
        self.grab_set()         # 他の操作をブロック
        
        # 中央に配置
        self.center_on_parent(parent)
        
        self.result = None
        
        self.create_widgets()
        
        # フォーカス設定
        self.entry.focus_set()
        
        # キーバインド
        self.bind('<Return>', lambda e: self.ok())
        self.bind('<Escape>', lambda e: self.cancel())
    
    def create_widgets(self):
        tk.Label(self, text="何か入力してください:", font=("Arial", 11)).pack(pady=10)
        
        self.entry = tk.Entry(self, width=25, font=("Arial", 11))
        self.entry.pack(pady=5)
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="OK", command=self.ok, 
                 bg="green", fg="white", width=8).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="キャンセル", command=self.cancel, 
                 bg="gray", fg="white", width=8).pack(side=tk.LEFT, padx=5)
    
    def center_on_parent(self, parent):
        parent.update_idletasks()
        
        # 親ウィンドウの中央に配置
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        dialog_width = 250
        dialog_height = 150
        
        x = parent_x + (parent_width - dialog_width) // 2
        y = parent_y + (parent_height - dialog_height) // 2
        
        self.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
    
    def ok(self):
        self.result = self.entry.get()
        self.destroy()
    
    def cancel(self):
        self.result = None
        self.destroy()

if __name__ == "__main__":
    app = SimpleModalApp()
    app.mainloop() 