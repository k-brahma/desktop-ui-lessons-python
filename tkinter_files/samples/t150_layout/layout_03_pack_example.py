"""
tkinter Packレイアウトの実用的な例
"""
import tkinter as tk
from tkinter import messagebox


class PackLayoutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pack レイアウトの実用例")
        self.geometry("800x600")
        
        self.create_widgets()
    
    def create_widgets(self):
        # ヘッダー（上部固定）
        self.create_header()
        
        # フッター（下部固定）
        self.create_footer()
        
        # メインコンテナ（中央の残りスペース）
        main_container = tk.Frame(self, bg="lightgray")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # サイドバー（左側固定幅）
        self.create_sidebar(main_container)
        
        # メインコンテンツエリア（右側の残りスペース）
        self.create_main_content(main_container)
    
    def create_header(self):
        # ヘッダーフレーム
        header_frame = tk.Frame(self, bg="darkblue", height=60)
        header_frame.pack(side=tk.TOP, fill=tk.X)
        header_frame.pack_propagate(False)  # 高さを固定
        
        # ロゴ
        logo_label = tk.Label(
            header_frame, 
            text="📊 アプリケーション", 
            bg="darkblue", 
            fg="white", 
            font=("Arial", 16, "bold")
        )
        logo_label.pack(side=tk.LEFT, padx=20, pady=15)
        
        # ナビゲーションボタン
        nav_frame = tk.Frame(header_frame, bg="darkblue")
        nav_frame.pack(side=tk.RIGHT, padx=20, pady=15)
        
        nav_buttons = ["ホーム", "データ", "レポート", "設定"]
        for btn_text in nav_buttons:
            btn = tk.Button(
                nav_frame, 
                text=btn_text, 
                bg="lightblue", 
                fg="darkblue",
                font=("Arial", 10, "bold"),
                width=8,
                command=lambda t=btn_text: self.nav_clicked(t)
            )
            btn.pack(side=tk.LEFT, padx=2)
    
    def create_footer(self):
        # フッターフレーム
        footer_frame = tk.Frame(self, bg="gray", height=30)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        footer_frame.pack_propagate(False)
        
        # ステータス表示
        status_label = tk.Label(
            footer_frame, 
            text="準備完了 | 最終更新: 2024-01-01 12:00:00", 
            bg="gray", 
            fg="white",
            font=("Arial", 9)
        )
        status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # 右側の情報
        info_label = tk.Label(
            footer_frame, 
            text="バージョン 1.0.0", 
            bg="gray", 
            fg="white",
            font=("Arial", 9)
        )
        info_label.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def create_sidebar(self, parent):
        # サイドバーフレーム
        sidebar_frame = tk.Frame(parent, bg="lightgray", width=200)
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        sidebar_frame.pack_propagate(False)  # 幅を固定
        
        # サイドバータイトル
        sidebar_title = tk.Label(
            sidebar_frame, 
            text="メニュー", 
            bg="lightgray", 
            font=("Arial", 14, "bold")
        )
        sidebar_title.pack(pady=10)
        
        # メニューボタン
        menu_items = [
            "📈 売上データ",
            "📊 顧客分析", 
            "📋 在庫管理",
            "👥 従業員管理",
            "⚙️ システム設定",
            "📄 レポート出力",
            "💾 データバックアップ",
            "❓ ヘルプ"
        ]
        
        for item in menu_items:
            btn = tk.Button(
                sidebar_frame,
                text=item,
                bg="white",
                anchor="w",
                width=25,
                padx=10,
                command=lambda t=item: self.menu_clicked(t)
            )
            btn.pack(fill=tk.X, padx=10, pady=2)
    
    def create_main_content(self, parent):
        # メインコンテンツフレーム
        content_frame = tk.Frame(parent, bg="white")
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # タイトル
        content_title = tk.Label(
            content_frame, 
            text="ダッシュボード", 
            bg="white", 
            font=("Arial", 20, "bold")
        )
        content_title.pack(pady=20)
        
        # コンテンツエリア
        self.content_text = tk.Text(
            content_frame, 
            bg="white", 
            font=("Arial", 12),
            wrap=tk.WORD,
            padx=20,
            pady=20
        )
        self.content_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 初期コンテンツ
        initial_content = """
ようこそ、業務管理システムへ！

このシステムでは以下の機能をご利用いただけます：

• 売上データの閲覧・分析
• 顧客情報の管理
• 在庫状況の確認
• 従業員情報の管理
• レポートの生成と出力

左側のメニューから機能を選択してください。
        """
        self.content_text.insert(tk.END, initial_content.strip())
        self.content_text.config(state=tk.DISABLED)  # 読み取り専用
    
    def nav_clicked(self, nav_item):
        messagebox.showinfo("ナビゲーション", f"「{nav_item}」が選択されました。")
    
    def menu_clicked(self, menu_item):
        # メインコンテンツを更新
        self.content_text.config(state=tk.NORMAL)
        self.content_text.delete(1.0, tk.END)
        
        content_map = {
            "📈 売上データ": "売上データの表示画面\n\n今月の売上: ¥1,250,000\n前月比: +15%",
            "📊 顧客分析": "顧客分析画面\n\n総顧客数: 1,456名\n新規顧客: 23名（今月）",
            "📋 在庫管理": "在庫管理画面\n\n総商品数: 342点\n在庫切れ: 5点",
            "👥 従業員管理": "従業員管理画面\n\n在籍者数: 25名\n出勤率: 96%",
            "⚙️ システム設定": "システム設定画面\n\n各種設定を変更できます。",
            "📄 レポート出力": "レポート出力画面\n\n各種レポートを生成・出力できます。",
            "💾 データバックアップ": "データバックアップ画面\n\nデータのバックアップ・復元ができます。",
            "❓ ヘルプ": "ヘルプ画面\n\nシステムの使用方法を確認できます。"
        }
        
        content = content_map.get(menu_item, f"「{menu_item}」の画面")
        self.content_text.insert(tk.END, content)
        self.content_text.config(state=tk.DISABLED)
        
        messagebox.showinfo("メニュー選択", f"「{menu_item}」を表示しました。")

if __name__ == "__main__":
    app = PackLayoutApp()
    app.mainloop() 