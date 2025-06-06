"""
tkinter 基本的なチェックボタン
"""
import tkinter as tk


class BasicCheckbuttonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Checkbuttonの例")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        # BooleanVar でチェック状態を管理
        self.check_var = tk.BooleanVar()
        
        self.checkbutton = tk.Checkbutton(
            self, 
            text="同意する", 
            variable=self.check_var,
            command=self.show_state
        )
        self.checkbutton.pack(pady=20)
        
        self.button = tk.Button(self, text="状態を確認", command=self.show_state)
        self.button.pack()
    
    def show_state(self):
        state = self.check_var.get()
        print(f"チェック状態: {'オン' if state else 'オフ'}")

if __name__ == "__main__":
    app = BasicCheckbuttonApp()
    app.mainloop() 