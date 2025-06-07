"""
tkinter セクション分けアプリケーション
"""
import tkinter as tk


class SectionedApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("セクション分けアプリケーション")
        self.geometry("600x500")
        
        self.create_widgets()
    
    def create_widgets(self):
        # ヘッダーフレーム
        header_frame = tk.Frame(self, bg="darkblue", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)  # 固定サイズを維持
        
        title_label = tk.Label(
            header_frame, 
            text="アプリケーションタイトル", 
            bg="darkblue", 
            fg="white",
            font=("Arial", 16, "bold")
        )
        title_label.pack(expand=True)
        
        # メインコンテンツエリア
        content_frame = tk.Frame(self)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 左サイドバー
        sidebar_frame = tk.Frame(content_frame, bg="lightgray", width=200, relief=tk.SUNKEN, bd=1)
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        sidebar_frame.pack_propagate(False)
        
        tk.Label(sidebar_frame, text="サイドバー", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=10)
        
        # サイドバーのボタン
        for i in range(5):
            btn = tk.Button(sidebar_frame, text=f"メニュー {i+1}", command=lambda x=i: self.menu_clicked(x+1))
            btn.pack(fill=tk.X, padx=10, pady=2)
        
        # メインコンテンツエリア
        main_content_frame = tk.Frame(content_frame, bg="white", relief=tk.SUNKEN, bd=1)
        main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # メインコンテンツ
        self.content_label = tk.Label(
            main_content_frame, 
            text="メインコンテンツエリア\nメニューを選択してください", 
            bg="white",
            font=("Arial", 14),
            justify=tk.CENTER
        )
        self.content_label.pack(expand=True)
        
        # フッターフレーム
        footer_frame = tk.Frame(self, bg="gray", height=40)
        footer_frame.pack(fill=tk.X)
        footer_frame.pack_propagate(False)
        
        status_label = tk.Label(
            footer_frame, 
            text="ステータス: 準備完了", 
            bg="gray", 
            fg="white"
        )
        status_label.pack(side=tk.LEFT, padx=10, expand=True, anchor=tk.W)
    
    def menu_clicked(self, menu_num):
        self.content_label.config(text=f"メニュー {menu_num} が選択されました\n\nここにコンテンツが表示されます")

if __name__ == "__main__":
    app = SectionedApp()
    app.mainloop() 