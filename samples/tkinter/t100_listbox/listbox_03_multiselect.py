"""
tkinter 複数選択リストボックス
"""
import tkinter as tk
from tkinter import messagebox


class MultiSelectListboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("複数選択リストボックス")
        self.geometry("400x500")
        
        self.create_widgets()
    
    def create_widgets(self):
        # タイトル
        tk.Label(self, text="プログラミング言語を選択（複数可）:", font=("Arial", 12, "bold")).pack(pady=10)
        
        # リストボックス（複数選択モード）
        self.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, height=8, font=("Arial", 10))
        self.listbox.pack(pady=10)
        
        # 項目を追加
        languages = [
            "Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", 
            "TypeScript", "PHP", "Ruby", "Swift", "Kotlin", "Dart"
        ]
        for lang in languages:
            self.listbox.insert(tk.END, lang)
        
        # ボタンフレーム
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        
        # 各種ボタン
        tk.Button(button_frame, text="選択項目を表示", command=self.show_selection).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="すべて選択", command=self.select_all).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="選択解除", command=self.clear_selection).pack(side=tk.LEFT, padx=5)
        
        # 項目操作フレーム
        operation_frame = tk.Frame(self)
        operation_frame.pack(pady=10)
        
        tk.Label(operation_frame, text="新しい言語:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.new_lang_entry = tk.Entry(operation_frame, width=15)
        self.new_lang_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Button(operation_frame, text="追加", command=self.add_language).pack(side=tk.LEFT, padx=5)
        tk.Button(operation_frame, text="削除", command=self.remove_selected).pack(side=tk.LEFT, padx=5)
        
        # 結果表示エリア
        tk.Label(self, text="選択結果:", font=("Arial", 10, "bold")).pack(pady=(20, 5))
        self.result_text = tk.Text(self, width=50, height=6, font=("Arial", 9))
        self.result_text.pack(pady=5)
    
    def show_selection(self):
        selection_indices = self.listbox.curselection()
        if selection_indices:
            selected_items = [self.listbox.get(i) for i in selection_indices]
            result = f"選択された言語 ({len(selected_items)}個):\n"
            result += "\n".join(f"- {item}" for item in selected_items)
        else:
            result = "何も選択されていません。"
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, result)
    
    def select_all(self):
        self.listbox.selection_set(0, tk.END)
        self.show_selection()
    
    def clear_selection(self):
        self.listbox.selection_clear(0, tk.END)
        self.result_text.delete(1.0, tk.END)
    
    def add_language(self):
        new_lang = self.new_lang_entry.get().strip()
        if new_lang:
            self.listbox.insert(tk.END, new_lang)
            self.new_lang_entry.delete(0, tk.END)
            messagebox.showinfo("追加完了", f"{new_lang} を追加しました。")
        else:
            messagebox.showwarning("警告", "言語名を入力してください。")
    
    def remove_selected(self):
        selection_indices = list(self.listbox.curselection())
        if selection_indices:
            # 後ろから削除（インデックスがずれるのを防ぐため）
            for i in reversed(selection_indices):
                self.listbox.delete(i)
            self.result_text.delete(1.0, tk.END)
            messagebox.showinfo("削除完了", f"{len(selection_indices)}個の項目を削除しました。")
        else:
            messagebox.showwarning("警告", "削除する項目を選択してください。")

if __name__ == "__main__":
    app = MultiSelectListboxApp()
    app.mainloop() 