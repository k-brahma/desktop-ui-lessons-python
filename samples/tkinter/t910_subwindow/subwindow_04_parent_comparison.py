"""
親ウィンドウ指定の有無による違いのテスト
"""
import tkinter as tk


class ParentComparisonTest(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("親ウィンドウ指定テスト")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="親ウィンドウ指定テスト", font=("Arial", 16, "bold")).pack(pady=20)
        
        # 親指定あり
        tk.Button(
            self, 
            text="親ウィンドウ指定あり\n（推奨）", 
            command=self.open_with_parent,
            bg="lightgreen",
            width=20,
            height=3
        ).pack(pady=10)
        
        # 親指定なし
        tk.Button(
            self, 
            text="親ウィンドウ指定なし\n（非推奨）", 
            command=self.open_without_parent,
            bg="lightcoral",
            width=20,
            height=3
        ).pack(pady=10)
        
        # 説明
        explanation = """
テストしてみてください：

1. 各ボタンでウィンドウを開く
2. メインウィンドウを最小化/最大化
3. メインウィンドウを閉じてみる
4. タスクバーでの表示を確認
        """
        
        tk.Label(self, text=explanation, justify=tk.LEFT, font=("Arial", 10)).pack(pady=20)
    
    def open_with_parent(self):
        # 親ウィンドウ指定あり
        window = tk.Toplevel(self)  # selfを親として指定
        window.title("親指定あり")
        window.geometry("300x200")
        
        tk.Label(window, text="親ウィンドウ: 指定あり", font=("Arial", 12, "bold")).pack(pady=20)
        tk.Label(window, text="• メインと連動して最小化\n• メインを閉じると一緒に閉じる\n• タスクバーに個別に表示されない", 
                justify=tk.LEFT).pack(pady=10)
        tk.Button(window, text="閉じる", command=window.destroy).pack(pady=10)
    
    def open_without_parent(self):
        # 親ウィンドウ指定なし
        window = tk.Toplevel()  # 親を指定しない
        window.title("親指定なし")
        window.geometry("300x200")
        
        tk.Label(window, text="親ウィンドウ: 指定なし", font=("Arial", 12, "bold")).pack(pady=20)
        tk.Label(window, text="• 独立したウィンドウ\n• メインを閉じても残る可能性\n• タスクバーに個別表示", 
                justify=tk.LEFT).pack(pady=10)
        tk.Button(window, text="閉じる", command=window.destroy).pack(pady=10)

if __name__ == "__main__":
    app = ParentComparisonTest()
    app.mainloop() 