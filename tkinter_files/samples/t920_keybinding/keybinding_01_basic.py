#!/usr/bin/env python3
"""
基本的なキーバインディング例
特定のキーでボタンを実行し、フォーカス移動も行う
"""

import tkinter as tk
from tkinter import ttk


class BasicKeyBindingApp:
    def __init__(self, root):
        self.root = root
        root.title("基本的なキーバインディング")
        root.geometry("400x450")
        
        # メインフレーム
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 説明ラベル
        info_label = tk.Label(main_frame, 
                             text="キーバインディングの例\n"
                                  "F1: ボタン1実行, F2: ボタン2実行\n"
                                  "F3-F5: エントリフィールドにフォーカス移動\n"
                                  "Ctrl+Enter: メッセージ表示",
                             justify=tk.LEFT, fg="blue")
        info_label.pack(pady=(0, 20))
        
        # ボタン群
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.button1 = tk.Button(button_frame, text="ボタン1 (F1)", 
                               command=self.button1_click, width=15)
        self.button1.pack(side=tk.LEFT, padx=5)
        
        self.button2 = tk.Button(button_frame, text="ボタン2 (F2)", 
                               command=self.button2_click, width=15)
        self.button2.pack(side=tk.LEFT, padx=5)
        
        # エントリフィールド群
        entry_frame = tk.Frame(main_frame)
        entry_frame.pack(fill=tk.X, pady=20)
        
        tk.Label(entry_frame, text="エントリ1 (F3):").pack(anchor=tk.W)
        self.entry1 = tk.Entry(entry_frame)
        self.entry1.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(entry_frame, text="エントリ2 (F4):").pack(anchor=tk.W)
        self.entry2 = tk.Entry(entry_frame)
        self.entry2.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(entry_frame, text="エントリ3 (F5):").pack(anchor=tk.W)
        self.entry3 = tk.Entry(entry_frame)
        self.entry3.pack(fill=tk.X, pady=(0, 10))
        
        # ステータス表示
        self.status_label = tk.Label(main_frame, text="キーを押してください...", 
                                   relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(fill=tk.X, pady=(20, 0))
        
        # キーバインディング設定
        self.setup_keybindings()
        
    def setup_keybindings(self):
        # ボタンのキーバインディング
        self.root.bind('<F1>', lambda e: self.button1.invoke())
        self.root.bind('<F2>', lambda e: self.button2.invoke())
        
        # フォーカス移動のキーバインディング
        self.root.bind('<F3>', lambda e: self.focus_entry1())
        self.root.bind('<F4>', lambda e: self.focus_entry2())
        self.root.bind('<F5>', lambda e: self.focus_entry3())
        
        # カスタムショートカット
        self.root.bind('<Control-Return>', lambda e: self.show_message())
        self.root.bind('<Escape>', lambda e: self.clear_all())
        
        # フォーカス管理（Tab/Shift+Tab）
        self.root.bind('<Control-Tab>', self.focus_next_widget)
        self.root.bind('<Control-Shift-Tab>', self.focus_prev_widget)
        
    def button1_click(self):
        self.status_label.config(text="ボタン1がクリックされました！")
        self.root.after(2000, self.clear_status)
        
    def button2_click(self):
        self.status_label.config(text="ボタン2がクリックされました！")
        self.root.after(2000, self.clear_status)
        
    def focus_entry1(self):
        self.entry1.focus_set()
        self.status_label.config(text="エントリ1にフォーカスしました")
        self.root.after(2000, self.clear_status)
        
    def focus_entry2(self):
        self.entry2.focus_set()
        self.status_label.config(text="エントリ2にフォーカスしました")
        self.root.after(2000, self.clear_status)
        
    def focus_entry3(self):
        self.entry3.focus_set()
        self.status_label.config(text="エントリ3にフォーカスしました")
        self.root.after(2000, self.clear_status)
        
    def show_message(self):
        values = [self.entry1.get(), self.entry2.get(), self.entry3.get()]
        message = f"入力値: {', '.join(f'「{v}」' if v else '空' for v in values)}"
        self.status_label.config(text=message)
        self.root.after(3000, self.clear_status)
        
    def clear_all(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.status_label.config(text="すべてクリアしました")
        self.root.after(2000, self.clear_status)
        
    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus_set()
        
    def focus_prev_widget(self, event):
        event.widget.tk_focusPrev().focus_set()
        
    def clear_status(self):
        self.status_label.config(text="キーを押してください...")

def main():
    root = tk.Tk()
    app = BasicKeyBindingApp(root)
    
    # ウィンドウが閉じられるときの処理
    root.protocol("WM_DELETE_WINDOW", root.quit)
    
    # アプリケーション実行
    root.mainloop()

if __name__ == "__main__":
    main() 