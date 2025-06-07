"""
tkinter カラーミキサー
"""
import tkinter as tk


class ColorMixerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("カラーミキサー")
        self.geometry("400x450")
        
        self.create_widgets()
        self.update_color()
    
    def create_widgets(self):
        # タイトル
        tk.Label(self, text="RGB カラーミキサー", font=("Arial", 16, "bold")).pack(pady=10)
        
        # 色表示用のキャンバス
        self.color_canvas = tk.Canvas(self, width=200, height=100, bg="black")
        self.color_canvas.pack(pady=10)
        
        # RGB値表示用のラベル
        self.rgb_label = tk.Label(self, text="RGB: (0, 0, 0)", font=("Arial", 12))
        self.rgb_label.pack(pady=5)
        
        # 16進値表示用のラベル
        self.hex_label = tk.Label(self, text="HEX: #000000", font=("Arial", 12))
        self.hex_label.pack(pady=5)
        
        # RGBスライダーのフレーム
        sliders_frame = tk.Frame(self)
        sliders_frame.pack(pady=20)
        
        # 赤 (Red) スライダー
        self.red_var = tk.IntVar()
        red_frame = tk.Frame(sliders_frame)
        red_frame.pack(pady=5)
        tk.Label(red_frame, text="Red:", width=6, fg="red", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        self.red_scale = tk.Scale(
            red_frame, from_=0, to=255, orient=tk.HORIZONTAL,
            length=200, variable=self.red_var, command=self.update_color
        )
        self.red_scale.pack(side=tk.LEFT, padx=10)
        
        # 緑 (Green) スライダー
        self.green_var = tk.IntVar()
        green_frame = tk.Frame(sliders_frame)
        green_frame.pack(pady=5)
        tk.Label(green_frame, text="Green:", width=6, fg="green", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        self.green_scale = tk.Scale(
            green_frame, from_=0, to=255, orient=tk.HORIZONTAL,
            length=200, variable=self.green_var, command=self.update_color
        )
        self.green_scale.pack(side=tk.LEFT, padx=10)
        
        # 青 (Blue) スライダー
        self.blue_var = tk.IntVar()
        blue_frame = tk.Frame(sliders_frame)
        blue_frame.pack(pady=5)
        tk.Label(blue_frame, text="Blue:", width=6, fg="blue", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        self.blue_scale = tk.Scale(
            blue_frame, from_=0, to=255, orient=tk.HORIZONTAL,
            length=200, variable=self.blue_var, command=self.update_color
        )
        self.blue_scale.pack(side=tk.LEFT, padx=10)

    def update_color(self, event=None):
        r = self.red_var.get()
        g = self.green_var.get()
        b = self.blue_var.get()
        
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        
        self.color_canvas.config(bg=hex_color)
        self.rgb_label.config(text=f"RGB: ({r}, {g}, {b})")
        self.hex_label.config(text=f"HEX: {hex_color.upper()}")

if __name__ == "__main__":
    app = ColorMixerApp()
    app.mainloop() 