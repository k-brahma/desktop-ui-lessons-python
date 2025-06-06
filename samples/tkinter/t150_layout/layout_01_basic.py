"""
tkinter 基本的なレイアウトマネージャー
"""
import tkinter as tk


class BasicLayoutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("基本的なレイアウトマネージャー")
        self.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        # タイトル
        title_label = tk.Label(self, text="レイアウトマネージャーの比較", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # 3つのフレームを作成（各レイアウトマネージャー用）
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pack レイアウトのデモ
        pack_frame = tk.LabelFrame(main_frame, text="Pack レイアウト", font=("Arial", 12, "bold"))
        pack_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(pack_frame, text="上", bg="lightblue").pack(side=tk.TOP, fill=tk.X)
        tk.Label(pack_frame, text="下", bg="lightgreen").pack(side=tk.BOTTOM, fill=tk.X)
        tk.Label(pack_frame, text="左", bg="lightcoral").pack(side=tk.LEFT, fill=tk.Y)
        tk.Label(pack_frame, text="右", bg="lightyellow").pack(side=tk.RIGHT, fill=tk.Y)
        tk.Label(pack_frame, text="中央", bg="lightgray").pack(fill=tk.BOTH, expand=True)
        
        # Grid レイアウトのデモ
        grid_frame = tk.LabelFrame(main_frame, text="Grid レイアウト", font=("Arial", 12, "bold"))
        grid_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(grid_frame, text="(0,0)", bg="lightblue").grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        tk.Label(grid_frame, text="(0,1)", bg="lightgreen").grid(row=0, column=1, sticky="nsew", padx=1, pady=1)
        tk.Label(grid_frame, text="(1,0)", bg="lightcoral").grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
        tk.Label(grid_frame, text="(1,1)", bg="lightyellow").grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
        
        # Grid の重み設定
        grid_frame.grid_rowconfigure(0, weight=1)
        grid_frame.grid_rowconfigure(1, weight=1)
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        
        # Place レイアウトのデモ
        place_frame = tk.LabelFrame(main_frame, text="Place レイアウト", font=("Arial", 12, "bold"))
        place_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(place_frame, text="左上", bg="lightblue").place(x=5, y=5)
        tk.Label(place_frame, text="中央", bg="lightgreen").place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        tk.Label(place_frame, text="右下", bg="lightcoral").place(relx=1.0, rely=1.0, anchor=tk.SE, x=-5, y=-5)

if __name__ == "__main__":
    app = BasicLayoutApp()
    app.mainloop() 