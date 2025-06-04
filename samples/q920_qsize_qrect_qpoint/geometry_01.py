"""
QSize, QRect, QPoint基本サンプル - 基本図形クラスの操作

このモジュールは、PySide6の基本図形クラス（QPoint、QSize、QRect）の使用方法を示します。
これらのクラスは、GUI要素の位置、サイズ、領域を表現するための基本的なクラスです。

主要な学習ポイント:
- QPointによる座標点の操作
- QSizeによるサイズの管理
- QRectによる矩形領域の操作
- ウィジェットでの実用的な使用例

Authors: PySide6 Learning Team
Date: 2024
"""

import math
import sys

from PySide6.QtCore import QPoint, QRect, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class GeometryDemoWindow(QWidget):
    """
    QPoint、QSize、QRectの使用例を示すウィンドウクラス
    
    基本図形クラスの様々な操作と応用を実演します。
    """
    
    def __init__(self):
        """
        GeometryDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定と図形サンプルの作成を行います。
        """
        super().__init__()
        self.shapes = []  # 描画する図形のリスト
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々な基本図形クラスの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QPoint, QSize, QRect基本サンプル - 基本図形クラス")
        self.setGeometry(200, 200, 900, 700)
        
        # メインレイアウト
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        
        # 左側：コントロールパネル
        self.create_control_panel(main_layout)
        
        # 右側：描画エリア
        self.create_drawing_area(main_layout)
        
    def create_control_panel(self, layout):
        """
        コントロールパネルの作成
        
        Args:
            layout (QHBoxLayout): 追加先のレイアウト
        """
        control_widget = QWidget()
        control_widget.setFixedWidth(300)
        control_layout = QVBoxLayout()
        control_widget.setLayout(control_layout)
        
        # タイトル
        title_label = QLabel("基本図形クラス デモ")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                background-color: #ecf0f1;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 10px;
            }
        """)
        control_layout.addWidget(title_label)
        
        # QPointセクション
        self.create_point_section(control_layout)
        
        # QSizeセクション
        self.create_size_section(control_layout)
        
        # QRectセクション
        self.create_rect_section(control_layout)
        
        # 操作ボタン
        self.create_action_buttons(control_layout)
        
        # 情報表示
        self.create_info_display(control_layout)
        
        layout.addWidget(control_widget)
        
    def create_point_section(self, layout):
        """
        QPointセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        point_group = QGroupBox("QPoint - 座標点")
        point_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #3498db;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        point_layout = QVBoxLayout()
        
        # X座標
        x_layout = QHBoxLayout()
        x_layout.addWidget(QLabel("X:"))
        self.x_spinbox = QSpinBox()
        self.x_spinbox.setRange(0, 400)
        self.x_spinbox.setValue(100)
        self.x_spinbox.valueChanged.connect(self.update_shapes)
        x_layout.addWidget(self.x_spinbox)
        point_layout.addLayout(x_layout)
        
        # Y座標
        y_layout = QHBoxLayout()
        y_layout.addWidget(QLabel("Y:"))
        self.y_spinbox = QSpinBox()
        self.y_spinbox.setRange(0, 400)
        self.y_spinbox.setValue(100)
        self.y_spinbox.valueChanged.connect(self.update_shapes)
        y_layout.addWidget(self.y_spinbox)
        point_layout.addLayout(y_layout)
        
        point_group.setLayout(point_layout)
        layout.addWidget(point_group)
        
    def create_size_section(self, layout):
        """
        QSizeセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        size_group = QGroupBox("QSize - サイズ")
        size_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #e74c3c;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        size_layout = QVBoxLayout()
        
        # 幅
        width_layout = QHBoxLayout()
        width_layout.addWidget(QLabel("幅:"))
        self.width_spinbox = QSpinBox()
        self.width_spinbox.setRange(10, 300)
        self.width_spinbox.setValue(100)
        self.width_spinbox.valueChanged.connect(self.update_shapes)
        width_layout.addWidget(self.width_spinbox)
        size_layout.addLayout(width_layout)
        
        # 高さ
        height_layout = QHBoxLayout()
        height_layout.addWidget(QLabel("高さ:"))
        self.height_spinbox = QSpinBox()
        self.height_spinbox.setRange(10, 300)
        self.height_spinbox.setValue(80)
        self.height_spinbox.valueChanged.connect(self.update_shapes)
        height_layout.addWidget(self.height_spinbox)
        size_layout.addLayout(height_layout)
        
        size_group.setLayout(size_layout)
        layout.addWidget(size_group)
        
    def create_rect_section(self, layout):
        """
        QRectセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        rect_group = QGroupBox("QRect - 矩形")
        rect_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #f39c12;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        rect_layout = QVBoxLayout()
        
        # 矩形操作ボタン
        move_btn = QPushButton("矩形を移動")
        move_btn.clicked.connect(self.move_rect)
        move_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        rect_layout.addWidget(move_btn)
        
        resize_btn = QPushButton("矩形をリサイズ")
        resize_btn.clicked.connect(self.resize_rect)
        resize_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        rect_layout.addWidget(resize_btn)
        
        rect_group.setLayout(rect_layout)
        layout.addWidget(rect_group)
        
    def create_action_buttons(self, layout):
        """
        操作ボタンセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        action_group = QGroupBox("操作")
        action_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #9b59b6;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        action_layout = QVBoxLayout()
        
        # 図形追加ボタン
        add_rect_btn = QPushButton("矩形を追加")
        add_rect_btn.clicked.connect(self.add_rect)
        add_rect_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        action_layout.addWidget(add_rect_btn)
        
        add_circle_btn = QPushButton("円を追加")
        add_circle_btn.clicked.connect(self.add_circle)
        add_circle_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d68910;
            }
        """)
        action_layout.addWidget(add_circle_btn)
        
        clear_btn = QPushButton("クリア")
        clear_btn.clicked.connect(self.clear_shapes)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        action_layout.addWidget(clear_btn)
        
        action_group.setLayout(action_layout)
        layout.addWidget(action_group)
        
    def create_info_display(self, layout):
        """
        情報表示セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        self.info_label = QLabel("""
