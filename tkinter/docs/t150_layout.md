# Layout Manager リファレンス

ウィジェットの配置を管理する `pack`, `grid`, `place` のレイアウトマネージャーについての詳細なリファレンスです。

## 概要

tkinter では、ウィジェットをウィンドウ内に配置するために3つのレイアウトマネージャーが提供されています。それぞれ異なる配置方法と用途があり、適切な選択により効率的で美しいUIを作成できます。

## Pack レイアウトマネージャー

### 概要

`pack` は最もシンプルなレイアウトマネージャーで、ウィジェットを一方向（上下または左右）に順番に配置します。

### 基本的な使用方法

```python
import tkinter as tk

app = tk.Tk()
app.title("Pack レイアウトの例")
app.geometry("300x200")

# 上から順番に配置
tk.Label(app, text="上部ラベル", bg="lightblue").pack(side=tk.TOP)
tk.Label(app, text="下部ラベル", bg="lightgreen").pack(side=tk.BOTTOM)
tk.Label(app, text="左側ラベル", bg="lightcoral").pack(side=tk.LEFT)
tk.Label(app, text="右側ラベル", bg="lightyellow").pack(side=tk.RIGHT)

app.mainloop()
```

### クラスベースでのPack使用

```python
import tkinter as tk

class PackApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pack レイアウトの例（クラスベース）")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # ヘッダー
        header = tk.Label(self, text="ヘッダー", bg="darkblue", fg="white", height=2)
        header.pack(side=tk.TOP, fill=tk.X)
        
        # フッター
        footer = tk.Label(self, text="フッター", bg="darkgray", fg="white", height=2)
        footer.pack(side=tk.BOTTOM, fill=tk.X)
        
        # サイドバー
        sidebar = tk.Label(self, text="サイドバー", bg="lightgray", width=15)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # メインコンテンツ
        main_content = tk.Label(self, text="メインコンテンツ", bg="white")
        main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = PackApp()
    app.mainloop()
```

### Pack の主要オプション

| オプション | 説明 |
| --- | --- |
| `side` | 配置する方向 (`tk.TOP`, `tk.BOTTOM`, `tk.LEFT`, `tk.RIGHT`)。デフォルトは `tk.TOP`。 |
| `fill` | ウィジェットがスペースを埋める方向 (`tk.X`, `tk.Y`, `tk.BOTH`)。 |
| `expand` | 親ウィンドウのサイズ変更時にウィジェットが拡張するかどうか (`True` / `False`)。 |
| `padx`, `pady` | ウィジェット周辺の余白をピクセルで指定。 |
| `ipadx`, `ipady` | ウィジェット内部の余白をピクセルで指定。 |
| `anchor` | ウィジェットの配置位置 (`n`, `s`, `e`, `w`, `center` など)。 |

## Grid レイアウトマネージャー

### 概要

`grid` は表形式でウィジェットを配置するレイアウトマネージャーで、最も柔軟で強力な配置が可能です。

### 基本的な使用方法

```python
import tkinter as tk

app = tk.Tk()
app.title("Grid レイアウトの例")
app.geometry("300x200")

# 2x2のグリッドに配置
tk.Label(app, text="(0,0)", bg="lightblue").grid(row=0, column=0)
tk.Label(app, text="(0,1)", bg="lightgreen").grid(row=0, column=1)
tk.Label(app, text="(1,0)", bg="lightcoral").grid(row=1, column=0)
tk.Label(app, text="(1,1)", bg="lightyellow").grid(row=1, column=1)

app.mainloop()
```

### クラスベースでのGrid使用

