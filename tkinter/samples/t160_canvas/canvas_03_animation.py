"""
tkinter Canvasアニメーション例
"""
import math
import time
import tkinter as tk


class CanvasAnimationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Canvasアニメーション")
        self.geometry("800x700")
        
        # アニメーション制御
        self.is_running = False
        
        self.create_widgets()
        self.setup_animations()
    
    def create_widgets(self):
        # タイトル
        title_label = tk.Label(self, text="Canvasアニメーション例", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # コントロールパネル
        control_frame = tk.Frame(self, bg="lightgray")
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(
            control_frame, 
            text="開始", 
            command=self.start_animation,
            bg="green",
            fg="white",
            font=("Arial", 12, "bold"),
            width=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame, 
            text="停止", 
            command=self.stop_animation,
            bg="red",
            fg="white",
            font=("Arial", 12, "bold"),
            width=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame, 
            text="リセット", 
            command=self.reset_animation,
            bg="orange",
            fg="white",
            font=("Arial", 12, "bold"),
            width=8
        ).pack(side=tk.LEFT, padx=5)
        
        # ステータス表示
        self.status_var = tk.StringVar()
        self.status_var.set("停止中")
        status_label = tk.Label(control_frame, textvariable=self.status_var, font=("Arial", 12))
        status_label.pack(side=tk.RIGHT, padx=20)
        
        # キャンバス
        self.canvas = tk.Canvas(
            self, 
            width=750, 
            height=500, 
            bg='black',
            relief=tk.SUNKEN, 
            borderwidth=2
        )
        self.canvas.pack(padx=10, pady=10)
    
    def setup_animations(self):
        # 跳ねるボール
        self.ball1 = self.canvas.create_oval(50, 50, 80, 80, fill='red', outline='darkred', width=2)
        self.ball1_dx = 3
        self.ball1_dy = 2
        
        # 回転するボール
        self.ball2 = self.canvas.create_oval(100, 100, 130, 130, fill='blue', outline='darkblue', width=2)
        self.ball2_angle = 0
        self.ball2_center_x = 200
        self.ball2_center_y = 150
        self.ball2_radius = 80
        
        # 正弦波で動くボール
        self.ball3 = self.canvas.create_oval(300, 200, 330, 230, fill='green', outline='darkgreen', width=2)
        self.ball3_x = 300
        self.ball3_time = 0
        
        # アナログ時計
        self.setup_clock()
        
        # 星を描画
        self.draw_stars()
        
        # 初期位置を設定
        self.animation_step = 0
    
    def setup_clock(self):
        # 時計の中心
        self.clock_center_x = 600
        self.clock_center_y = 150
        self.clock_radius = 70
        
        # 時計の枠
        self.canvas.create_oval(
            self.clock_center_x - self.clock_radius,
            self.clock_center_y - self.clock_radius,
            self.clock_center_x + self.clock_radius,
            self.clock_center_y + self.clock_radius,
            outline='white', width=3
        )
        
        # 文字盤の数字
        for i in range(12):
            angle = i * 30 - 90  # 12時を上に
            rad = math.radians(angle)
            x = self.clock_center_x + (self.clock_radius - 20) * math.cos(rad)
            y = self.clock_center_y + (self.clock_radius - 20) * math.sin(rad)
            hour = 12 if i == 0 else i
            self.canvas.create_text(x, y, text=str(hour), fill='white', font=('Arial', 12, 'bold'))
        
        # 時計の針（初期化）
        self.hour_hand = self.canvas.create_line(
            self.clock_center_x, self.clock_center_y,
            self.clock_center_x, self.clock_center_y - 30,
            fill='white', width=4
        )
        
        self.minute_hand = self.canvas.create_line(
            self.clock_center_x, self.clock_center_y,
            self.clock_center_x, self.clock_center_y - 50,
            fill='yellow', width=3
        )
        
        self.second_hand = self.canvas.create_line(
            self.clock_center_x, self.clock_center_y,
            self.clock_center_x, self.clock_center_y - 60,
            fill='red', width=2
        )
        
        # 時計の中心点
        self.canvas.create_oval(
            self.clock_center_x - 5, self.clock_center_y - 5,
            self.clock_center_x + 5, self.clock_center_y + 5,
            fill='white'
        )
    
    def draw_stars(self):
        # 背景の星を描画
        import random
        random.seed(42)  # 同じ位置に星を配置
        
        for _ in range(30):
            x = random.randint(10, 740)
            y = random.randint(10, 490)
            size = random.randint(1, 3)
            
            self.canvas.create_oval(
                x - size, y - size, x + size, y + size,
                fill='white', outline='white'
            )
    
    def start_animation(self):
        if not self.is_running:
            self.is_running = True
            self.status_var.set("実行中")
            self.animate()
    
    def stop_animation(self):
        self.is_running = False
        self.status_var.set("停止中")
    
    def reset_animation(self):
        self.stop_animation()
        
        # ボールの位置をリセット
        self.canvas.coords(self.ball1, 50, 50, 80, 80)
        self.ball1_dx = 3
        self.ball1_dy = 2
        
        self.ball2_angle = 0
        self.ball3_time = 0
        self.ball3_x = 300
        self.animation_step = 0
        
        self.status_var.set("リセット完了")
    
    def animate(self):
        if not self.is_running:
            return
        
        # 跳ねるボールのアニメーション
        self.animate_bouncing_ball()
        
        # 回転するボールのアニメーション
        self.animate_rotating_ball()
        
        # 正弦波で動くボールのアニメーション
        self.animate_sine_ball()
        
        # 時計のアニメーション
        self.animate_clock()
        
        self.animation_step += 1
        
        # 次のフレームをスケジュール（約60FPS）
        self.after(16, self.animate)
    
    def animate_bouncing_ball(self):
        # 現在の位置を取得
        coords = self.canvas.coords(self.ball1)
        x1, y1, x2, y2 = coords
        
        # 新しい位置を計算
        new_x1 = x1 + self.ball1_dx
        new_y1 = y1 + self.ball1_dy
        new_x2 = x2 + self.ball1_dx
        new_y2 = y2 + self.ball1_dy
        
        # 境界チェック
        if new_x1 <= 0 or new_x2 >= 750:
            self.ball1_dx = -self.ball1_dx
        if new_y1 <= 0 or new_y2 >= 500:
            self.ball1_dy = -self.ball1_dy
        
        # 位置を更新
        self.canvas.move(self.ball1, self.ball1_dx, self.ball1_dy)
    
    def animate_rotating_ball(self):
        # 円軌道で回転
        self.ball2_angle += 2
        if self.ball2_angle >= 360:
            self.ball2_angle = 0
        
        rad = math.radians(self.ball2_angle)
        x = self.ball2_center_x + self.ball2_radius * math.cos(rad)
        y = self.ball2_center_y + self.ball2_radius * math.sin(rad)
        
        self.canvas.coords(self.ball2, x - 15, y - 15, x + 15, y + 15)
    
    def animate_sine_ball(self):
        # 正弦波で上下に動く
        self.ball3_time += 0.1
        self.ball3_x += 1
        
        if self.ball3_x > 750:
            self.ball3_x = -30
        
        y = 250 + 100 * math.sin(self.ball3_time)
        
        self.canvas.coords(self.ball3, self.ball3_x - 15, y - 15, self.ball3_x + 15, y + 15)
    
    def animate_clock(self):
        # 現在時刻を取得
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        
        # 針の角度を計算（12時を0度として時計回り）
        second_angle = seconds * 6 - 90  # 1秒 = 6度
        minute_angle = minutes * 6 + seconds * 0.1 - 90  # 1分 = 6度
        hour_angle = hours * 30 + minutes * 0.5 - 90  # 1時間 = 30度
        
        # 針の座標を計算
        def get_hand_coords(angle, length):
            rad = math.radians(angle)
            end_x = self.clock_center_x + length * math.cos(rad)
            end_y = self.clock_center_y + length * math.sin(rad)
            return self.clock_center_x, self.clock_center_y, end_x, end_y
        
        # 針を更新
        self.canvas.coords(self.second_hand, *get_hand_coords(second_angle, 60))
        self.canvas.coords(self.minute_hand, *get_hand_coords(minute_angle, 50))
        self.canvas.coords(self.hour_hand, *get_hand_coords(hour_angle, 30))

if __name__ == "__main__":
    app = CanvasAnimationApp()
    app.mainloop() 