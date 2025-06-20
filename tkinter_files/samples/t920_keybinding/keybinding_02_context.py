#!/usr/bin/env python3
"""
コンテキスト固有のキーバインディング例
異なるウィジェットで異なるキーバインディングを設定
"""

import tkinter as tk
from tkinter import ttk


class ContextKeyBindingApp:
    def __init__(self, root):
        self.root = root
        root.title("コンテキスト固有キーバインディング")
        root.geometry("600x400")
        
        # ノートブック（タブウィジェット）
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # テキストエディタタブ
        self.create_text_tab()
        
        # リスト管理タブ
        self.create_list_tab()
        
        # 計算機タブ
        self.create_calculator_tab()
        
        # ステータスバー
        self.status_bar = tk.Label(root, text="準備完了", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
    def create_text_tab(self):
        """テキストエディタタブ"""
        text_frame = tk.Frame(self.notebook)
        self.notebook.add(text_frame, text="テキストエディタ")
        
        # 説明ラベル
        info_label = tk.Label(text_frame, 
                             text="テキストエディタ - キーバインディング:\n"
                                  "Ctrl+D: 行を複製\n"
                                  "Ctrl+K: 行を削除\n"
                                  "Ctrl+U: 大文字に変換\n"
                                  "Ctrl+L: 小文字に変換",
                             justify=tk.LEFT, bg="lightyellow")
        info_label.pack(fill=tk.X, padx=5, pady=5)
        
        # テキストウィジェット
        text_container = tk.Frame(text_frame)
        text_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.text_widget = tk.Text(text_container, wrap=tk.WORD)
        scrollbar = tk.Scrollbar(text_container, orient=tk.VERTICAL, command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=scrollbar.set)
        
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 初期テキスト
        self.text_widget.insert(1.0, "ここにテキストを入力してください。\n"
                                     "Ctrl+Dで行複製、Ctrl+Kで行削除できます。\n"
                                     "Ctrl+U/Lで大文字/小文字変換もできます。")
        
        # テキスト固有のキーバインディング
        self.text_widget.bind('<Control-d>', self.duplicate_text_line)
        self.text_widget.bind('<Control-k>', self.delete_text_line)
        self.text_widget.bind('<Control-u>', self.text_to_upper)
        self.text_widget.bind('<Control-l>', self.text_to_lower)
        
    def create_list_tab(self):
        """リスト管理タブ"""
        list_frame = tk.Frame(self.notebook)
        self.notebook.add(list_frame, text="リスト管理")
        
        # 説明ラベル
        info_label = tk.Label(list_frame,
                             text="リスト管理 - キーバインディング:\n"
                                  "Delete: アイテム削除\n"
                                  "Ctrl+A: 全選択\n"
                                  "Ctrl+I: アイテム追加\n"
                                  "Enter: アイテム編集",
                             justify=tk.LEFT, bg="lightgreen")
        info_label.pack(fill=tk.X, padx=5, pady=5)
        
        # 入力フィールド
        input_frame = tk.Frame(list_frame)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(input_frame, text="新しいアイテム:").pack(side=tk.LEFT)
        self.list_entry = tk.Entry(input_frame)
        self.list_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.list_entry.bind('<Return>', self.add_list_item)
        
        add_btn = tk.Button(input_frame, text="追加", command=self.add_list_item)
        add_btn.pack(side=tk.RIGHT)
        
        # リストボックス
        list_container = tk.Frame(list_frame)
        list_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.listbox = tk.Listbox(list_container, selectmode=tk.EXTENDED)
        list_scrollbar = tk.Scrollbar(list_container, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=list_scrollbar.set)
        
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 初期データ
        for i in range(1, 11):
            self.listbox.insert(tk.END, f"アイテム {i}")
            
        # リスト固有のキーバインディング
        self.listbox.bind('<Delete>', self.delete_list_items)
        self.listbox.bind('<Control-a>', self.select_all_list_items)
        self.listbox.bind('<Control-i>', lambda e: self.list_entry.focus_set())
        self.listbox.bind('<Return>', self.edit_list_item)
        
    def create_calculator_tab(self):
        """計算機タブ"""
        calc_frame = tk.Frame(self.notebook)
        self.notebook.add(calc_frame, text="計算機")
        
        # 説明ラベル
        info_label = tk.Label(calc_frame,
                             text="計算機 - キーバインディング:\n"
                                  "数字キー: 数字入力\n"
                                  "+,-,*,/: 演算子\n"
                                  "Enter: 計算実行\n"
                                  "Escape: クリア",
                             justify=tk.LEFT, bg="lightblue")
        info_label.pack(fill=tk.X, padx=5, pady=5)
        
        # ディスプレイ
        self.calc_display = tk.Entry(calc_frame, font=("Arial", 16), justify=tk.RIGHT)
        self.calc_display.pack(fill=tk.X, padx=5, pady=5)
        self.calc_display.insert(0, "0")
        
        # ボタンフレーム
        button_frame = tk.Frame(calc_frame)
        button_frame.pack(expand=True, padx=5, pady=5)
        
        # 計算機ボタンレイアウト
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(button_frame, text=btn_text, width=5, height=2,
                              command=lambda t=btn_text: self.calc_button_click(t))
                btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                
        # グリッドの重み設定
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
            
        # 計算機固有のキーバインディング
        calc_frame.bind('<Key>', self.calc_key_press)
        calc_frame.focus_set()  # フォーカスを設定してキーイベントを受け取る
        
        # 計算機の状態
        self.calc_expression = ""
        self.calc_result = 0
        
    # テキストエディタ用メソッド
    def duplicate_text_line(self, event):
        widget = event.widget
        current_line = widget.index(tk.INSERT).split('.')[0]
        line_content = widget.get(f"{current_line}.0", f"{current_line}.end")
        widget.insert(f"{current_line}.end", f"\n{line_content}")
        self.status_bar.config(text="行を複製しました")
        self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))
        
    def delete_text_line(self, event):
        widget = event.widget
        current_line = widget.index(tk.INSERT).split('.')[0]
        widget.delete(f"{current_line}.0", f"{int(current_line)+1}.0")
        self.status_bar.config(text="行を削除しました")
        self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))
        
    def text_to_upper(self, event):
        widget = event.widget
        try:
            selected_text = widget.get(tk.SEL_FIRST, tk.SEL_LAST)
            widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
            widget.insert(tk.INSERT, selected_text.upper())
            self.status_bar.config(text="大文字に変換しました")
        except tk.TclError:
            self.status_bar.config(text="テキストを選択してください")
        self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))
        
    def text_to_lower(self, event):
        widget = event.widget
        try:
            selected_text = widget.get(tk.SEL_FIRST, tk.SEL_LAST)
            widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
            widget.insert(tk.INSERT, selected_text.lower())
            self.status_bar.config(text="小文字に変換しました")
        except tk.TclError:
            self.status_bar.config(text="テキストを選択してください")
        self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))
        
    # リスト管理用メソッド
    def add_list_item(self, event=None):
        text = self.list_entry.get().strip()
        if text:
            self.listbox.insert(tk.END, text)
            self.list_entry.delete(0, tk.END)
            self.status_bar.config(text=f"'{text}' を追加しました")
            self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))
            
    def delete_list_items(self, event):
        selections = self.listbox.curselection()
        if selections:
            # 後ろから削除（インデックスがずれないように）
            for index in reversed(selections):
                self.listbox.delete(index)
            self.status_bar.config(text=f"{len(selections)}個のアイテムを削除しました")
            self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))
            
    def select_all_list_items(self, event):
        self.listbox.select_set(0, tk.END)
        self.status_bar.config(text="すべてのアイテムを選択しました")
        self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))
        
    def edit_list_item(self, event):
        selection = self.listbox.curselection()
        if selection:
            current_text = self.listbox.get(selection[0])
            self.list_entry.delete(0, tk.END)
            self.list_entry.insert(0, current_text)
            self.list_entry.focus_set()
            self.listbox.delete(selection[0])
            self.status_bar.config(text="アイテムを編集モードにしました")
            
    # 計算機用メソッド
    def calc_button_click(self, btn_text):
        if btn_text == 'C':
            self.calc_display.delete(0, tk.END)
            self.calc_display.insert(0, "0")
            self.calc_expression = ""
        elif btn_text == '=':
            self.calc_execute()
        elif btn_text in '+-×÷':
            op = btn_text.replace('×', '*').replace('÷', '/')
            self.calc_expression += self.calc_display.get() + op
            self.calc_display.delete(0, tk.END)
        else:
            if self.calc_display.get() == "0":
                self.calc_display.delete(0, tk.END)
            self.calc_display.insert(tk.END, btn_text)
            
    def calc_key_press(self, event):
        key = event.char
        if key.isdigit() or key == '.':
            if self.calc_display.get() == "0" and key != '.':
                self.calc_display.delete(0, tk.END)
            self.calc_display.insert(tk.END, key)
        elif key in '+-*/':
            op = key
            self.calc_expression += self.calc_display.get() + op
            self.calc_display.delete(0, tk.END)
        elif key == '\r':  # Enter
            self.calc_execute()
        elif event.keysym == 'Escape':
            self.calc_display.delete(0, tk.END)
            self.calc_display.insert(0, "0")
            self.calc_expression = ""
            
    def calc_execute(self):
        try:
            full_expression = self.calc_expression + self.calc_display.get()
            result = eval(full_expression)  # 注意: 実際の製品では安全な評価が必要
            self.calc_display.delete(0, tk.END)
            self.calc_display.insert(0, str(result))
            self.calc_expression = ""
            self.status_bar.config(text=f"計算結果: {result}")
        except:
            self.calc_display.delete(0, tk.END)
            self.calc_display.insert(0, "エラー")
            self.calc_expression = ""
            self.status_bar.config(text="計算エラーが発生しました")
        self.root.after(2000, lambda: self.status_bar.config(text="準備完了"))

def main():
    root = tk.Tk()
    app = ContextKeyBindingApp(root)
    
    # ウィンドウが閉じられるときの処理
    root.protocol("WM_DELETE_WINDOW", root.quit)
    
    # アプリケーション実行
    root.mainloop()

if __name__ == "__main__":
    main() 