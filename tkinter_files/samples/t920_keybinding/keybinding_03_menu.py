#!/usr/bin/env python3
"""
メニューアクセラレータとキーバインディング例
accelerator オプションと実際のキーバインディングを組み合わせた例
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class MenuAcceleratorApp:
    def __init__(self, root):
        self.root = root
        root.title("メニューアクセラレータ例")
        root.geometry("600x400")
        
        # メニューバー作成
        self.create_menubar()
        
        # メインコンテンツエリア
        self.create_content_area()
        
        # ステータスバー
        self.status_bar = tk.Label(root, text="準備完了", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
        # キーバインディング設定
        self.setup_keybindings()
        
        # ファイル関連の状態
        self.current_file = None
        self.is_modified = False
        
    def create_menubar(self):
        """メニューバーの作成"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # ファイルメニュー
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="ファイル", menu=file_menu, underline=0)
        
        file_menu.add_command(label="新規", command=self.new_file, 
                             accelerator="Ctrl+N", underline=0)
        file_menu.add_command(label="開く", command=self.open_file, 
                             accelerator="Ctrl+O", underline=0)
        file_menu.add_separator()
        file_menu.add_command(label="保存", command=self.save_file, 
                             accelerator="Ctrl+S", underline=0)
        file_menu.add_command(label="名前を付けて保存", command=self.save_as_file, 
                             accelerator="Ctrl+Shift+S", underline=3)
        file_menu.add_separator()
        file_menu.add_command(label="終了", command=self.exit_app, 
                             accelerator="Ctrl+Q", underline=0)
        
        # 編集メニュー
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="編集", menu=edit_menu, underline=0)
        
        edit_menu.add_command(label="元に戻す", command=self.undo, 
                             accelerator="Ctrl+Z", underline=0)
        edit_menu.add_command(label="やり直し", command=self.redo, 
                             accelerator="Ctrl+Y", underline=0)
        edit_menu.add_separator()
        edit_menu.add_command(label="切り取り", command=self.cut, 
                             accelerator="Ctrl+X", underline=0)
        edit_menu.add_command(label="コピー", command=self.copy, 
                             accelerator="Ctrl+C", underline=0)
        edit_menu.add_command(label="貼り付け", command=self.paste, 
                             accelerator="Ctrl+V", underline=0)
        edit_menu.add_separator()
        edit_menu.add_command(label="すべて選択", command=self.select_all, 
                             accelerator="Ctrl+A", underline=2)
        edit_menu.add_command(label="検索", command=self.find, 
                             accelerator="Ctrl+F", underline=0)
        
        # 表示メニュー
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="表示", menu=view_menu, underline=0)
        
        # チェックメニューの状態
        self.show_line_numbers = tk.BooleanVar(value=True)
        self.word_wrap = tk.BooleanVar(value=True)
        
        view_menu.add_checkbutton(label="行番号を表示", variable=self.show_line_numbers,
                                command=self.toggle_line_numbers, accelerator="Ctrl+L")
        view_menu.add_checkbutton(label="折り返し表示", variable=self.word_wrap,
                                command=self.toggle_word_wrap, accelerator="Ctrl+W")
        view_menu.add_separator()
        view_menu.add_command(label="フォントサイズを大きく", command=self.increase_font_size,
                             accelerator="Ctrl++")
        view_menu.add_command(label="フォントサイズを小さく", command=self.decrease_font_size,
                             accelerator="Ctrl+-")
        
        # ヘルプメニュー
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="ヘルプ", menu=help_menu, underline=0)
        
        help_menu.add_command(label="ショートカット一覧", command=self.show_shortcuts,
                             accelerator="F1", underline=0)
        help_menu.add_command(label="バージョン情報", command=self.show_about,
                             accelerator="Ctrl+I", underline=0)
        
    def create_content_area(self):
        """コンテンツエリアの作成"""
        # メインフレーム
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # テキストエリア
        text_frame = tk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        # 行番号用フレーム
        self.line_number_frame = tk.Frame(text_frame, width=50, bg="lightgray")
        self.line_number_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.line_number_text = tk.Text(self.line_number_frame, width=4, 
                                       state=tk.DISABLED, bg="lightgray",
                                       relief=tk.FLAT)
        self.line_number_text.pack(fill=tk.BOTH, expand=True)
        
        # メインテキストエリア
        self.text_area = tk.Text(text_frame, wrap=tk.WORD, undo=True)
        scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # テキスト変更イベント
        self.text_area.bind('<KeyRelease>', self.on_text_change)
        self.text_area.bind('<Button-1>', self.on_text_change)
        
        # 初期テキスト
        self.text_area.insert(1.0, "テキストエディタのサンプルです。\n\n"
                                   "メニューまたはキーボードショートカットを使用して\n"
                                   "各種機能を実行できます。\n\n"
                                   "F1キーでショートカット一覧を表示できます。")
        
        # フォント設定
        self.current_font_size = 11
        self.update_font()
        
    def setup_keybindings(self):
        """キーバインディングの設定"""
        # ファイル操作
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_as_file())
        self.root.bind('<Control-q>', lambda e: self.exit_app())
        
        # 編集操作
        self.root.bind('<Control-z>', lambda e: self.undo())
        self.root.bind('<Control-y>', lambda e: self.redo())
        self.root.bind('<Control-x>', lambda e: self.cut())
        self.root.bind('<Control-c>', lambda e: self.copy())
        self.root.bind('<Control-v>', lambda e: self.paste())
        self.root.bind('<Control-a>', lambda e: self.select_all())
        self.root.bind('<Control-f>', lambda e: self.find())
        
        # 表示操作
        self.root.bind('<Control-l>', lambda e: self.toggle_line_numbers())
        self.root.bind('<Control-w>', lambda e: self.toggle_word_wrap())
        self.root.bind('<Control-plus>', lambda e: self.increase_font_size())
        self.root.bind('<Control-minus>', lambda e: self.decrease_font_size())
        
        # ヘルプ
        self.root.bind('<F1>', lambda e: self.show_shortcuts())
        self.root.bind('<Control-i>', lambda e: self.show_about())
        
    # ファイル操作メソッド
    def new_file(self):
        if self.check_save_needed():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.is_modified = False
            self.update_title()
            self.status_bar.config(text="新しいファイルを作成しました")
            
    def open_file(self):
        if self.check_save_needed():
            filename = filedialog.askopenfilename(
                title="ファイルを開く",
                filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")]
            )
            if filename:
                try:
                    with open(filename, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.text_area.delete(1.0, tk.END)
                        self.text_area.insert(1.0, content)
                        self.current_file = filename
                        self.is_modified = False
                        self.update_title()
                        self.status_bar.config(text=f"ファイルを開きました: {filename}")
                except Exception as e:
                    messagebox.showerror("エラー", f"ファイルを開けませんでした:\n{str(e)}")
                    
    def save_file(self):
        if self.current_file is None:
            self.save_as_file()
        else:
            try:
                content = self.text_area.get(1.0, tk.END + '-1c')
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.is_modified = False
                self.update_title()
                self.status_bar.config(text=f"ファイルを保存しました: {self.current_file}")
            except Exception as e:
                messagebox.showerror("エラー", f"ファイルを保存できませんでした:\n{str(e)}")
                
    def save_as_file(self):
        filename = filedialog.asksaveasfilename(
            title="名前を付けて保存",
            defaultextension=".txt",
            filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")]
        )
        if filename:
            try:
                content = self.text_area.get(1.0, tk.END + '-1c')
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.current_file = filename
                self.is_modified = False
                self.update_title()
                self.status_bar.config(text=f"ファイルを保存しました: {filename}")
            except Exception as e:
                messagebox.showerror("エラー", f"ファイルを保存できませんでした:\n{str(e)}")
                
    def exit_app(self):
        if self.check_save_needed():
            self.root.quit()
            
    # 編集操作メソッド
    def undo(self):
        try:
            self.text_area.edit_undo()
            self.status_bar.config(text="元に戻しました")
        except tk.TclError:
            self.status_bar.config(text="元に戻す操作はありません")
            
    def redo(self):
        try:
            self.text_area.edit_redo()
            self.status_bar.config(text="やり直しました")
        except tk.TclError:
            self.status_bar.config(text="やり直す操作はありません")
            
    def cut(self):
        try:
            self.text_area.event_generate("<<Cut>>")
            self.status_bar.config(text="切り取りました")
        except:
            pass
            
    def copy(self):
        try:
            self.text_area.event_generate("<<Copy>>")
            self.status_bar.config(text="コピーしました")
        except:
            pass
            
    def paste(self):
        try:
            self.text_area.event_generate("<<Paste>>")
            self.status_bar.config(text="貼り付けました")
        except:
            pass
            
    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        self.status_bar.config(text="すべて選択しました")
        
    def find(self):
        search_text = tk.simpledialog.askstring("検索", "検索する文字列を入力してください:")
        if search_text:
            # 簡単な検索実装
            start_pos = self.text_area.search(search_text, "1.0", tk.END)
            if start_pos:
                end_pos = f"{start_pos}+{len(search_text)}c"
                self.text_area.tag_remove(tk.SEL, "1.0", tk.END)
                self.text_area.tag_add(tk.SEL, start_pos, end_pos)
                self.text_area.mark_set(tk.INSERT, start_pos)
                self.text_area.see(tk.INSERT)
                self.status_bar.config(text=f"'{search_text}' が見つかりました")
            else:
                self.status_bar.config(text=f"'{search_text}' は見つかりませんでした")
                
    # 表示操作メソッド
    def toggle_line_numbers(self):
        if self.show_line_numbers.get():
            self.line_number_frame.pack(side=tk.LEFT, fill=tk.Y, before=self.text_area)
            self.update_line_numbers()
        else:
            self.line_number_frame.pack_forget()
        self.status_bar.config(text=f"行番号表示: {'ON' if self.show_line_numbers.get() else 'OFF'}")
        
    def toggle_word_wrap(self):
        wrap_mode = tk.WORD if self.word_wrap.get() else tk.NONE
        self.text_area.config(wrap=wrap_mode)
        self.status_bar.config(text=f"折り返し表示: {'ON' if self.word_wrap.get() else 'OFF'}")
        
    def increase_font_size(self):
        self.current_font_size += 1
        self.update_font()
        self.status_bar.config(text=f"フォントサイズ: {self.current_font_size}")
        
    def decrease_font_size(self):
        if self.current_font_size > 8:
            self.current_font_size -= 1
            self.update_font()
            self.status_bar.config(text=f"フォントサイズ: {self.current_font_size}")
            
    def update_font(self):
        font = ("Consolas", self.current_font_size)
        self.text_area.config(font=font)
        self.line_number_text.config(font=font)
        
    # ヘルプメソッド
    def show_shortcuts(self):
        shortcuts_text = """キーボードショートカット一覧

ファイル操作:
  Ctrl+N    新規ファイル
  Ctrl+O    ファイルを開く
  Ctrl+S    保存
  Ctrl+Shift+S  名前を付けて保存
  Ctrl+Q    終了

編集操作:
  Ctrl+Z    元に戻す
  Ctrl+Y    やり直し
  Ctrl+X    切り取り
  Ctrl+C    コピー
  Ctrl+V    貼り付け
  Ctrl+A    すべて選択
  Ctrl+F    検索

表示操作:
  Ctrl+L    行番号表示切り替え
  Ctrl+W    折り返し表示切り替え
  Ctrl++    フォントサイズを大きく
  Ctrl+-    フォントサイズを小さく

ヘルプ:
  F1        このヘルプ
  Ctrl+I    バージョン情報"""
        
        messagebox.showinfo("ショートカット一覧", shortcuts_text)
        
    def show_about(self):
        about_text = """テキストエディタ v1.0

メニューアクセラレータとキーバインディングの
デモンストレーション用アプリケーション

作成者: Python Tkinter Examples"""
        messagebox.showinfo("バージョン情報", about_text)
        
    # ユーティリティメソッド
    def on_text_change(self, event=None):
        self.is_modified = True
        self.update_title()
        if self.show_line_numbers.get():
            self.update_line_numbers()
            
    def update_line_numbers(self):
        content = self.text_area.get(1.0, tk.END)
        lines = content.count('\n')
        line_numbers = '\n'.join(str(i) for i in range(1, lines + 1))
        
        self.line_number_text.config(state=tk.NORMAL)
        self.line_number_text.delete(1.0, tk.END)
        self.line_number_text.insert(1.0, line_numbers)
        self.line_number_text.config(state=tk.DISABLED)
        
    def update_title(self):
        title = "メニューアクセラレータ例"
        if self.current_file:
            title += f" - {self.current_file}"
        if self.is_modified:
            title += " *"
        self.root.title(title)
        
    def check_save_needed(self):
        if self.is_modified:
            result = messagebox.askyesnocancel(
                "保存の確認",
                "ファイルが変更されています。保存しますか？"
            )
            if result is True:  # Yes
                self.save_file()
                return not self.is_modified
            elif result is False:  # No
                return True
            else:  # Cancel
                return False
        return True

def main():
    # simpledialog import
    import tkinter.simpledialog
    
    root = tk.Tk()
    app = MenuAcceleratorApp(root)
    
    # ウィンドウが閉じられるときの処理
    root.protocol("WM_DELETE_WINDOW", app.exit_app)
    
    # アプリケーション実行
    root.mainloop()

if __name__ == "__main__":
    main() 