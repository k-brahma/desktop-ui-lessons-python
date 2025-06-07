"""
tkinter 設定選択画面
"""
import tkinter as tk
from tkinter import messagebox


class ConfigurationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("設定選択")
        self.geometry("500x700")
        
        self.create_widgets()
    
    def create_widgets(self):
        # タイトル
        title_label = tk.Label(self, text="アプリケーション設定", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # テーマ設定
        theme_frame = tk.LabelFrame(self, text="テーマ選択", font=("Arial", 12, "bold"), padx=10, pady=10)
        theme_frame.pack(fill="x", padx=20, pady=10)
        
        self.theme_var = tk.StringVar(value="light")
        
        themes = [
            ("ライトテーマ", "light"),
            ("ダークテーマ", "dark"),
            ("ハイコントラスト", "high_contrast"),
            ("システム設定に従う", "system")
        ]
        
        for text, value in themes:
            tk.Radiobutton(
                theme_frame,
                text=text,
                variable=self.theme_var,
                value=value,
                command=self.on_theme_changed
            ).pack(anchor="w", pady=2)
        
        # 言語設定
        language_frame = tk.LabelFrame(self, text="言語選択", font=("Arial", 12, "bold"), padx=10, pady=10)
        language_frame.pack(fill="x", padx=20, pady=10)
        
        self.language_var = tk.StringVar(value="ja")
        
        languages = [
            ("日本語", "ja"),
            ("English", "en"),
            ("Español", "es"),
            ("Français", "fr"),
            ("Deutsch", "de")
        ]
        
        for text, value in languages:
            tk.Radiobutton(
                language_frame,
                text=text,
                variable=self.language_var,
                value=value,
                command=self.on_language_changed
            ).pack(anchor="w", pady=2)
        
        # 難易度設定
        difficulty_frame = tk.LabelFrame(self, text="難易度レベル", font=("Arial", 12, "bold"), padx=10, pady=10)
        difficulty_frame.pack(fill="x", padx=20, pady=10)
        
        self.difficulty_var = tk.StringVar(value="normal")
        
        difficulties = [
            ("初心者", "beginner"),
            ("標準", "normal"),
            ("上級者", "advanced"),
            ("エキスパート", "expert")
        ]
        
        for text, value in difficulties:
            tk.Radiobutton(
                difficulty_frame,
                text=text,
                variable=self.difficulty_var,
                value=value,
                command=self.on_difficulty_changed
            ).pack(anchor="w", pady=2)
        
        # ボタン
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        apply_button = tk.Button(button_frame, text="設定を適用", command=self.apply_settings)
        apply_button.pack(side=tk.LEFT, padx=5)
        
        reset_button = tk.Button(button_frame, text="デフォルトに戻す", command=self.reset_settings)
        reset_button.pack(side=tk.LEFT, padx=5)
    
    def on_theme_changed(self):
        theme = self.theme_var.get()
        print(f"テーマが変更されました: {theme}")
    
    def on_language_changed(self):
        language = self.language_var.get()
        print(f"言語が変更されました: {language}")
    
    def on_difficulty_changed(self):
        difficulty = self.difficulty_var.get()
        print(f"難易度が変更されました: {difficulty}")
    
    def apply_settings(self):
        theme = self.theme_var.get()
        language = self.language_var.get()
        difficulty = self.difficulty_var.get()
        
        theme_names = {
            "light": "ライトテーマ",
            "dark": "ダークテーマ",
            "high_contrast": "ハイコントラスト",
            "system": "システム設定に従う"
        }
        
        language_names = {
            "ja": "日本語",
            "en": "English",
            "es": "Español",
            "fr": "Français",
            "de": "Deutsch"
        }
        
        difficulty_names = {
            "beginner": "初心者",
            "normal": "標準",
            "advanced": "上級者",
            "expert": "エキスパート"
        }
        
        message = f"設定を適用しました:\n\n" \
                 f"テーマ: {theme_names.get(theme, theme)}\n" \
                 f"言語: {language_names.get(language, language)}\n" \
                 f"難易度: {difficulty_names.get(difficulty, difficulty)}"
        
        messagebox.showinfo("設定適用", message)
    
    def reset_settings(self):
        self.theme_var.set("light")
        self.language_var.set("ja")
        self.difficulty_var.set("normal")
        messagebox.showinfo("リセット", "設定をデフォルト値にリセットしました")

if __name__ == "__main__":
    app = ConfigurationApp()
    app.mainloop() 