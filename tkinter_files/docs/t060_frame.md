# Frame リファレンス

ウィジェットをグループ化し、レイアウトを整理するための `Frame` ウィジェットについての詳細なリファレンスです。

## 概要

`Frame` ウィジェットは、他のウィジェットを格納するためのコンテナです。ウィジェットをグループ化して整理したり、複雑なレイアウトを構築したりするために使用されます。Frame 自体は視覚的な要素を持ちませんが、境界線や背景色を設定して表示することも可能です。

## 基本的な使用方法

### シンプルなフレームの作成

```python
import tkinter as tk

app = tk.Tk()
app.title("Frameの例")
app.geometry("400x300")

# メインフレーム
main_frame = tk.Frame(app, bg="lightblue", relief=tk.RAISED, bd=2)
main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# フレーム内にウィジェットを配置
label = tk.Label(main_frame, text="フレーム内のラベル", bg="lightblue")
label.pack(pady=10)

button = tk.Button(main_frame, text="フレーム内のボタン")
button.pack(pady=5)

app.mainloop()
```

### クラスベースでのフレーム作成

```python
import tkinter as tk

class FrameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Frameの例（クラスベース）")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # メインフレーム
        self.main_frame = tk.Frame(self, bg="lightblue", relief=tk.RAISED, bd=2)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # フレーム内にウィジェットを配置
        self.label = tk.Label(self.main_frame, text="フレーム内のラベル", bg="lightblue")
        self.label.pack(pady=10)
        
        self.button = tk.Button(self.main_frame, text="フレーム内のボタン")
        self.button.pack(pady=5)

if __name__ == "__main__":
    app = FrameApp()
    app.mainloop()
```

## 主要なオプション

| オプション | 説明 |
| --- | --- |
| `width` | フレームの幅をピクセル単位で指定します。 |
| `height` | フレームの高さをピクセル単位で指定します。 |
| `bg` (または `background`) | フレームの背景色。 |
| `relief` | 境界線のスタイル (`flat`, `raised`, `sunken`, `groove`, `ridge`)。 |
| `borderwidth` (または `bd`) | 境界線の幅。 |
| `padx`, `pady` | フレーム内のコンテンツと境界線の間の水平・垂直方向の余白。 |
| `cursor` | フレーム上でのマウスカーソルの形状。 |

## レイアウトマネージャーとの組み合わせ

Frame は `pack()`, `grid()`, `place()` のすべてのレイアウトマネージャーと組み合わせて使用できます。

| マネージャー | 説明 |
| --- | --- |
| `pack()` | 上下左右に順次配置。シンプルなレイアウトに適している。 |
| `grid()` | 格子状の配置。表形式のレイアウトに適している。 |
| `place()` | 絶対座標での配置。精密な位置制御が可能。 |

## 実用的な例

### 複数のセクションを持つアプリケーション

```python
import tkinter as tk
from tkinter import ttk

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
```

### フォームレイアウト（grid使用）

```python
import tkinter as tk
from tkinter import messagebox

class FormLayout(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("フォームレイアウト")
        self.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        # メインフレーム
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # タイトル
        title_label = tk.Label(main_frame, text="ユーザー情報入力", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # 個人情報セクション
        personal_frame = tk.LabelFrame(main_frame, text="個人情報", font=("Arial", 12, "bold"), padx=10, pady=10)
        personal_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        
        # 個人情報フィールド
        tk.Label(personal_frame, text="氏名:").grid(row=0, column=0, sticky="e", padx=(0, 10), pady=5)
        self.name_entry = tk.Entry(personal_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(personal_frame, text="年齢:").grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.age_entry = tk.Entry(personal_frame, width=30)
        self.age_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(personal_frame, text="メールアドレス:").grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
        self.email_entry = tk.Entry(personal_frame, width=30)
        self.email_entry.grid(row=2, column=1, pady=5)
        
        # 連絡先セクション
        contact_frame = tk.LabelFrame(main_frame, text="連絡先", font=("Arial", 12, "bold"), padx=10, pady=10)
        contact_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        
        # 連絡先フィールド
        tk.Label(contact_frame, text="電話番号:").grid(row=0, column=0, sticky="e", padx=(0, 10), pady=5)
        self.phone_entry = tk.Entry(contact_frame, width=30)
        self.phone_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(contact_frame, text="住所:").grid(row=1, column=0, sticky="ne", padx=(0, 10), pady=5)
        self.address_text = tk.Text(contact_frame, width=30, height=3)
        self.address_text.grid(row=1, column=1, pady=5)
        
        # 設定セクション
        settings_frame = tk.LabelFrame(main_frame, text="設定", font=("Arial", 12, "bold"), padx=10, pady=10)
        settings_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        
        # チェックボックス
        self.newsletter_var = tk.BooleanVar()
        newsletter_check = tk.Checkbutton(settings_frame, text="ニュースレターを受け取る", variable=self.newsletter_var)
        newsletter_check.grid(row=0, column=0, sticky="w", pady=2)
        
        self.notifications_var = tk.BooleanVar()
        notifications_check = tk.Checkbutton(settings_frame, text="通知を受け取る", variable=self.notifications_var)
        notifications_check.grid(row=1, column=0, sticky="w", pady=2)
        
        # ボタンフレーム
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2)
        
        submit_button = tk.Button(button_frame, text="送信", command=self.submit_form, bg="lightblue")
        submit_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(button_frame, text="クリア", command=self.clear_form, bg="lightcoral")
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # グリッドの重みを設定
        main_frame.columnconfigure(1, weight=1)
    
    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_text.get("1.0", tk.END).strip()
        newsletter = self.newsletter_var.get()
        notifications = self.notifications_var.get()
        
        if not name:
            messagebox.showerror("エラー", "氏名を入力してください")
            return
        
        result = f"氏名: {name}\n年齢: {age}\nメール: {email}\n電話: {phone}\n住所: {address}\n"
        result += f"ニュースレター: {'はい' if newsletter else 'いいえ'}\n"
        result += f"通知: {'はい' if notifications else 'いいえ'}"
        
        messagebox.showinfo("送信完了", result)
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_text.delete("1.0", tk.END)
        self.newsletter_var.set(False)
        self.notifications_var.set(False)

if __name__ == "__main__":
    app = FormLayout()
    app.mainloop()
```

## ベストプラクティス

| プラクティス | 説明 |
| --- | --- |
| **論理的なグループ化** | 関連するウィジェットをFrame でグループ化して、UI の構造を明確にします。 |
| **`LabelFrame` の活用** | タイトル付きのセクションには `LabelFrame` を使用します。 |
| **`pack_propagate()` の理解** | フレームの固定サイズを維持したい場合は `pack_propagate(False)` を使用します。 |
| **レイアウトマネージャーの統一** | 一つの親ウィジェット内では同一のレイアウトマネージャー（pack、grid、place）を使用します。 |
| **入れ子構造の活用** | 複雑なレイアウトは Frame を入れ子にして構築します。 |

## 参考リンク

- [Python Docs - tkinter.Frame](https://docs.python.org/3/library/tkinter.html#frame)
- [TkDocs - Frame](https://tkdocs.com/tutorial/widgets.html#frame) 