```python
import tkinter as tk

class GridApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Grid レイアウトの例（クラスベース）")
        self.geometry("400x300")
        
        self.create_widgets()
        self.configure_grid()
    
    def create_widgets(self):
        # ヘッダー（複数列にわたって配置）
        tk.Label(self, text="アプリケーションタイトル", bg="darkblue", fg="white", font=("Arial", 14)).grid(
            row=0, column=0, columnspan=3, sticky="ew", pady=5
        )
        
        # ラベル
        tk.Label(self, text="名前:", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(self, text="メール:", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Label(self, text="メッセージ:", font=("Arial", 10)).grid(row=3, column=0, sticky="ne", padx=5, pady=5)
        
        # 入力フィールド
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
        
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
        
        self.message_text = tk.Text(self, width=30, height=5)
        self.message_text.grid(row=3, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # ボタン
        tk.Button(self, text="送信", bg="green", fg="white").grid(row=4, column=1, sticky="e", padx=5, pady=10)
        tk.Button(self, text="クリア", bg="red", fg="white").grid(row=4, column=2, sticky="w", padx=5, pady=10)
    
    def configure_grid(self):
        # 列の重みを設定（リサイズ時の動作）
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        # 行の重みを設定
        self.grid_rowconfigure(3, weight=1)

if __name__ == "__main__":
    app = GridApp()
    app.mainloop()
```

### Grid の主要オプション

| オプション | 説明 |
| --- | --- |
| `row`, `column` | ウィジェットを配置するグリッドの行・列番号（0から開始）。 |
| `rowspan`, `columnspan` | ウィジェットが占める行・列の数。 |
| `sticky` | セル内でのウィジェットの配置 (`n`, `s`, `e`, `w` の組み合わせ)。 |
| `padx`, `pady` | ウィジェット周辺の余白をピクセルで指定。 |
| `ipadx`, `ipady` | ウィジェット内部の余白をピクセルで指定。 |

### Grid の重み設定

| メソッド | 説明 |
| --- | --- |
| `grid_rowconfigure(index, weight=N)` | 指定行の重みを設定。ウィンドウリサイズ時の拡張率を決定。 |
| `grid_columnconfigure(index, weight=N)` | 指定列の重みを設定。ウィンドウリサイズ時の拡張率を決定。 |

## Place レイアウトマネージャー

### 概要

`place` は絶対座標や相対座標でウィジェットを配置するレイアウトマネージャーです。

### 基本的な使用方法

```python
import tkinter as tk

app = tk.Tk()
app.title("Place レイアウトの例")
app.geometry("400x300")

# 絶対座標で配置
tk.Label(app, text="絶対座標", bg="lightblue").place(x=50, y=50)

# 相対座標で配置
tk.Label(app, text="中央", bg="lightgreen").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 右下に配置
tk.Label(app, text="右下", bg="lightcoral").place(relx=1.0, rely=1.0, anchor=tk.SE)

app.mainloop()
```

### クラスベースでのPlace使用

```python
import tkinter as tk

class PlaceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Place レイアウトの例（クラスベース）")
        self.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        # 背景画像の代わりとしてキャンバス
        self.canvas = tk.Canvas(self, bg="lightsteelblue")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # タイトル（上部中央）
        title_label = tk.Label(self, text="Place レイアウト デモ", font=("Arial", 18, "bold"), bg="white")
        title_label.place(relx=0.5, y=20, anchor=tk.N)
        
        # ログインフォーム（中央）
        form_frame = tk.Frame(self, bg="white", relief=tk.RAISED, bd=2)
        form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=200)
        
        tk.Label(form_frame, text="ユーザー名:", bg="white").place(x=20, y=40)
        username_entry = tk.Entry(form_frame, width=25)
        username_entry.place(x=100, y=40)
        
        tk.Label(form_frame, text="パスワード:", bg="white").place(x=20, y=80)
        password_entry = tk.Entry(form_frame, width=25, show="*")
        password_entry.place(x=100, y=80)
        
        login_button = tk.Button(form_frame, text="ログイン", bg="blue", fg="white")
        login_button.place(x=100, y=120)
        
        cancel_button = tk.Button(form_frame, text="キャンセル")
        cancel_button.place(x=180, y=120)
        
        # ステータス（下部）
        status_label = tk.Label(self, text="ログインしてください", bg="yellow")
        status_label.place(relx=0.5, rely=1.0, anchor=tk.S, y=-10)
        
        # バージョン情報（右下）
        version_label = tk.Label(self, text="v1.0", font=("Arial", 8), fg="gray")
        version_label.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-5, y=-5)

if __name__ == "__main__":
    app = PlaceApp()
    app.mainloop()
```