基本操作:

QPoint:
- 座標点を表現
- x(), y()で値取得
- setX(), setY()で値設定

QSize:
- サイズを表現
- width(), height()で値取得
- setWidth(), setHeight()で設定

QRect:
- 矩形領域を表現
- QPoint + QSizeから作成可能
- contains()で点の包含判定
        """)
        self.info_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Courier New', monospace;
                font-size: 10px;
            }
        """)
        layout.addWidget(self.info_label)
        
    def create_drawing_area(self, layout):
        """
        描画エリアの作成
        
        Args:
            layout (QHBoxLayout): 追加先のレイアウト
        """
        self.drawing_area = DrawingArea()
        layout.addWidget(self.drawing_area)
        
        # 初期図形の追加
        self.update_shapes()
        
    def update_shapes(self):
        """
        図形の更新
        """
        # 現在の値から基本図形を作成
        point = QPoint(self.x_spinbox.value(), self.y_spinbox.value())
        size = QSize(self.width_spinbox.value(), self.height_spinbox.value())
        rect = QRect(point, size)
        
        # 描画エリアに基本図形を設定
        self.drawing_area.set_basic_shapes(point, size, rect)
        
    def move_rect(self):
        """
        矩形の移動
        """
        import random
        new_x = random.randint(50, 350)
        new_y = random.randint(50, 350)
        self.x_spinbox.setValue(new_x)
        self.y_spinbox.setValue(new_y)
        
    def resize_rect(self):
        """
        矩形のリサイズ
        """
        import random
        new_width = random.randint(50, 200)
        new_height = random.randint(50, 200)
        self.width_spinbox.setValue(new_width)
        self.height_spinbox.setValue(new_height)
        
    def add_rect(self):
        """
        矩形の追加
        """
        point = QPoint(self.x_spinbox.value(), self.y_spinbox.value())
        size = QSize(self.width_spinbox.value(), self.height_spinbox.value())
        rect = QRect(point, size)
        self.drawing_area.add_shape(("rect", rect, QColor("#3498db")))
        
    def add_circle(self):
        """
        円の追加
        """
        point = QPoint(self.x_spinbox.value(), self.y_spinbox.value())
        size = QSize(self.width_spinbox.value(), self.height_spinbox.value())
        rect = QRect(point, size)  # 円は矩形に内接して描画
        self.drawing_area.add_shape(("circle", rect, QColor("#e74c3c")))
        
    def clear_shapes(self):
        """
        図形のクリア
        """
        self.drawing_area.clear_shapes()


