#!/usr/bin/env python3
"""
ショートカット一覧表示とリアルタイムキーバインディング例
利用可能なショートカットを表示し、リアルタイムで実行状況を表示
"""

import datetime
import tkinter as tk
from tkinter import ttk


class ShortcutDisplayApp:
    def __init__(self, root):
        self.root = root
        root.title("ショートカット一覧とリアルタイム表示")
        root.geometry("800x600")
        
        # ショートカット定義
        self.shortcuts = {
            'F1': {'action': 'ヘルプを表示', 'category': 'ヘルプ'},
            'F2': {'action': 'ファイルの名前変更', 'category': 'ファイル'},
            'F3': {'action': '検索', 'category': '編集'},
            'F4': {'action': 'アドレスバーに移動', 'category': 'ナビゲーション'},
            'F5': {'action': '更新', 'category': 'ページ'},
            'F11': {'action': '全画面切り替え', 'category': '表示'},
            'F12': {'action': '開発者ツール', 'category': '開発'},
            'Ctrl+N': {'action': '新規作成', 'category': 'ファイル'},
            'Ctrl+O': {'action': 'ファイルを開く', 'category': 'ファイル'},
            'Ctrl+S': {'action': '保存', 'category': 'ファイル'},
            'Ctrl+P': {'action': '印刷', 'category': 'ファイル'},
            'Ctrl+Z': {'action': '元に戻す', 'category': '編集'},
            'Ctrl+Y': {'action': 'やり直し', 'category': '編集'},
            'Ctrl+X': {'action': '切り取り', 'category': '編集'},
            'Ctrl+C': {'action': 'コピー', 'category': '編集'},
            'Ctrl+V': {'action': '貼り付け', 'category': '編集'},
            'Ctrl+A': {'action': 'すべて選択', 'category': '編集'},
            'Ctrl+F': {'action': '検索', 'category': '編集'},
            'Ctrl+H': {'action': '置換', 'category': '編集'},
            'Ctrl+G': {'action': '指定行へ移動', 'category': 'ナビゲーション'},
            'Ctrl+L': {'action': 'アドレスバーに移動', 'category': 'ナビゲーション'},
            'Ctrl+T': {'action': '新しいタブ', 'category': 'タブ'},
            'Ctrl+W': {'action': 'タブを閉じる', 'category': 'タブ'},
            'Ctrl+Tab': {'action': '次のタブ', 'category': 'タブ'},
            'Ctrl+Shift+Tab': {'action': '前のタブ', 'category': 'タブ'},
            'Ctrl+Plus': {'action': '拡大', 'category': '表示'},
            'Ctrl+Minus': {'action': '縮小', 'category': '表示'},
            'Ctrl+0': {'action': '標準倍率', 'category': '表示'},
            'Alt+F4': {'action': 'アプリケーション終了', 'category': 'システム'},
            'Alt+Tab': {'action': 'アプリケーション切り替え', 'category': 'システム'},
            'Win+D': {'action': 'デスクトップ表示', 'category': 'システム'},
            'Win+L': {'action': 'ロック画面', 'category': 'システム'},
            'Escape': {'action': 'キャンセル', 'category': 'システム'},
            'Enter': {'action': '実行/確定', 'category': 'システム'},
            'Space': {'action': 'スペース/選択', 'category': 'システム'},
            'Delete': {'action': '削除', 'category': '編集'},
            'Home': {'action': '行の始めに移動', 'category': 'ナビゲーション'},
            'End': {'action': '行の終わりに移動', 'category': 'ナビゲーション'},
            'Page Up': {'action': '前のページ', 'category': 'ナビゲーション'},
            'Page Down': {'action': '次のページ', 'category': 'ナビゲーション'},
        }
        
        # 実行履歴
        self.execution_history = []
        
        # UI作成
        self.create_ui()
        self.setup_keybindings()
        
    def create_ui(self):
        # メインフレーム
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 上部: ショートカット一覧
        upper_frame = tk.LabelFrame(main_frame, text="利用可能なショートカット", font=("Arial", 12, "bold"))
        upper_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # カテゴリフィルター
        filter_frame = tk.Frame(upper_frame)
        filter_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(filter_frame, text="カテゴリフィルター:").pack(side=tk.LEFT)
        
        self.category_var = tk.StringVar(value="すべて")
        categories = ["すべて"] + sorted(set(info['category'] for info in self.shortcuts.values()))
        category_combo = ttk.Combobox(filter_frame, textvariable=self.category_var, 
                                     values=categories, state="readonly", width=15)
        category_combo.pack(side=tk.LEFT, padx=5)
        category_combo.bind("<<ComboboxSelected>>", self.filter_shortcuts)
        
        # 検索フィールド
        tk.Label(filter_frame, text="検索:").pack(side=tk.LEFT, padx=(20, 0))
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(filter_frame, textvariable=self.search_var, width=20)
        search_entry.pack(side=tk.LEFT, padx=5)
        search_entry.bind('<KeyRelease>', self.search_shortcuts)
        
        # ショートカット一覧テーブル
        tree_frame = tk.Frame(upper_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Treeviewウィジェット
        columns = ('shortcut', 'action', 'category')
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=12)
        
        # 列の設定
        self.tree.heading('shortcut', text='ショートカット')
        self.tree.heading('action', text='動作')
        self.tree.heading('category', text='カテゴリ')
        
        self.tree.column('shortcut', width=150, anchor='center')
        self.tree.column('action', width=250)
        self.tree.column('category', width=120, anchor='center')
        
        # スクロールバー
        tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # ショートカット一覧を表示
        self.populate_tree()
        
        # 下部: リアルタイム実行表示
        lower_frame = tk.LabelFrame(main_frame, text="ショートカット実行履歴", font=("Arial", 12, "bold"))
        lower_frame.pack(fill=tk.BOTH, expand=False, pady=(10, 0))
        
        # 現在の状態表示
        status_frame = tk.Frame(lower_frame)
        status_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(status_frame, text="現在の状態:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        self.current_status = tk.Label(status_frame, text="キー入力待ち...", 
                                      fg="blue", font=("Arial", 10))
        self.current_status.pack(side=tk.LEFT, padx=10)
        
        # クリアボタン
        clear_btn = tk.Button(status_frame, text="履歴クリア", command=self.clear_history)
        clear_btn.pack(side=tk.RIGHT)
        
        # 実行履歴リスト
        history_frame = tk.Frame(lower_frame)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.history_listbox = tk.Listbox(history_frame, height=8, font=("Consolas", 9))
        history_scroll = tk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_listbox.yview)
        self.history_listbox.configure(yscrollcommand=history_scroll.set)
        
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        history_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 統計情報
        stats_frame = tk.Frame(lower_frame)
        stats_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.stats_label = tk.Label(stats_frame, text="実行回数: 0回", font=("Arial", 9))
        self.stats_label.pack(side=tk.LEFT)
        
        self.most_used_label = tk.Label(stats_frame, text="", font=("Arial", 9))
        self.most_used_label.pack(side=tk.RIGHT)
        
    def populate_tree(self):
        """ショートカット一覧をツリーに表示"""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        category_filter = self.category_var.get()
        search_text = self.search_var.get().lower()
        
        for shortcut, info in self.shortcuts.items():
            # カテゴリフィルター
            if category_filter != "すべて" and info['category'] != category_filter:
                continue
                
            # 検索フィルター
            if search_text and search_text not in shortcut.lower() and search_text not in info['action'].lower():
                continue
                
            self.tree.insert('', tk.END, values=(shortcut, info['action'], info['category']))
            
    def filter_shortcuts(self, event=None):
        """カテゴリフィルターが変更された時の処理"""
        self.populate_tree()
        
    def search_shortcuts(self, event=None):
        """検索フィールドが変更された時の処理"""
        self.populate_tree()
        
    def setup_keybindings(self):
        """キーバインディングの設定"""
        # 各ショートカットにバインド
        self.root.bind('<F1>', lambda e: self.execute_shortcut('F1'))
        self.root.bind('<F2>', lambda e: self.execute_shortcut('F2'))
        self.root.bind('<F3>', lambda e: self.execute_shortcut('F3'))
        self.root.bind('<F4>', lambda e: self.execute_shortcut('F4'))
        self.root.bind('<F5>', lambda e: self.execute_shortcut('F5'))
        self.root.bind('<F11>', lambda e: self.execute_shortcut('F11'))
        self.root.bind('<F12>', lambda e: self.execute_shortcut('F12'))
        
        self.root.bind('<Control-n>', lambda e: self.execute_shortcut('Ctrl+N'))
        self.root.bind('<Control-o>', lambda e: self.execute_shortcut('Ctrl+O'))
        self.root.bind('<Control-s>', lambda e: self.execute_shortcut('Ctrl+S'))
        self.root.bind('<Control-p>', lambda e: self.execute_shortcut('Ctrl+P'))
        self.root.bind('<Control-z>', lambda e: self.execute_shortcut('Ctrl+Z'))
        self.root.bind('<Control-y>', lambda e: self.execute_shortcut('Ctrl+Y'))
        self.root.bind('<Control-x>', lambda e: self.execute_shortcut('Ctrl+X'))
        self.root.bind('<Control-c>', lambda e: self.execute_shortcut('Ctrl+C'))
        self.root.bind('<Control-v>', lambda e: self.execute_shortcut('Ctrl+V'))
        self.root.bind('<Control-a>', lambda e: self.execute_shortcut('Ctrl+A'))
        self.root.bind('<Control-f>', lambda e: self.execute_shortcut('Ctrl+F'))
        self.root.bind('<Control-h>', lambda e: self.execute_shortcut('Ctrl+H'))
        self.root.bind('<Control-g>', lambda e: self.execute_shortcut('Ctrl+G'))
        self.root.bind('<Control-l>', lambda e: self.execute_shortcut('Ctrl+L'))
        self.root.bind('<Control-t>', lambda e: self.execute_shortcut('Ctrl+T'))
        self.root.bind('<Control-w>', lambda e: self.execute_shortcut('Ctrl+W'))
        self.root.bind('<Control-Tab>', lambda e: self.execute_shortcut('Ctrl+Tab'))
        self.root.bind('<Control-Shift-Tab>', lambda e: self.execute_shortcut('Ctrl+Shift+Tab'))
        self.root.bind('<Control-plus>', lambda e: self.execute_shortcut('Ctrl+Plus'))
        self.root.bind('<Control-minus>', lambda e: self.execute_shortcut('Ctrl+Minus'))
        self.root.bind('<Control-0>', lambda e: self.execute_shortcut('Ctrl+0'))
        
        self.root.bind('<Alt-F4>', lambda e: self.execute_shortcut('Alt+F4'))
        self.root.bind('<Alt-Tab>', lambda e: self.execute_shortcut('Alt+Tab'))
        
        self.root.bind('<Escape>', lambda e: self.execute_shortcut('Escape'))
        self.root.bind('<Return>', lambda e: self.execute_shortcut('Enter'))
        self.root.bind('<space>', lambda e: self.execute_shortcut('Space'))
        self.root.bind('<Delete>', lambda e: self.execute_shortcut('Delete'))
        self.root.bind('<Home>', lambda e: self.execute_shortcut('Home'))
        self.root.bind('<End>', lambda e: self.execute_shortcut('End'))
        self.root.bind('<Prior>', lambda e: self.execute_shortcut('Page Up'))
        self.root.bind('<Next>', lambda e: self.execute_shortcut('Page Down'))
        
    def execute_shortcut(self, shortcut_key):
        """ショートカット実行処理"""
        if shortcut_key in self.shortcuts:
            info = self.shortcuts[shortcut_key]
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            
            # 履歴に追加
            history_entry = f"[{timestamp}] {shortcut_key} → {info['action']}"
            self.execution_history.append({
                'time': timestamp,
                'shortcut': shortcut_key,
                'action': info['action'],
                'category': info['category']
            })
            
            # 履歴リストボックスに追加
            self.history_listbox.insert(0, history_entry)
            
            # 現在の状態更新
            self.current_status.config(text=f"実行: {shortcut_key} → {info['action']}", fg="green")
            
            # 統計更新
            self.update_statistics()
            
            # 一定時間後にステータスをリセット
            self.root.after(3000, lambda: self.current_status.config(text="キー入力待ち...", fg="blue"))
            
    def clear_history(self):
        """履歴をクリア"""
        self.history_listbox.delete(0, tk.END)
        self.execution_history.clear()
        self.update_statistics()
        self.current_status.config(text="履歴をクリアしました", fg="orange")
        self.root.after(2000, lambda: self.current_status.config(text="キー入力待ち...", fg="blue"))
        
    def update_statistics(self):
        """統計情報を更新"""
        total_count = len(self.execution_history)
        self.stats_label.config(text=f"実行回数: {total_count}回")
        
        if total_count > 0:
            # 最も使用されたショートカットを計算
            shortcut_counts = {}
            for entry in self.execution_history:
                shortcut = entry['shortcut']
                shortcut_counts[shortcut] = shortcut_counts.get(shortcut, 0) + 1
                
            most_used = max(shortcut_counts.items(), key=lambda x: x[1])
            self.most_used_label.config(text=f"最多使用: {most_used[0]} ({most_used[1]}回)")
        else:
            self.most_used_label.config(text="")

def main():
    root = tk.Tk()
    app = ShortcutDisplayApp(root)
    
    # フォーカスを設定してキーイベントを受け取る
    root.focus_set()
    
    # ウィンドウが閉じられるときの処理
    root.protocol("WM_DELETE_WINDOW", root.quit)
    
    # アプリケーション実行
    root.mainloop()

if __name__ == "__main__":
    main() 