### Place の主要オプション

| オプション | 説明 |
| --- | --- |
| `x`, `y` | 絶対座標での位置をピクセルで指定。 |
| `relx`, `rely` | 相対座標での位置を0.0〜1.0の範囲で指定。 |
| `width`, `height` | ウィジェットのサイズをピクセルで指定。 |
| `relwidth`, `relheight` | ウィジェットのサイズを親ウィンドウに対する比率（0.0〜1.0）で指定。 |
| `anchor` | ウィジェットのアンカーポイント (`n`, `s`, `e`, `w`, `center` など)。 |

## 実用的な例

### 複合レイアウトアプリケーション

```python
import tkinter as tk
from tkinter import ttk

class ComplexLayoutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("複合レイアウト デモ")
        self.geometry("800x600")
        
        self.create_layout()
    
    def create_layout(self):
        # メインコンテナ（Grid使用）
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # ヘッダー（Pack使用）
        self.create_header()
        
        # サイドバー（Grid + Pack使用）
        self.create_sidebar()
        
        # メインコンテンツエリア（Grid + Place使用）
        self.create_main_content()
        
        # ステータスバー（Pack使用）
        self.create_status_bar()
    
    def create_header(self):
        header_frame = tk.Frame(self, bg="darkblue", height=60)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        header_frame.grid_propagate(False)
        
        # ヘッダー内でPackを使用
        tk.Label(header_frame, text="複合レイアウト アプリケーション", 
                bg="darkblue", fg="white", font=("Arial", 16, "bold")).pack(side=tk.LEFT, padx=20, pady=15)
        
        # ヘッダーボタン
        button_frame = tk.Frame(header_frame, bg="darkblue")
        button_frame.pack(side=tk.RIGHT, padx=20, pady=15)
        
        tk.Button(button_frame, text="設定", width=8).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="ヘルプ", width=8).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="終了", width=8, bg="red", fg="white").pack(side=tk.LEFT, padx=2)
    
    def create_sidebar(self):
        sidebar_frame = tk.Frame(self, bg="lightgray", width=200)
        sidebar_frame.grid(row=1, column=0, sticky="ns")
        sidebar_frame.grid_propagate(False)
        
        # サイドバー内でPackを使用
        tk.Label(sidebar_frame, text="ナビゲーション", bg="gray", fg="white", 
                font=("Arial", 12, "bold")).pack(fill=tk.X, pady=(0, 10))
        
        # メニュー項目
        menu_items = ["ダッシュボード", "データ", "レポート", "設定", "ユーザー管理"]
        
        for item in menu_items:
            btn = tk.Button(sidebar_frame, text=item, width=20, anchor=tk.W)
            btn.pack(fill=tk.X, padx=10, pady=2)
        
        # サイドバー下部
        tk.Label(sidebar_frame, text="ステータス", bg="lightgray").pack(side=tk.BOTTOM, pady=10)
    
    def create_main_content(self):
        main_frame = tk.Frame(self, bg="white")
        main_frame.grid(row=1, column=1, sticky="nsew")
        
        # メインコンテンツをさらにGridで分割
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        
        # ツールバー（Pack使用）
        toolbar_frame = tk.Frame(main_frame, bg="lightsteelblue", height=40)
        toolbar_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        toolbar_frame.grid_propagate(False)
        
        tk.Button(toolbar_frame, text="新規").pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar_frame, text="開く").pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar_frame, text="保存").pack(side=tk.LEFT, padx=5, pady=5)
        
        # 左パネル（データ表示）
        left_panel = tk.Frame(main_frame, bg="white", relief=tk.SUNKEN, bd=1)
        left_panel.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        tk.Label(left_panel, text="データビュー", font=("Arial", 12, "bold")).pack(pady=10)
        
        # Treeview for data display
        tree = ttk.Treeview(left_panel, columns=("col1", "col2"), show="tree headings")
        tree.heading("#0", text="ID")
        tree.heading("col1", text="名前")
        tree.heading("col2", text="値")
        
        # サンプルデータ
        for i in range(10):
            tree.insert("", "end", text=str(i), values=(f"項目{i}", f"値{i}"))
        
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 右パネル（詳細表示）
        right_panel = tk.Frame(main_frame, bg="white", relief=tk.SUNKEN, bd=1)
        right_panel.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        
        tk.Label(right_panel, text="詳細ビュー", font=("Arial", 12, "bold")).pack(pady=10)
        
        # 詳細フォーム（Gridを使用）
        detail_frame = tk.Frame(right_panel, bg="white")
        detail_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for i, label in enumerate(["名前:", "タイプ:", "値:", "説明:"]):
            tk.Label(detail_frame, text=label, bg="white").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            if label == "説明:":
                tk.Text(detail_frame, height=3, width=25).grid(row=i, column=1, padx=5, pady=5)
            else:
                tk.Entry(detail_frame, width=25).grid(row=i, column=1, padx=5, pady=5)
        
        # ボタンフレーム（Pack使用）
        button_frame = tk.Frame(right_panel, bg="white")
        button_frame.pack(side=tk.BOTTOM, pady=10)
        
        tk.Button(button_frame, text="更新", bg="green", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="削除", bg="red", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="リセット").pack(side=tk.LEFT, padx=5)
        
        # フローティングボタン（Place使用）
        floating_btn = tk.Button(main_frame, text="+", font=("Arial", 20, "bold"), 
                                bg="blue", fg="white", width=3, height=1)
        floating_btn.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-20, y=-20)
    
    def create_status_bar(self):
        status_frame = tk.Frame(self, bg="lightgray", height=25)
        status_frame.grid(row=2, column=0, columnspan=2, sticky="ew")
        status_frame.grid_propagate(False)
        
        # ステータス情報（Pack使用）
        tk.Label(status_frame, text="準備完了", bg="lightgray").pack(side=tk.LEFT, padx=10)
        tk.Label(status_frame, text="行: 1, 列: 1", bg="lightgray").pack(side=tk.RIGHT, padx=10)
        
        # プログレスバー
        progress = ttk.Progressbar(status_frame, length=100, mode='indeterminate')
        progress.pack(side=tk.RIGHT, padx=10)

if __name__ == "__main__":
    app = ComplexLayoutApp()
    app.mainloop()
```

