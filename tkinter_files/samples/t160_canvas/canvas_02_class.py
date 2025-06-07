"""
tkinter インタラクティブなCanvas描画アプリ
"""
import tkinter as tk
from tkinter import colorchooser, messagebox


class InteractiveCanvasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("インタラクティブCanvas描画")
        self.geometry("800x700")
        
        # 描画設定
        self.current_color = "blue"
        self.current_tool = "rectangle"
        self.line_width = 2
        
        # 描画用の変数
        self.start_x = 0
        self.start_y = 0
        self.current_item = None
        
        # アンドゥ機能用の履歴管理
        self.drawing_history = []  # 描画操作の履歴
        self.current_stroke = []   # 現在の描画操作（自由描画用）
        
        # 多角形描画用の変数
        self.polygon_points = []   # 多角形の頂点
        self.polygon_preview_lines = []  # 予定線（点線）
        self.polygon_temp_line = None    # マウス追跡用の一時的な線
        
        self.create_widgets()
        self.bind_events()
    
    def create_widgets(self):
        # コントロールパネル
        self.create_control_panel()
        
        # キャンバス
        self.canvas = tk.Canvas(
            self, 
            width=750, 
            height=500, 
            bg='white',
            relief=tk.SUNKEN, 
            borderwidth=2,
            cursor='crosshair'
        )
        self.canvas.pack(padx=10, pady=10)
        
        # ステータスバー
        self.status_var = tk.StringVar()
        self.status_var.set("準備完了 - 図形を描画してください")
        status_bar = tk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_control_panel(self):
        # メインコントロールフレーム
        control_frame = tk.Frame(self, bg="lightgray", height=120)
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        control_frame.pack_propagate(False)
        
        # 上段：ツール選択
        tool_frame = tk.Frame(control_frame, bg="lightgray")
        tool_frame.pack(pady=5)
        
        tk.Label(tool_frame, text="描画ツール:", bg="lightgray", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
        
        self.tool_var = tk.StringVar(value="rectangle")
        tools = [
            ("矩形", "rectangle"),
            ("楕円", "oval"),
            ("線", "line"),
            ("多角形", "polygon"),
            ("自由描画", "freehand")
        ]
        
        for text, tool in tools:
            tk.Radiobutton(
                tool_frame, 
                text=text, 
                variable=self.tool_var, 
                value=tool,
                bg="lightgray",
                command=self.tool_changed
            ).pack(side=tk.LEFT, padx=5)
        
        # 中段：色とサイズ設定
        setting_frame = tk.Frame(control_frame, bg="lightgray")
        setting_frame.pack(pady=5)
        
        # 色選択
        tk.Label(setting_frame, text="色:", bg="lightgray", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
        
        self.color_button = tk.Button(
            setting_frame, 
            bg=self.current_color, 
            width=3, 
            height=1, 
            command=self.choose_color
        )
        self.color_button.pack(side=tk.LEFT, padx=5)
        
        # 線の太さ
        tk.Label(setting_frame, text="線の太さ:", bg="lightgray", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=(20, 5))
        
        self.width_var = tk.IntVar(value=2)
        width_scale = tk.Scale(
            setting_frame, 
            from_=1, 
            to=10, 
            orient=tk.HORIZONTAL, 
            variable=self.width_var,
            bg="lightgray",
            command=self.width_changed
        )
        width_scale.pack(side=tk.LEFT, padx=5)
        
        # 下段：操作ボタン
        button_frame = tk.Frame(control_frame, bg="lightgray")
        button_frame.pack(pady=5)
        
        tk.Button(
            button_frame, 
            text="すべてクリア", 
            command=self.clear_canvas,
            bg="red",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, 
            text="最後の操作を取り消し", 
            command=self.undo_last,
            bg="orange",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, 
            text="保存", 
            command=self.save_drawing,
            bg="green",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)
        
        # 図形カウンター
        self.shape_count = 0
        self.count_label = tk.Label(button_frame, text="図形数: 0", bg="lightgray", font=("Arial", 10))
        self.count_label.pack(side=tk.RIGHT, padx=20)
    
    def bind_events(self):
        # マウスイベント
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw_motion)
        self.canvas.bind('<ButtonRelease-1>', self.end_draw)
        self.canvas.bind('<Motion>', self.mouse_move)
        self.canvas.bind('<Button-3>', self.finish_polygon)  # 右クリックで多角形完成
        self.canvas.bind('<Double-Button-1>', self.finish_polygon)  # ダブルクリックでも完成
    
    def tool_changed(self):
        self.current_tool = self.tool_var.get()
        
        # ツール変更時に多角形の途中描画をクリア
        if self.current_tool != "polygon":
            self.clear_polygon_preview()
        
        self.status_var.set(f"ツール変更: {self.current_tool}")
        
        # ステータスメッセージを更新
        if self.current_tool == "polygon":
            self.status_var.set("多角形モード: クリックで頂点追加、右クリックまたはダブルクリックで完成")
        
        # カーソルを変更
        if self.current_tool == "freehand":
            self.canvas.config(cursor="pencil")
        else:
            self.canvas.config(cursor="crosshair")
    
    def choose_color(self):
        color = colorchooser.askcolor(color=self.current_color, title="色を選択")
        if color[1]:  # 色が選択された場合
            self.current_color = color[1]
            self.color_button.config(bg=self.current_color)
            self.status_var.set(f"色変更: {self.current_color}")
    
    def width_changed(self, value):
        self.line_width = int(value)
        self.status_var.set(f"線の太さ変更: {self.line_width}")
    
    def start_draw(self, event):
        if self.current_tool == "polygon":
            # 多角形モードでは左クリックで頂点追加
            self.add_polygon_point(event.x, event.y)
            return
        
        self.start_x, self.start_y = event.x, event.y
        
        # 新しい描画操作の開始
        self.current_stroke = []
        
        if self.current_tool == "rectangle":
            self.current_item = self.canvas.create_rectangle(
                self.start_x, self.start_y, self.start_x, self.start_y,
                outline=self.current_color, width=self.line_width
            )
        elif self.current_tool == "oval":
            self.current_item = self.canvas.create_oval(
                self.start_x, self.start_y, self.start_x, self.start_y,
                outline=self.current_color, width=self.line_width
            )
        elif self.current_tool == "line":
            self.current_item = self.canvas.create_line(
                self.start_x, self.start_y, self.start_x, self.start_y,
                fill=self.current_color, width=self.line_width
            )
        elif self.current_tool == "freehand":
            # 自由描画の開始点
            self.freehand_points = [self.start_x, self.start_y]
    
    def draw_motion(self, event):
        if self.current_tool == "polygon":
            # 多角形モードではマウス追跡線を更新
            self.update_polygon_preview(event.x, event.y)
            return
        
        if self.current_item and self.current_tool != "freehand":
            self.canvas.coords(self.current_item, 
                             self.start_x, self.start_y, event.x, event.y)
        elif self.current_tool == "freehand" and hasattr(self, 'freehand_points'):
            # 自由描画
            line_id = self.canvas.create_line(
                self.freehand_points[-2], self.freehand_points[-1], 
                event.x, event.y,
                fill=self.current_color, width=self.line_width,
                capstyle=tk.ROUND, smooth=tk.TRUE
            )
            # 自由描画の線を現在のストロークに追加
            self.current_stroke.append(line_id)
            self.freehand_points.extend([event.x, event.y])
    
    def end_draw(self, event):
        if self.current_tool == "polygon":
            return  # 多角形は別途処理
        
        if self.current_item or self.current_tool == "freehand":
            # 描画操作を履歴に追加
            if self.current_tool == "freehand":
                # 自由描画の場合は複数の線をグループとして保存
                if self.current_stroke:
                    self.drawing_history.append(self.current_stroke.copy())
            else:
                # 通常の図形の場合は単一のアイテムを保存
                if self.current_item:
                    self.drawing_history.append([self.current_item])
            
            self.shape_count += 1
            self.count_label.config(text=f"図形数: {self.shape_count}")
            self.status_var.set(f"図形を作成しました（{self.current_tool}）")
        
        self.current_item = None
        self.current_stroke = []
        if hasattr(self, 'freehand_points'):
            delattr(self, 'freehand_points')
    
    def mouse_move(self, event):
        if self.current_tool == "polygon" and self.polygon_points:
            self.update_polygon_preview(event.x, event.y)
        else:
            self.status_var.set(f"座標: ({event.x}, {event.y}) | ツール: {self.current_tool}")
    
    def add_polygon_point(self, x, y):
        # 多角形の頂点を追加
        self.polygon_points.extend([x, y])
        
        # 小さな円で頂点を表示
        point_marker = self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=self.current_color, outline=self.current_color)
        self.polygon_preview_lines.append(point_marker)
        
        # 前の点から現在の点への線を描画（最初の点以外）
        if len(self.polygon_points) > 2:
            prev_x = self.polygon_points[-4]
            prev_y = self.polygon_points[-3]
            line = self.canvas.create_line(prev_x, prev_y, x, y, 
                                         fill=self.current_color, width=self.line_width, 
                                         dash=(5, 5))  # 点線
            self.polygon_preview_lines.append(line)
        
        points_count = len(self.polygon_points) // 2
        self.status_var.set(f"多角形: {points_count}個の頂点 | 右クリックまたはダブルクリックで完成")
    
    def update_polygon_preview(self, x, y):
        # マウス追跡用の一時的な線を更新
        if self.polygon_temp_line:
            self.canvas.delete(self.polygon_temp_line)
        
        if self.polygon_points:
            last_x = self.polygon_points[-2]
            last_y = self.polygon_points[-1]
            self.polygon_temp_line = self.canvas.create_line(
                last_x, last_y, x, y, 
                fill=self.current_color, width=self.line_width, 
                dash=(2, 2)  # より細かい点線
            )
    
    def finish_polygon(self, event):
        if self.current_tool != "polygon" or len(self.polygon_points) < 6:  # 最低3つの頂点が必要
            return
        
        # 座標データを保存してから予定線を削除
        points_copy = self.polygon_points.copy()
        points_count = len(points_copy) // 2
        
        # 予定線と頂点マーカーを削除
        self.clear_polygon_preview()
        
        # 実際の多角形を作成
        polygon_id = self.canvas.create_polygon(
            points_copy, 
            outline=self.current_color, 
            width=self.line_width,
            fill=""  # 塗りつぶしなし
        )
        
        # 履歴に追加
        self.drawing_history.append([polygon_id])
        
        # カウンターとステータスを更新
        self.shape_count += 1
        self.count_label.config(text=f"図形数: {self.shape_count}")
        self.status_var.set(f"多角形を作成しました（{points_count}個の頂点）")
    
    def clear_polygon_preview(self):
        # 予定線と頂点マーカーを削除
        for item in self.polygon_preview_lines:
            self.canvas.delete(item)
        self.polygon_preview_lines = []
        
        if self.polygon_temp_line:
            self.canvas.delete(self.polygon_temp_line)
            self.polygon_temp_line = None
        
        self.polygon_points = []
    
    def clear_canvas(self):
        if messagebox.askyesno("確認", "すべての図形を削除しますか？"):
            self.canvas.delete("all")
            self.drawing_history.clear()  # 履歴もクリア
            self.clear_polygon_preview()  # 多角形の予定線もクリア
            self.shape_count = 0
            self.count_label.config(text="図形数: 0")
            self.status_var.set("キャンバスをクリアしました")
    
    def undo_last(self):
        # 最後に描いた図形グループを削除
        if self.drawing_history:
            # 最後の描画操作を取得
            last_operation = self.drawing_history.pop()
            
            # そのグループのすべてのアイテムを削除
            for item_id in last_operation:
                try:
                    self.canvas.delete(item_id)
                except tk.TclError:
                    # アイテムが既に削除されている場合は無視
                    pass
            
            self.shape_count = max(0, self.shape_count - 1)
            self.count_label.config(text=f"図形数: {self.shape_count}")
            self.status_var.set("最後の図形を削除しました")
        else:
            messagebox.showinfo("情報", "削除する図形がありません。")
    
    def save_drawing(self):
        # 実際の保存機能は簡略化
        messagebox.showinfo("保存", f"描画を保存しました。\n図形数: {self.shape_count}")

if __name__ == "__main__":
    app = InteractiveCanvasApp()
    app.mainloop() 