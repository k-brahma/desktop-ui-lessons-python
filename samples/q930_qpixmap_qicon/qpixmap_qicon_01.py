"""
QPixmap & QIcon基本サンプル - 画像とアイコンの処理

このモジュールは、PySide6のQPixmapとQIconクラスの基本的な使用方法を示します。
QPixmapは画像の表示と操作、QIconは様々なサイズのアイコンを管理するためのクラスです。

主要な学習ポイント:
- QPixmapによる画像の読み込み、表示、変換
- QIconによるアイコンの管理とサイズ処理
- 画像の描画、変形、フィルタ操作
- プログラムで画像を生成する方法
- 実用的なアイコンとプレビュー機能

Authors: PySide6 Learning Team
Date: 2024
"""

import math
import os
import sys
from typing import Optional

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import (
    QBrush,
    QColor,
    QFont,
    QIcon,
    QPainter,
    QPen,
    QPixmap,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSlider,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class PixmapIconDemoWindow(QWidget):
    """
    QPixmapとQIconの使用例を示すウィンドウクラス
    
    画像処理、アイコン管理、描画操作の様々な機能を実演します。
    """
    
    def __init__(self):
        """
        PixmapIconDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定と画像・アイコンサンプルの作成を行います。
        """
        super().__init__()
        self.current_pixmap = None
        self.original_pixmap = None
        self.init_ui()
        self.create_sample_images()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQPixmapとQIconの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QPixmap & QIcon基本サンプル - 画像とアイコン処理")
        self.setGeometry(200, 200, 1200, 800)
        
        # メインレイアウト
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        
        # 左側：コントロールパネル
        self.create_control_panel(main_layout)
        
        # 右側：画像表示エリア
        self.create_image_display_area(main_layout)
        
    def create_control_panel(self, layout):
        """
        コントロールパネルの作成
        
        Args:
            layout (QHBoxLayout): 追加先のレイアウト
        """
        control_widget = QWidget()
        control_widget.setFixedWidth(400)
        control_layout = QVBoxLayout()
        control_widget.setLayout(control_layout)
        
        # タイトル
        title_label = QLabel("QPixmap & QIcon デモ")
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
        
        # 画像作成セクション
        self.create_image_creation_section(control_layout)
        
        # 画像変形セクション
        self.create_transformation_section(control_layout)
        
        # アイコンセクション
        self.create_icon_section(control_layout)
        
        # 描画効果セクション
        self.create_effects_section(control_layout)
        
        # ログ表示
        self.create_log_section(control_layout)
        
        layout.addWidget(control_widget)
        
    def create_image_creation_section(self, layout):
        """
        画像作成セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        creation_group = QGroupBox("画像の作成と操作")
        creation_group.setStyleSheet("""
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
        
        creation_layout = QVBoxLayout()
        
        # 画像作成ボタン
        button_layout = QHBoxLayout()
        
        create_gradient_btn = QPushButton("グラデーション")
        create_gradient_btn.clicked.connect(self.create_gradient_image)
        create_gradient_btn.setStyleSheet(self.get_button_style("#3498db"))
        button_layout.addWidget(create_gradient_btn)
        
        create_pattern_btn = QPushButton("パターン")
        create_pattern_btn.clicked.connect(self.create_pattern_image)
        create_pattern_btn.setStyleSheet(self.get_button_style("#e74c3c"))
        button_layout.addWidget(create_pattern_btn)
        
        creation_layout.addLayout(button_layout)
        
        create_chart_btn = QPushButton("簡単なチャート")
        create_chart_btn.clicked.connect(self.create_chart_image)
        create_chart_btn.setStyleSheet(self.get_button_style("#27ae60"))
        creation_layout.addWidget(create_chart_btn)
        
        create_icon_btn = QPushButton("カスタムアイコン")
        create_icon_btn.clicked.connect(self.create_custom_icon)
        create_icon_btn.setStyleSheet(self.get_button_style("#9b59b6"))
        creation_layout.addWidget(create_icon_btn)
        
        creation_group.setLayout(creation_layout)
        layout.addWidget(creation_group)
        
    def create_transformation_section(self, layout):
        """
        変形セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        transform_group = QGroupBox("画像の変形")
        transform_group.setStyleSheet("""
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
        
        transform_layout = QVBoxLayout()
        
        # スケール制御
        scale_layout = QHBoxLayout()
        scale_layout.addWidget(QLabel("スケール:"))
        self.scale_slider = QSlider(Qt.Orientation.Horizontal)
        self.scale_slider.setRange(10, 300)
        self.scale_slider.setValue(100)
        self.scale_slider.valueChanged.connect(self.apply_transformations)
        scale_layout.addWidget(self.scale_slider)
        self.scale_label = QLabel("100%")
        self.scale_label.setMinimumWidth(50)
        scale_layout.addWidget(self.scale_label)
        transform_layout.addLayout(scale_layout)
        
        # 回転制御
        rotation_layout = QHBoxLayout()
        rotation_layout.addWidget(QLabel("回転:"))
        self.rotation_slider = QSlider(Qt.Orientation.Horizontal)
        self.rotation_slider.setRange(-180, 180)
        self.rotation_slider.setValue(0)
        self.rotation_slider.valueChanged.connect(self.apply_transformations)
        rotation_layout.addWidget(self.rotation_slider)
        self.rotation_label = QLabel("0°")
        self.rotation_label.setMinimumWidth(50)
        rotation_layout.addWidget(self.rotation_label)
        transform_layout.addLayout(rotation_layout)
        
        # 変形ボタン
        transform_button_layout = QHBoxLayout()
        
        flip_h_btn = QPushButton("水平反転")
        flip_h_btn.clicked.connect(self.flip_horizontal)
        flip_h_btn.setStyleSheet(self.get_button_style("#e67e22"))
        transform_button_layout.addWidget(flip_h_btn)
        
        flip_v_btn = QPushButton("垂直反転")
        flip_v_btn.clicked.connect(self.flip_vertical)
        flip_v_btn.setStyleSheet(self.get_button_style("#e67e22"))
        transform_button_layout.addWidget(flip_v_btn)
        
        transform_layout.addLayout(transform_button_layout)
        
        reset_btn = QPushButton("変形をリセット")
        reset_btn.clicked.connect(self.reset_transformations)
        reset_btn.setStyleSheet(self.get_button_style("#95a5a6"))
        transform_layout.addWidget(reset_btn)
        
        transform_group.setLayout(transform_layout)
        layout.addWidget(transform_group)
        
    def create_icon_section(self, layout):
        """
        アイコンセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        icon_group = QGroupBox("QIcon デモ")
        icon_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #8e44ad;
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
        
        icon_layout = QVBoxLayout()
        
        # アイコンサイズ選択
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("サイズ:"))
        self.icon_size_combo = QComboBox()
        self.icon_size_combo.addItems(["16x16", "24x24", "32x32", "48x48", "64x64", "128x128"])
        self.icon_size_combo.setCurrentText("32x32")
        self.icon_size_combo.currentTextChanged.connect(self.update_icon_display)
        size_layout.addWidget(self.icon_size_combo)
        icon_layout.addLayout(size_layout)
        
        # アイコン表示エリア
        self.icon_display_area = QWidget()
        self.icon_display_area.setFixedHeight(100)
        self.icon_display_area.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
            }
        """)
        icon_layout.addWidget(self.icon_display_area)
        
        # アイコン作成ボタン
        icon_buttons_layout = QHBoxLayout()
        
        system_icon_btn = QPushButton("システムアイコン")
        system_icon_btn.clicked.connect(self.show_system_icons)
        system_icon_btn.setStyleSheet(self.get_button_style("#16a085"))
        icon_buttons_layout.addWidget(system_icon_btn)
        
        multi_size_btn = QPushButton("マルチサイズ")
        multi_size_btn.clicked.connect(self.create_multi_size_icon)
        multi_size_btn.setStyleSheet(self.get_button_style("#2980b9"))
        icon_buttons_layout.addWidget(multi_size_btn)
        
        icon_layout.addLayout(icon_buttons_layout)
        
        icon_group.setLayout(icon_layout)
        layout.addWidget(icon_group)
        
    def create_effects_section(self, layout):
        """
        効果セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        effects_group = QGroupBox("画像効果")
        effects_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #c0392b;
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
        
        effects_layout = QVBoxLayout()
        
        # 透明度制御
        opacity_layout = QHBoxLayout()
        opacity_layout.addWidget(QLabel("透明度:"))
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.valueChanged.connect(self.apply_opacity)
        opacity_layout.addWidget(self.opacity_slider)
        self.opacity_label = QLabel("100%")
        self.opacity_label.setMinimumWidth(50)
        opacity_layout.addWidget(self.opacity_label)
        effects_layout.addLayout(opacity_layout)
        
        # 効果ボタン
        effects_buttons_layout = QHBoxLayout()
        
        grayscale_btn = QPushButton("グレースケール")
        grayscale_btn.clicked.connect(self.apply_grayscale)
        grayscale_btn.setStyleSheet(self.get_button_style("#7f8c8d"))
        effects_buttons_layout.addWidget(grayscale_btn)
        
        sepia_btn = QPushButton("セピア")
        sepia_btn.clicked.connect(self.apply_sepia)
        sepia_btn.setStyleSheet(self.get_button_style("#d35400"))
        effects_buttons_layout.addWidget(sepia_btn)
        
        effects_layout.addLayout(effects_buttons_layout)
        
        effects_group.setLayout(effects_layout)
        layout.addWidget(effects_group)
        
    def create_log_section(self, layout):
        """
        ログセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        self.log_display = QTextEdit()
        self.log_display.setMaximumHeight(120)
        self.log_display.setPlaceholderText("操作ログがここに表示されます...")
        self.log_display.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 5px;
                font-family: 'Courier New', monospace;
                font-size: 10px;
            }
        """)
        layout.addWidget(self.log_display)
        
    def create_image_display_area(self, layout):
        """
        画像表示エリアの作成
        
        Args:
            layout (QHBoxLayout): 追加先のレイアウト
        """
        # スクロールエリアで囲む
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: #ffffff;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
            }
        """)
        
        # 画像表示ラベル
        self.image_label = QLabel("画像が表示されます")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: #ecf0f1;
                color: #7f8c8d;
                font-size: 16px;
                padding: 50px;
                border-radius: 5px;
            }
        """)
        self.image_label.setMinimumSize(400, 400)
        
        scroll_area.setWidget(self.image_label)
        layout.addWidget(scroll_area)
        
    def get_button_style(self, color: str) -> str:
        """
        ボタンスタイルの取得
        
        Args:
            color (str): ボタンの色
            
        Returns:
            str: スタイルシート
        """
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {color}dd;
            }}
        """
        
    def log_action(self, message: str):
        """
        アクションをログに記録
        
        Args:
            message (str): ログメッセージ
        """
        self.log_display.append(f"[{self.__class__.__name__}] {message}")
        
    def create_sample_images(self):
        """
        サンプル画像の作成
        """
        # 初期画像として簡単なグラデーションを作成
        self.create_gradient_image()
        
    def create_gradient_image(self):
        """
        グラデーション画像の作成
        """
        pixmap = QPixmap(300, 200)
        painter = QPainter(pixmap)
        
        # グラデーション作成
        for i in range(300):
            ratio = i / 300.0
            color = QColor()
            color.setHsv(int(240 * ratio), 200, 255)  # 青から赤へのグラデーション
            painter.setPen(QPen(color, 1))
            painter.drawLine(i, 0, i, 200)
            
        painter.end()
        
        self.original_pixmap = pixmap
        self.current_pixmap = pixmap.copy()
        self.image_label.setPixmap(pixmap)
        self.log_action("グラデーション画像を作成しました")
        
    def create_pattern_image(self):
        """
        パターン画像の作成
        """
        pixmap = QPixmap(300, 200)
        pixmap.fill(Qt.GlobalColor.white)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # チェッカーボードパターン
        checker_size = 20
        for row in range(0, 200, checker_size):
            for col in range(0, 300, checker_size):
                if (row // checker_size + col // checker_size) % 2 == 0:
                    painter.fillRect(col, row, checker_size, checker_size, QColor("#3498db"))
                else:
                    painter.fillRect(col, row, checker_size, checker_size, QColor("#e74c3c"))
                    
        # 円形パターンを重ねる
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Multiply)
        painter.setBrush(QBrush(QColor(255, 255, 0, 100)))
        painter.setPen(Qt.PenStyle.NoPen)
        
        for i in range(5):
            x = 50 + i * 50
            y = 50 + (i % 2) * 100
            painter.drawEllipse(x - 30, y - 30, 60, 60)
            
        painter.end()
        
        self.original_pixmap = pixmap
        self.current_pixmap = pixmap.copy()
        self.image_label.setPixmap(pixmap)
        self.log_action("チェッカーボードパターンを作成しました")
        
    def create_chart_image(self):
        """
        簡単なチャート画像の作成
        """
        pixmap = QPixmap(400, 300)
        pixmap.fill(Qt.GlobalColor.white)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 背景
        painter.fillRect(50, 50, 300, 200, QColor("#f8f9fa"))
        
        # グリッド線
        painter.setPen(QPen(QColor("#dee2e6"), 1))
        for i in range(6):
            y = 50 + i * 40
            painter.drawLine(50, y, 350, y)
        for i in range(7):
            x = 50 + i * 50
            painter.drawLine(x, 50, x, 250)
            
        # データ描画
        data = [30, 80, 45, 90, 65, 120]
        painter.setPen(QPen(QColor("#3498db"), 3))
        
        for i in range(len(data) - 1):
            x1 = 50 + i * 50
            y1 = 250 - data[i]
            x2 = 50 + (i + 1) * 50
            y2 = 250 - data[i + 1]
            painter.drawLine(x1, y1, x2, y2)
            
        # データポイント
        painter.setBrush(QBrush(QColor("#e74c3c")))
        for i, value in enumerate(data):
            x = 50 + i * 50
            y = 250 - value
            painter.drawEllipse(x - 4, y - 4, 8, 8)
            
        # タイトル
        painter.setPen(QPen(QColor("#2c3e50"), 2))
        painter.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        painter.drawText(150, 30, "サンプルチャート")
        
        painter.end()
        
        self.original_pixmap = pixmap
        self.current_pixmap = pixmap.copy()
        self.image_label.setPixmap(pixmap)
        self.log_action("チャート画像を作成しました")
        
    def create_custom_icon(self):
        """
        カスタムアイコンの作成
        """
        # 複数サイズのアイコンを作成
        icon = QIcon()
        
        for size in [16, 24, 32, 48, 64]:
            pixmap = QPixmap(size, size)
            pixmap.fill(Qt.GlobalColor.transparent)
            
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            # 背景円
            painter.setBrush(QBrush(QColor("#3498db")))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(1, 1, size - 2, size - 2)
            
            # 星型を描画
            painter.setBrush(QBrush(QColor("#ffffff")))
            star_size = size * 0.6
            center = size / 2
            
            # 簡単な星型（5つの三角形）
            for i in range(5):
                angle = i * 72 * 3.14159 / 180
                outer_x = center + (star_size / 2) * 0.8 * math.cos(angle)
                outer_y = center + (star_size / 2) * 0.8 * math.sin(angle)
                
                inner_angle = (i + 0.5) * 72 * 3.14159 / 180
                inner_x = center + (star_size / 2) * 0.3 * math.cos(inner_angle)
                inner_y = center + (star_size / 2) * 0.3 * math.sin(inner_angle)
                
                # 簡略化して中央から線を引く
                painter.setPen(QPen(QColor("#ffffff"), max(1, size // 16)))
                painter.drawLine(int(center), int(center), int(outer_x), int(outer_y))
                
            painter.end()
            icon.addPixmap(pixmap)
            
        # アイコンを表示用画像として使用
        display_pixmap = icon.pixmap(QSize(128, 128))
        self.original_pixmap = display_pixmap
        self.current_pixmap = display_pixmap.copy()
        self.image_label.setPixmap(display_pixmap)
        self.log_action("カスタムアイコンを作成しました（複数サイズ対応）")
        
    def cos(self, angle):
        """簡易cos関数"""
        return math.cos(angle)
        
    def sin(self, angle):
        """簡易sin関数"""
        return math.sin(angle)
        
    def apply_transformations(self):
        """
        変形の適用
        """
        if not self.original_pixmap:
            return
            
        scale = self.scale_slider.value() / 100.0
        rotation = self.rotation_slider.value()
        
        # スケールラベル更新
        self.scale_label.setText(f"{int(scale * 100)}%")
        self.rotation_label.setText(f"{rotation}°")
        
        # 変形の適用
        transform = QTransform()
        transform.scale(scale, scale)
        transform.rotate(rotation)
        
        self.current_pixmap = self.original_pixmap.transformed(transform, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(self.current_pixmap)
        
        self.log_action(f"変形を適用: スケール{int(scale * 100)}%, 回転{rotation}°")
        
    def flip_horizontal(self):
        """
        水平反転
        """
        if not self.current_pixmap:
            return
            
        transform = QTransform()
        transform.scale(-1, 1)
        self.current_pixmap = self.current_pixmap.transformed(transform)
        self.image_label.setPixmap(self.current_pixmap)
        self.log_action("水平反転を適用しました")
        
    def flip_vertical(self):
        """
        垂直反転
        """
        if not self.current_pixmap:
            return
            
        transform = QTransform()
        transform.scale(1, -1)
        self.current_pixmap = self.current_pixmap.transformed(transform)
        self.image_label.setPixmap(self.current_pixmap)
        self.log_action("垂直反転を適用しました")
        
    def reset_transformations(self):
        """
        変形のリセット
        """
        if not self.original_pixmap:
            return
            
        self.scale_slider.setValue(100)
        self.rotation_slider.setValue(0)
        self.opacity_slider.setValue(100)
        self.current_pixmap = self.original_pixmap.copy()
        self.image_label.setPixmap(self.current_pixmap)
        self.log_action("すべての変形をリセットしました")
        
    def apply_opacity(self):
        """
        透明度の適用
        """
        if not self.current_pixmap:
            return
            
        opacity = self.opacity_slider.value()
        self.opacity_label.setText(f"{opacity}%")
        
        # 透明度の適用（簡易版）
        if opacity < 100:
            temp_pixmap = QPixmap(self.current_pixmap.size())
            temp_pixmap.fill(Qt.GlobalColor.transparent)
            
            painter = QPainter(temp_pixmap)
            painter.setOpacity(opacity / 100.0)
            painter.drawPixmap(0, 0, self.current_pixmap)
            painter.end()
            
            self.image_label.setPixmap(temp_pixmap)
        else:
            self.image_label.setPixmap(self.current_pixmap)
            
        self.log_action(f"透明度を{opacity}%に設定しました")
        
    def apply_grayscale(self):
        """
        グレースケール効果の適用
        """
        if not self.original_pixmap:
            return
            
        grayscale_pixmap = QPixmap(self.original_pixmap.size())
        grayscale_pixmap.fill(Qt.GlobalColor.white)
        
        painter = QPainter(grayscale_pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        
        # グレースケール変換（簡易版）
        for y in range(self.original_pixmap.height()):
            for x in range(self.original_pixmap.width()):
                color = self.original_pixmap.toImage().pixelColor(x, y)
                gray = int(0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue())
                gray_color = QColor(gray, gray, gray)
                painter.setPen(gray_color)
                painter.drawPoint(x, y)
                
        painter.end()
        
        self.current_pixmap = grayscale_pixmap
        self.image_label.setPixmap(self.current_pixmap)
        self.log_action("グレースケール効果を適用しました")
        
    def apply_sepia(self):
        """
        セピア効果の適用
        """
        if not self.original_pixmap:
            return
            
        sepia_pixmap = QPixmap(self.original_pixmap.size())
        painter = QPainter(sepia_pixmap)
        painter.drawPixmap(0, 0, self.original_pixmap)
        
        # セピアオーバーレイ
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Multiply)
        painter.fillRect(sepia_pixmap.rect(), QColor(222, 184, 135, 100))
        
        painter.end()
        
        self.current_pixmap = sepia_pixmap
        self.image_label.setPixmap(self.current_pixmap)
        self.log_action("セピア効果を適用しました")
        
    def update_icon_display(self):
        """
        アイコン表示の更新
        """
        size_text = self.icon_size_combo.currentText()
        size = int(size_text.split('x')[0])
        
        self.log_action(f"アイコンサイズを{size_text}に変更しました")
        
    def show_system_icons(self):
        """
        システムアイコンの表示
        """
        # システムアイコンのデモを作成
        pixmap = QPixmap(300, 200)
        pixmap.fill(Qt.GlobalColor.white)
        
        painter = QPainter(pixmap)
        painter.setFont(QFont("Arial", 12))
        painter.drawText(10, 20, "システムアイコンの例:")
        painter.drawText(10, 50, "• QStyle::SP_ComputerIcon")
        painter.drawText(10, 80, "• QStyle::SP_FileIcon") 
        painter.drawText(10, 110, "• QStyle::SP_MessageBoxWarning")
        painter.drawText(10, 140, "• QStyle::SP_DialogOkButton")
        painter.drawText(10, 170, "実際のアプリでは QStyle から取得")
        painter.end()
        
        self.current_pixmap = pixmap
        self.image_label.setPixmap(pixmap)
        self.log_action("システムアイコンの一覧を表示しました")
        
    def create_multi_size_icon(self):
        """
        マルチサイズアイコンのデモ
        """
        pixmap = QPixmap(400, 300)
        pixmap.fill(Qt.GlobalColor.white)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 異なるサイズのアイコンを表示
        sizes = [16, 24, 32, 48, 64]
        x_pos = 50
        
        for size in sizes:
            # 簡単なアイコンを描画
            painter.setBrush(QBrush(QColor("#3498db")))
            painter.setPen(QPen(QColor("#2980b9"), 2))
            painter.drawRoundedRect(x_pos, 100, size, size, size//4, size//4)
            
            # サイズラベル
            painter.setPen(QPen(QColor("#2c3e50"), 1))
            painter.setFont(QFont("Arial", 10))
            painter.drawText(x_pos, 90, f"{size}px")
            
            x_pos += size + 20
            
        # タイトル
        painter.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        painter.drawText(50, 30, "マルチサイズアイコンの例")
        painter.setFont(QFont("Arial", 10))
        painter.drawText(50, 50, "同じアイコンを異なるサイズで使用")
        
        painter.end()
        
        self.current_pixmap = pixmap
        self.image_label.setPixmap(pixmap)
        self.log_action("マルチサイズアイコンのデモを表示しました")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QPixmapとQIconの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = PixmapIconDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 