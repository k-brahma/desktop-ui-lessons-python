"""
tkinter 設定オプション画面
"""
import tkinter as tk
from tkinter import messagebox


class SettingsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("設定オプション")
        self.geometry("400x350")
        
        self.create_widgets()
    
    def create_widgets(self):
        # タイトル
        title_label = tk.Label(self, text="アプリケーション設定", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # 一般設定セクション
        general_frame = tk.LabelFrame(self, text="一般設定", font=("Arial", 12, "bold"), padx=10, pady=10)
        general_frame.pack(fill="x", padx=20, pady=10)
        
        # 設定変数
        self.auto_save_var = tk.BooleanVar(value=True)
        self.startup_var = tk.BooleanVar()
        self.backup_var = tk.BooleanVar(value=True)
        
        # チェックボタン
        auto_save_check = tk.Checkbutton(
            general_frame, 
            text="自動保存を有効にする", 
            variable=self.auto_save_var,
            command=self.on_setting_changed
        )
        auto_save_check.pack(anchor="w", pady=2)
        
        startup_check = tk.Checkbutton(
            general_frame, 
            text="Windowsスタートアップに追加", 
            variable=self.startup_var,
            command=self.on_setting_changed
        )
        startup_check.pack(anchor="w", pady=2)
        
        backup_check = tk.Checkbutton(
            general_frame, 
            text="自動バックアップを有効にする", 
            variable=self.backup_var,
            command=self.on_setting_changed
        )
        backup_check.pack(anchor="w", pady=2)
        
        # 通知設定セクション
        notification_frame = tk.LabelFrame(self, text="通知設定", font=("Arial", 12, "bold"), padx=10, pady=10)
        notification_frame.pack(fill="x", padx=20, pady=10)
        
        # 通知設定変数
        self.email_notification_var = tk.BooleanVar()
        self.desktop_notification_var = tk.BooleanVar(value=True)
        self.sound_notification_var = tk.BooleanVar()
        
        email_notification_check = tk.Checkbutton(
            notification_frame, 
            text="メール通知", 
            variable=self.email_notification_var,
            command=self.on_setting_changed
        )
        email_notification_check.pack(anchor="w", pady=2)
        
        desktop_notification_check = tk.Checkbutton(
            notification_frame, 
            text="デスクトップ通知", 
            variable=self.desktop_notification_var,
            command=self.on_setting_changed
        )
        desktop_notification_check.pack(anchor="w", pady=2)
        
        sound_notification_check = tk.Checkbutton(
            notification_frame, 
            text="音声通知", 
            variable=self.sound_notification_var,
            command=self.on_setting_changed
        )
        sound_notification_check.pack(anchor="w", pady=2)
        
        # ボタン
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        save_button = tk.Button(button_frame, text="設定を保存", command=self.save_settings)
        save_button.pack(side=tk.LEFT, padx=5)
        
        reset_button = tk.Button(button_frame, text="リセット", command=self.reset_settings)
        reset_button.pack(side=tk.LEFT, padx=5)
    
    def on_setting_changed(self):
        print("設定が変更されました")
    
    def save_settings(self):
        settings = {
            "自動保存": self.auto_save_var.get(),
            "スタートアップ": self.startup_var.get(),
            "自動バックアップ": self.backup_var.get(),
            "メール通知": self.email_notification_var.get(),
            "デスクトップ通知": self.desktop_notification_var.get(),
            "音声通知": self.sound_notification_var.get()
        }
        
        enabled_settings = [key for key, value in settings.items() if value]
        message = "有効な設定:\n" + "\n".join([f"• {setting}" for setting in enabled_settings])
        messagebox.showinfo("設定保存", message if enabled_settings else "有効な設定がありません")
    
    def reset_settings(self):
        self.auto_save_var.set(True)
        self.startup_var.set(False)
        self.backup_var.set(True)
        self.email_notification_var.set(False)
        self.desktop_notification_var.set(True)
        self.sound_notification_var.set(False)
        messagebox.showinfo("リセット", "設定をデフォルト値にリセットしました")

if __name__ == "__main__":
    app = SettingsApp()
    app.mainloop() 