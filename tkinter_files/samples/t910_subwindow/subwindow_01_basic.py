"""
tkinter 基本的なサブウィンドウ
"""
import tkinter as tk
from tkinter import messagebox


class BasicSubWindowApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("基本的なサブウィンドウ")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # タイトル
        title_label = tk.Label(self, text="メインウィンドウ", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        # 説明
        info_label = tk.Label(
            self, 
            text="ボタンをクリックして、各種サブウィンドウを開いてください。", 
            font=("Arial", 11)
        )
        info_label.pack(pady=10)
        
        # ボタンフレーム
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        # 各種サブウィンドウボタン
        tk.Button(
            button_frame, 
            text="情報ウィンドウを開く", 
            command=self.open_info_window,
            bg="lightblue",
            width=20,
            height=2
        ).pack(pady=5)
        
        tk.Button(
            button_frame, 
            text="設定ウィンドウを開く", 
            command=self.open_settings_window,
            bg="lightgreen",
            width=20,
            height=2
        ).pack(pady=5)
        
        tk.Button(
            button_frame, 
            text="ヘルプウィンドウを開く", 
            command=self.open_help_window,
            bg="lightyellow",
            width=20,
            height=2
        ).pack(pady=5)
        
        # カウンター
        self.window_counter = 0
        self.counter_label = tk.Label(self, text="開いたウィンドウ数: 0", font=("Arial", 10))
        self.counter_label.pack(pady=20)
    
    def open_info_window(self):
        # 情報表示用のサブウィンドウ
        info_window = tk.Toplevel(self)
        info_window.title("アプリケーション情報")
        info_window.geometry("350x250")
        info_window.resizable(False, False)
        
        # 中央に配置
        self.center_window(info_window, 350, 250)
        
        # アイコン風の装飾
        header_frame = tk.Frame(info_window, bg="darkblue", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame, 
            text="ℹ️ アプリケーション情報", 
            bg="darkblue", 
            fg="white", 
            font=("Arial", 14, "bold")
        ).pack(pady=15)
        
        # 情報内容
        content_frame = tk.Frame(info_window, padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        info_text = """
アプリケーション名: サブウィンドウデモ
バージョン: 1.0.0
開発者: Python学習者
作成日: 2024年

このアプリケーションはtkinterのサブウィンドウ
機能をデモンストレーションします。
        """
        
        tk.Label(content_frame, text=info_text.strip(), justify=tk.LEFT, font=("Arial", 10)).pack()
        
        # 閉じるボタン
        tk.Button(
            content_frame, 
            text="閉じる", 
            command=info_window.destroy,
            bg="gray",
            fg="white",
            width=10
        ).pack(pady=10)
        
        self.update_counter()
    
    def open_settings_window(self):
        # 設定用のサブウィンドウ
        settings_window = tk.Toplevel(self)
        settings_window.title("設定")
        settings_window.geometry("400x300")
        
        # 中央に配置
        self.center_window(settings_window, 400, 300)
        
        # ヘッダー
        header_frame = tk.Frame(settings_window, bg="darkgreen", height=50)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame, 
            text="⚙️ アプリケーション設定", 
            bg="darkgreen", 
            fg="white", 
            font=("Arial", 12, "bold")
        ).pack(pady=12)
        
        # 設定内容
        content_frame = tk.Frame(settings_window, padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # 一般設定
        general_frame = tk.LabelFrame(content_frame, text="一般設定", font=("Arial", 11, "bold"))
        general_frame.pack(fill=tk.X, pady=10)
        
        tk.Checkbutton(general_frame, text="起動時にヒントを表示", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)
        tk.Checkbutton(general_frame, text="自動保存を有効にする", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)
        tk.Checkbutton(general_frame, text="音声通知を有効にする", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)
        
        # 表示設定
        display_frame = tk.LabelFrame(content_frame, text="表示設定", font=("Arial", 11, "bold"))
        display_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(display_frame, text="テーマ:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        theme_var = tk.StringVar(value="ライト")
        tk.OptionMenu(display_frame, theme_var, "ライト", "ダーク", "自動").grid(row=0, column=1, sticky="w", padx=10, pady=5)
        
        tk.Label(display_frame, text="フォントサイズ:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        font_var = tk.StringVar(value="中")
        tk.OptionMenu(display_frame, font_var, "小", "中", "大").grid(row=1, column=1, sticky="w", padx=10, pady=5)
        
        # ボタン
        button_frame = tk.Frame(content_frame)
        button_frame.pack(pady=20)
        
        tk.Button(
            button_frame, 
            text="保存", 
            command=lambda: [messagebox.showinfo("設定", "設定を保存しました。"), settings_window.destroy()],
            bg="green",
            fg="white",
            width=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, 
            text="キャンセル", 
            command=settings_window.destroy,
            bg="gray",
            fg="white",
            width=8
        ).pack(side=tk.LEFT, padx=5)
        
        self.update_counter()
    
    def open_help_window(self):
        # ヘルプ用のサブウィンドウ
        help_window = tk.Toplevel(self)
        help_window.title("ヘルプ")
        help_window.geometry("500x400")
        
        # 中央に配置
        self.center_window(help_window, 500, 400)
        
        # ヘッダー
        header_frame = tk.Frame(help_window, bg="darkorange", height=50)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame, 
            text="❓ ヘルプ", 
            bg="darkorange", 
            fg="white", 
            font=("Arial", 12, "bold")
        ).pack(pady=12)
        
        # ヘルプ内容（スクロール可能）
        content_frame = tk.Frame(help_window)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # スクロールバー付きテキスト
        text_frame = tk.Frame(content_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        help_text = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 10))
        scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=help_text.yview)
        help_text.config(yscrollcommand=scrollbar.set)
        
        help_content = """
サブウィンドウデモ - ヘルプ

【基本的な使い方】

1. メインウィンドウから各種ボタンをクリック
2. サブウィンドウが開きます
3. サブウィンドウで必要な操作を実行
4. 完了したらサブウィンドウを閉じる

【各ウィンドウの説明】

• 情報ウィンドウ
  アプリケーションの基本情報を表示します。

• 設定ウィンドウ
  アプリケーションの設定を変更できます。
  設定は「保存」ボタンで保存されます。

• ヘルプウィンドウ
  このウィンドウです。操作方法や機能について
  説明しています。

【ショートカットキー】

• Ctrl+N: 新しいウィンドウを開く
• Ctrl+W: ウィンドウを閉じる
• F1: ヘルプを開く
• Escape: ダイアログを閉じる

【トラブルシューティング】

Q: ウィンドウが開かない
A: メインウィンドウがアクティブになっているか確認してください。

Q: 設定が保存されない
A: 「保存」ボタンを押してからウィンドウを閉じてください。

Q: 複数のウィンドウを同時に開けない
A: 一部のウィンドウはモーダルダイアログの場合があります。

【更新履歴】

v1.0.0 - 初期リリース
- 基本的なサブウィンドウ機能
- 情報・設定・ヘルプウィンドウの実装
"""
        
        help_text.insert(tk.END, help_content.strip())
        help_text.config(state=tk.DISABLED)  # 編集不可にする
        
        help_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 閉じるボタン
        tk.Button(
            content_frame, 
            text="閉じる", 
            command=help_window.destroy,
            bg="orange",
            fg="white",
            width=10
        ).pack(pady=10)
        
        self.update_counter()
    
    def center_window(self, window, width, height):
        # ウィンドウを画面の中央に配置
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def update_counter(self):
        # ウィンドウカウンターを更新
        self.window_counter += 1
        self.counter_label.config(text=f"開いたウィンドウ数: {self.window_counter}")

if __name__ == "__main__":
    app = BasicSubWindowApp()
    app.mainloop() 