"""
tkinter 複数のスクロールバーを持つウィジェット
"""
import random
import tkinter as tk


class MultiScrollApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("複数スクロールバー")
        self.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        # メインフレーム
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Canvas ウィジェット
        self.canvas = tk.Canvas(main_frame, bg="white")
        
        # 垂直スクロールバー
        v_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=v_scrollbar.set)
        
        # 水平スクロールバー
        h_scrollbar = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=h_scrollbar.set)
        
        # スクロールバーとキャンバスを配置
        self.canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Grid の重みを設定
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Canvas に大きなコンテンツを描画
        self.draw_content()
        
        # スクロール領域を設定
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        # マウスホイールでのスクロールを有効化
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind("<Button-4>", self.on_mouse_wheel_linux) # Linux
        self.canvas.bind("<Button-5>", self.on_mouse_wheel_linux) # Linux
        self.canvas.focus_set()
    
    def draw_content(self):
        # グリッド状にコンテンツを描画
        for i in range(50):
            for j in range(30):
                x1, y1 = j * 80 + 10, i * 50 + 10
                x2, y2 = x1 + 70, y1 + 40
                
                colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
                color = random.choice(colors)
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#555555", width=2)
                self.canvas.create_text(x1 + 35, y1 + 20, text=f"({i},{j})", font=("Arial", 9))
    
    def on_mouse_wheel(self, event):
        # WindowsとmacOSでの垂直スクロール
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_mouse_wheel_linux(self, event):
        # Linuxでの垂直スクロール
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

if __name__ == "__main__":
    app = MultiScrollApp()
    app.mainloop() 