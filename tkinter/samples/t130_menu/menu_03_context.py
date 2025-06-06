"""
tkinter コンテキストメニュー（右クリックメニュー）
"""
import tkinter as tk
from tkinter import messagebox


class ContextMenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("コンテキストメニュー")
        self.geometry("500x400")
        
        self.create_menu()
        self.create_widgets()
        self.create_context_menu()
    
    def create_menu(self):
        # メニューバーを作成
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        
        # ファイルメニュー
        file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="ファイル", menu=file_menu)
        file_menu.add_command(label="新規", command=self.new_file)
        file_menu.add_command(label="終了", command=self.quit)
        
        # 表示メニュー
        view_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="表示", menu=view_menu)
        
        # フォントサイズサブメニュー
        font_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label="フォントサイズ", menu=font_menu)
        font_menu.add_command(label="小 (10pt)", command=lambda: self.change_font_size(10))
        font_menu.add_command(label="中 (12pt)", command=lambda: self.change_font_size(12))
        font_menu.add_command(label="大 (14pt)", command=lambda: self.change_font_size(14))
        font_menu.add_command(label="特大 (16pt)", command=lambda: self.change_font_size(16))
    
    def create_widgets(self):
        # テキストエリア
        self.text_area = tk.Text(self, wrap=tk.WORD, font=("Arial", 12), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 初期テキスト
        self.text_area.insert(1.0, "このテキストエリアで右クリックしてみてください。\nコンテキストメニューが表示されます。\n\nテキストを選択してから右クリックすると、選択テキスト用のメニューが表示されます。")
        
        # ステータスバー
        self.status_bar = tk.Label(self, text="右クリックでコンテキストメニューを表示", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_context_menu(self):
        # 通常のコンテキストメニュー
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="元に戻す", command=self.undo)
        self.context_menu.add_command(label="やり直し", command=self.redo)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="全て選択", command=self.select_all)
        self.context_menu.add_command(label="貼り付け", command=self.paste)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="文字数をカウント", command=self.count_chars)
        
        # 選択テキスト用のコンテキストメニュー
        self.selection_menu = tk.Menu(self, tearoff=0)
        self.selection_menu.add_command(label="切り取り", command=self.cut)
        self.selection_menu.add_command(label="コピー", command=self.copy)
        self.selection_menu.add_command(label="削除", command=self.delete_selection)
        self.selection_menu.add_separator()
        self.selection_menu.add_command(label="大文字に変換", command=self.to_uppercase)
        self.selection_menu.add_command(label="小文字に変換", command=self.to_lowercase)
        self.selection_menu.add_separator()
        self.selection_menu.add_command(label="選択文字数をカウント", command=self.count_selected_chars)
        
        # 右クリックイベントをバインド
        self.text_area.bind("<Button-3>", self.show_context_menu)  # Windows/Linux
        self.text_area.bind("<Button-2>", self.show_context_menu)  # macOS
    
    def show_context_menu(self, event):
        # 選択テキストがあるかチェック
        try:
            selection = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            if selection:
                # 選択テキストがある場合
                self.selection_menu.post(event.x_root, event.y_root)
            else:
                # 選択テキストがない場合
                self.context_menu.post(event.x_root, event.y_root)
        except tk.TclError:
            # 選択テキストがない場合
            self.context_menu.post(event.x_root, event.y_root)
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.status_bar.config(text="新しいファイルを作成しました")
    
    def change_font_size(self, size):
        current_font = self.text_area.cget("font")
        if isinstance(current_font, str):
            # フォント名から新しいフォントを作成
            self.text_area.config(font=("Arial", size))
        else:
            # 既存のフォントのサイズを変更
            font_family = current_font[0] if current_font else "Arial"
            self.text_area.config(font=(font_family, size))
        self.status_bar.config(text=f"フォントサイズを{size}ptに変更しました")
    
    def undo(self):
        try:
            self.text_area.edit_undo()
            self.status_bar.config(text="操作を元に戻しました")
        except tk.TclError:
            self.status_bar.config(text="元に戻す操作がありません")
    
    def redo(self):
        try:
            self.text_area.edit_redo()
            self.status_bar.config(text="操作をやり直しました")
        except tk.TclError:
            self.status_bar.config(text="やり直す操作がありません")
    
    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.status_bar.config(text="全てのテキストを選択しました")
    
    def cut(self):
        self.text_area.event_generate("<<Cut>>")
        self.status_bar.config(text="選択テキストを切り取りました")
    
    def copy(self):
        self.text_area.event_generate("<<Copy>>")
        self.status_bar.config(text="選択テキストをコピーしました")
    
    def paste(self):
        self.text_area.event_generate("<<Paste>>")
        self.status_bar.config(text="テキストを貼り付けました")
    
    def delete_selection(self):
        try:
            self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.status_bar.config(text="選択テキストを削除しました")
        except tk.TclError:
            self.status_bar.config(text="削除するテキストを選択してください")
    
    def to_uppercase(self):
        try:
            selection = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.text_area.insert(tk.INSERT, selection.upper())
            self.status_bar.config(text="選択テキストを大文字に変換しました")
        except tk.TclError:
            self.status_bar.config(text="変換するテキストを選択してください")
    
    def to_lowercase(self):
        try:
            selection = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.text_area.insert(tk.INSERT, selection.lower())
            self.status_bar.config(text="選択テキストを小文字に変換しました")
        except tk.TclError:
            self.status_bar.config(text="変換するテキストを選択してください")
    
    def count_chars(self):
        content = self.text_area.get(1.0, tk.END)
        char_count = len(content) - 1  # 最後の改行を除く
        word_count = len(content.split())
        messagebox.showinfo("文字数カウント", f"文字数: {char_count}\n単語数: {word_count}")
    
    def count_selected_chars(self):
        try:
            selection = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            char_count = len(selection)
            word_count = len(selection.split())
            messagebox.showinfo("選択文字数カウント", f"選択文字数: {char_count}\n選択単語数: {word_count}")
        except tk.TclError:
            messagebox.showwarning("警告", "カウントするテキストを選択してください")

if __name__ == "__main__":
    app = ContextMenuApp()
    app.mainloop() 