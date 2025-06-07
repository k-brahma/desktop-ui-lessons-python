"""
tkinter クラスベースでのラジオボタン例
"""
import tkinter as tk


class RadiobuttonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Radiobuttonの例（クラスベース）")
        self.geometry("300x250")
        
        self.create_widgets()
    
    def create_widgets(self):
        # StringVar で選択状態を管理
        self.selected_option = tk.StringVar(value="option1")
        
        # ラジオボタンの作成
        self.radio1 = tk.Radiobutton(
            self, 
            text="オプション 1", 
            variable=self.selected_option, 
            value="option1",
            command=self.show_selection
        )
        self.radio1.pack(anchor="w", padx=20, pady=5)
        
        self.radio2 = tk.Radiobutton(
            self, 
            text="オプション 2", 
            variable=self.selected_option, 
            value="option2",
            command=self.show_selection
        )
        self.radio2.pack(anchor="w", padx=20, pady=5)
        
        self.radio3 = tk.Radiobutton(
            self, 
            text="オプション 3", 
            variable=self.selected_option, 
            value="option3",
            command=self.show_selection
        )
        self.radio3.pack(anchor="w", padx=20, pady=5)
        
        self.button = tk.Button(self, text="選択を確認", command=self.show_selection)
        self.button.pack(pady=20)
    
    def show_selection(self):
        selection = self.selected_option.get()
        print(f"選択された項目: {selection}")

if __name__ == "__main__":
    app = RadiobuttonApp()
    app.mainloop() 