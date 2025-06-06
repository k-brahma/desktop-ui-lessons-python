"""
tkinter 非モーダルウィンドウ
"""
import tkinter as tk
from tkinter import messagebox


class NonModalWindowApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("シンプルな非モーダルウィンドウ")
        self.geometry("300x200")
        
        # ウィンドウ管理用
        self.sub_window = None
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="非モーダルウィンドウテスト", font=("Arial", 14, "bold")).pack(pady=20)
        
        tk.Label(self, text="非モーダル = ウィンドウを開いても\n他の操作ができます", 
                justify=tk.CENTER).pack(pady=10)
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        tk.Button(
            button_frame, 
            text="サブウィンドウを開く", 
            command=self.open_sub_window,
            bg="lightgreen",
            width=18,
            height=2
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, 
            text="サブウィンドウを閉じる", 
            command=self.close_sub_window,
            bg="lightcoral",
            width=18,
            height=2
        ).pack(side=tk.LEFT, padx=5)
        
        # 操作テスト用
        tk.Label(self, text="↓ウィンドウが開いていてもクリックできます").pack()
        tk.Button(self, text="テストボタン", command=lambda: messagebox.showinfo("テスト", "クリックできました！")).pack()
    
    def open_sub_window(self):
        # 重複開防止
        if self.sub_window and self.sub_window.winfo_exists():
            self.sub_window.lift()  # 既存ウィンドウを前面に
            return
        
        # 非モーダルウィンドウを作成
        self.sub_window = SubWindow(self)
    
    def close_sub_window(self):
        if self.sub_window and self.sub_window.winfo_exists():
            self.sub_window.destroy()
        self.sub_window = None

class SubWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.title("サブウィンドウ")
        self.geometry("250x200")
        self.resizable(True, True)
        
        # 非モーダル設定（grab_setを呼ばない）
        self.transient(parent)  # 親に関連付けるが、操作はブロックしない
        
        # 親ウィンドウの右側に配置
        self.position_beside_parent(parent)
        
        self.create_widgets()
        
        # 閉じる処理をカスタマイズ
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_widgets(self):
        tk.Label(self, text="非モーダルウィンドウ", font=("Arial", 12, "bold")).pack(pady=10)
        
        tk.Label(self, text="このウィンドウが開いていても\nメインウィンドウを操作できます", 
                justify=tk.CENTER).pack(pady=10)
        
        # カウンター例
        self.counter = 0
        self.counter_label = tk.Label(self, text=f"カウンター: {self.counter}", font=("Arial", 11))
        self.counter_label.pack(pady=10)
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="カウント+", command=self.increment, 
                 bg="lightblue").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="カウント-", command=self.decrement, 
                 bg="lightyellow").pack(side=tk.LEFT, padx=5)
        
        tk.Button(self, text="閉じる", command=self.on_closing, 
                 bg="gray", fg="white", width=10).pack(pady=10)
    
    def position_beside_parent(self, parent):
        parent.update_idletasks()
        
        # 親ウィンドウの右側に配置
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        
        x = parent_x + parent_width + 10
        y = parent_y
        
        self.geometry(f"250x200+{x}+{y}")
    
    def increment(self):
        self.counter += 1
        self.counter_label.config(text=f"カウンター: {self.counter}")
    
    def decrement(self):
        self.counter -= 1
        self.counter_label.config(text=f"カウンター: {self.counter}")
    
    def on_closing(self):
        # 親のサブウィンドウ参照をクリア
        self.parent.sub_window = None
        self.destroy()

if __name__ == "__main__":
    app = NonModalWindowApp()
    app.mainloop() 