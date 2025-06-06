"""
tkinter 基本的なCanvas描画
"""
import tkinter as tk


class BasicCanvasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("基本的なCanvas描画")
        self.geometry("600x500")
        
        self.create_widgets()
        self.draw_shapes()
    
    def create_widgets(self):
        # タイトル
        title_label = tk.Label(self, text="基本的な図形描画", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # キャンバス
        self.canvas = tk.Canvas(self, width=550, height=400, bg='white', relief=tk.SUNKEN, borderwidth=2)
        self.canvas.pack(padx=10, pady=10)
    
    def draw_shapes(self):
        # 線を描画
        self.canvas.create_line(50, 50, 200, 100, fill='red', width=3)
        self.canvas.create_text(125, 30, text="線", font=("Arial", 12, "bold"), fill="red")
        
        # 矩形を描画
        self.canvas.create_rectangle(50, 120, 150, 200, fill='lightblue', outline='blue', width=2)
        self.canvas.create_text(100, 210, text="矩形", font=("Arial", 12, "bold"), fill="blue")
        
        # 楕円を描画
        self.canvas.create_oval(200, 120, 300, 200, fill='lightgreen', outline='green', width=2)
        self.canvas.create_text(250, 210, text="楕円", font=("Arial", 12, "bold"), fill="green")
        
        # 多角形（三角形）を描画
        self.canvas.create_polygon(350, 200, 400, 120, 450, 200, fill='lightyellow', outline='orange', width=2)
        self.canvas.create_text(400, 210, text="多角形", font=("Arial", 12, "bold"), fill="orange")
        
        # 弧を描画
        self.canvas.create_arc(480, 120, 530, 200, start=0, extent=180, fill='lightcoral', outline='red', width=2)
        self.canvas.create_text(505, 210, text="弧", font=("Arial", 12, "bold"), fill="red")
        
        # テキストを描画
        self.canvas.create_text(300, 50, text='Canvasでの図形描画', font=('Arial', 16, 'bold'), fill='darkblue')
        
        # 複雑な図形（家）
        self.draw_house(300, 250)
    
    def draw_house(self, x, y):
        # 家の本体（矩形）
        self.canvas.create_rectangle(x-50, y, x+50, y+60, fill='lightgray', outline='black', width=2)
        
        # 屋根（三角形）
        self.canvas.create_polygon(x-60, y, x, y-40, x+60, y, fill='brown', outline='black', width=2)
        
        # ドア
        self.canvas.create_rectangle(x-15, y+20, x+15, y+60, fill='saddlebrown', outline='black', width=1)
        
        # ドアノブ
        self.canvas.create_oval(x+8, y+40, x+12, y+44, fill='gold', outline='black')
        
        # 窓
        self.canvas.create_rectangle(x-40, y+15, x-25, y+35, fill='lightblue', outline='black', width=1)
        self.canvas.create_rectangle(x+25, y+15, x+40, y+35, fill='lightblue', outline='black', width=1)
        
        # 窓の格子
        self.canvas.create_line(x-32.5, y+15, x-32.5, y+35, fill='black')
        self.canvas.create_line(x-40, y+25, x-25, y+25, fill='black')
        self.canvas.create_line(x+32.5, y+15, x+32.5, y+35, fill='black')
        self.canvas.create_line(x+25, y+25, x+40, y+25, fill='black')
        
        # ラベル
        self.canvas.create_text(x, y+80, text="家", font=("Arial", 12, "bold"), fill="black")

if __name__ == "__main__":
    app = BasicCanvasApp()
    app.mainloop() 