## レイアウトマネージャーの選択指針

| 用途 | 推奨レイアウト | 理由 |
| --- | --- | --- |
| **シンプルな一方向配置** | Pack | 実装が簡単で、ツールバーやボタンの配置に適している |
| **フォーム・表形式** | Grid | 正確な位置制御が可能で、複雑なレイアウトに対応 |
| **重複配置・絶対位置指定** | Place | 絶対座標での配置や、ウィジェットの重ね合わせが可能 |
| **複合レイアウト** | 組み合わせ | 各部分に最適なレイアウトマネージャーを使い分ける |

## ベストプラクティス

| プラクティス | 説明 |
| --- | --- |
| **一つのコンテナに一つのマネージャー** | 同じ親ウィンドウ内では一つのレイアウトマネージャーのみを使用します。 |
| **Frameで分割** | 複雑なレイアウトはFrameで区分けし、それぞれに適切なマネージャーを使用します。 |
| **Grid の重み設定** | Gridを使用する場合は、`grid_rowconfigure` と `grid_columnconfigure` で適切な重みを設定します。 |
| **レスポンシブデザイン** | `fill` と `expand` オプションを適切に使用してウィンドウリサイズに対応します。 |
| **一貫性の保持** | 同じアプリケーション内では一貫したレイアウト手法を使用します。 |

## 参考リンク

- [Python Docs - tkinter Layout Management](https://docs.python.org/3/library/tkinter.html#layout-management)
- [TkDocs - Layout Management](https://tkdocs.com/tutorial/grid.html) 