class DrawingArea(QWidget):
    """
    図形描画エリア
    
    QPoint、QSize、QRectの可視化を行います。
    """
    
    def __init__(self):
        """
        DrawingAreaクラスのコンストラクタ
        """
        super().__init__()
        self.setMinimumSize(500, 500)
        self.setStyleSheet("background-color: white; border: 2px solid #bdc3c7;")
        
        self.basic_point = QPoint(100, 100)
        self.basic_size = QSize(100, 80)
        self.basic_rect = QRect(self.basic_point, self.basic_size)
        self.shapes = []
        
    def set_basic_shapes(self, point, size, rect):
        """
        基本図形の設定
        
        Args:
            point (QPoint): 座標点
            size (QSize): サイズ
            rect (QRect): 矩形
        """
        self.basic_point = point
        self.basic_size = size
        self.basic_rect = rect
        self.update()
        
    def add_shape(self, shape):
        """
        図形の追加
        
        Args:
            shape (tuple): (タイプ, 図形, 色)
        """
        self.shapes.append(shape)
        self.update()
        
    def clear_shapes(self):
        """
        図形のクリア
        """
        self.shapes.clear()
        self.update()
        
    def paintEvent(self, event):
        """
        描画イベント
        
        Args:
            event: ペイントイベント
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 基本図形の描画
        self.draw_basic_shapes(painter)
        
        # 追加図形の描画
        self.draw_additional_shapes(painter)
        
    def draw_basic_shapes(self, painter):
        """
        基本図形の描画
        
        Args:
            painter (QPainter): ペインター
        """
        # QPoint（点）の描画
        painter.setPen(QPen(QColor("#e74c3c"), 8))
        painter.drawPoint(self.basic_point)
        
        # 点のラベル
        painter.setPen(QPen(QColor("#2c3e50"), 2))
        painter.drawText(
            self.basic_point.x() + 10, 
            self.basic_point.y() - 10,
            f"QPoint({self.basic_point.x()}, {self.basic_point.y()})"
        )
        
        # QRect（矩形）の描画
        painter.setPen(QPen(QColor("#3498db"), 2))
        painter.setBrush(QBrush(QColor("#3498db"), Qt.BrushStyle.NoBrush))
        painter.drawRect(self.basic_rect)
        
        # 矩形のラベル
        painter.setPen(QPen(QColor("#2c3e50"), 2))
        painter.drawText(
            self.basic_rect.x(),
            self.basic_rect.y() - 5,
            f"QRect({self.basic_rect.x()}, {self.basic_rect.y()}, {self.basic_rect.width()}, {self.basic_rect.height()})"
        )
        
        # サイズの表示（矩形の中央）
        painter.drawText(
            self.basic_rect.center().x() - 30,
            self.basic_rect.center().y(),
            f"QSize({self.basic_size.width()}, {self.basic_size.height()})"
        )
        
        # 角の点を描画
        painter.setPen(QPen(QColor("#f39c12"), 6))
        painter.drawPoint(self.basic_rect.topLeft())
        painter.drawPoint(self.basic_rect.topRight())
        painter.drawPoint(self.basic_rect.bottomLeft())
        painter.drawPoint(self.basic_rect.bottomRight())
        
    def draw_additional_shapes(self, painter):
        """
        追加図形の描画
        
        Args:
            painter (QPainter): ペインター
        """
        for shape_type, shape_rect, color in self.shapes:
            painter.setPen(QPen(color, 2))
            painter.setBrush(QBrush(color, Qt.BrushStyle.SolidPattern))
            
            if shape_type == "rect":
                painter.drawRect(shape_rect)
            elif shape_type == "circle":
                painter.drawEllipse(shape_rect)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QPoint、QSize、QRectの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = GeometryDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 