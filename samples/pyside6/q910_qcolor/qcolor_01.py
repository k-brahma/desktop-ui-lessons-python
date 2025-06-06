"""
QColor基本サンプル - 色の定義と操作

このモジュールは、PySide6のQColorクラスの基本的な使用方法を示します。
QColorは色を表現し操作するためのクラスで、様々な色空間をサポートします。

主要な学習ポイント:
- 色の作成方法（RGB、16進数、色名）
- 色空間の変換（RGB、HSV）
- スタイルシートでの色の使用
- よく使用される色パレット

"""

import sys

from PySide6.QtCore import Qt
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


class ColorDemoWindow(QWidget):
    """
    QColorの使用例を示すウィンドウクラス
    
    様々な色の作成方法と操作を実演します。
    """
    
    def __init__(self):
        """
        ColorDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とカラーサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQColorの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QColor基本サンプル - 色の定義と操作")
        self.setGeometry(200, 200, 700, 600)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_title_section(main_layout)
        self.create_basic_colors_section(main_layout)
        self.create_rgb_controls_section(main_layout)
        self.create_palette_section(main_layout)
        self.create_demo_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QColor デモンストレーション")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                background-color: #ecf0f1;
                padding: 15px;
                border-radius: 8px;
                border: 2px solid #bdc3c7;
                margin-bottom: 15px;
            }
        """)
        layout.addWidget(title_label)
        
    def create_basic_colors_section(self, layout):
        """
        基本色セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 基本色グループ
        basic_group = QGroupBox("基本的な色の作成")
        basic_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #3498db;
                border-radius: 8px;
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
        
        basic_layout = QVBoxLayout()
        
        # RGB値からの作成例
        rgb_row = QHBoxLayout()
        rgb_colors = [
            (QColor(255, 0, 0), "赤 RGB(255,0,0)"),
            (QColor(0, 255, 0), "緑 RGB(0,255,0)"),
            (QColor(0, 0, 255), "青 RGB(0,0,255)"),
            (QColor(255, 255, 0), "黄 RGB(255,255,0)")
        ]
        
        for color, text in rgb_colors:
            color_widget = self.create_color_sample(color, text)
            rgb_row.addWidget(color_widget)
            
        basic_layout.addLayout(rgb_row)
        
        # 16進数からの作成例
        hex_row = QHBoxLayout()
        hex_colors = [
            (QColor("#FF6B6B"), "#FF6B6B"),
            (QColor("#4ECDC4"), "#4ECDC4"),
            (QColor("#45B7D1"), "#45B7D1"),
            (QColor("#96CEB4"), "#96CEB4")
        ]
        
        for color, text in hex_colors:
            color_widget = self.create_color_sample(color, text)
            hex_row.addWidget(color_widget)
            
        basic_layout.addLayout(hex_row)
        
        # 色名からの作成例
        name_row = QHBoxLayout()
        name_colors = [
            (QColor("red"), "red"),
            (QColor("blue"), "blue"),
            (QColor("green"), "green"),
            (QColor("orange"), "orange")
        ]
        
        for color, text in name_colors:
            color_widget = self.create_color_sample(color, text)
            name_row.addWidget(color_widget)
            
        basic_layout.addLayout(name_row)
        
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
    def create_rgb_controls_section(self, layout):
        """
        RGB制御セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # RGB制御グループ
        rgb_group = QGroupBox("RGB値の制御")
        rgb_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #e74c3c;
                border-radius: 8px;
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
        
        rgb_layout = QVBoxLayout()
        
        # RGB スライダー
        controls_layout = QHBoxLayout()
        
        # R値制御
        r_layout = QVBoxLayout()
        r_layout.addWidget(QLabel("Red"))
        self.r_slider = QSlider(Qt.Orientation.Vertical)
        self.r_slider.setRange(0, 255)
        self.r_slider.setValue(128)
        self.r_slider.valueChanged.connect(self.update_rgb_color)
        r_layout.addWidget(self.r_slider)
        self.r_spinbox = QSpinBox()
        self.r_spinbox.setRange(0, 255)
        self.r_spinbox.setValue(128)
        self.r_spinbox.valueChanged.connect(self.update_rgb_from_spinbox)
        r_layout.addWidget(self.r_spinbox)
        controls_layout.addLayout(r_layout)
        
        # G値制御
        g_layout = QVBoxLayout()
        g_layout.addWidget(QLabel("Green"))
        self.g_slider = QSlider(Qt.Orientation.Vertical)
        self.g_slider.setRange(0, 255)
        self.g_slider.setValue(128)
        self.g_slider.valueChanged.connect(self.update_rgb_color)
        g_layout.addWidget(self.g_slider)
        self.g_spinbox = QSpinBox()
        self.g_spinbox.setRange(0, 255)
        self.g_spinbox.setValue(128)
        self.g_spinbox.valueChanged.connect(self.update_rgb_from_spinbox)
        g_layout.addWidget(self.g_spinbox)
        controls_layout.addLayout(g_layout)
        
        # B値制御
        b_layout = QVBoxLayout()
        b_layout.addWidget(QLabel("Blue"))
        self.b_slider = QSlider(Qt.Orientation.Vertical)
        self.b_slider.setRange(0, 255)
        self.b_slider.setValue(128)
        self.b_slider.valueChanged.connect(self.update_rgb_color)
        b_layout.addWidget(self.b_slider)
        self.b_spinbox = QSpinBox()
        self.b_spinbox.setRange(0, 255)
        self.b_spinbox.setValue(128)
        self.b_spinbox.valueChanged.connect(self.update_rgb_from_spinbox)
        b_layout.addWidget(self.b_spinbox)
        controls_layout.addLayout(b_layout)
        
        # 結果表示
        result_layout = QVBoxLayout()
        self.color_display = QLabel("Color Preview")
        self.color_display.setMinimumSize(150, 100)
        self.color_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.color_display.setStyleSheet("border: 2px solid black; background-color: rgb(128, 128, 128);")
        result_layout.addWidget(self.color_display)
        
        self.color_info = QLabel("RGB(128, 128, 128)\n#808080")
        self.color_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_layout.addWidget(self.color_info)
        
        controls_layout.addLayout(result_layout)
        
        rgb_layout.addLayout(controls_layout)
        rgb_group.setLayout(rgb_layout)
        layout.addWidget(rgb_group)
        
    def create_palette_section(self, layout):
        """
        パレットセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # パレットグループ
        palette_group = QGroupBox("Material Design 色パレット")
        palette_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #9b59b6;
                border-radius: 8px;
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
        
        palette_layout = QVBoxLayout()
        
        # Material Design カラーパレット
        material_colors = [
            [QColor("#F44336"), QColor("#E91E63"), QColor("#9C27B0"), QColor("#673AB7")],
            [QColor("#3F51B5"), QColor("#2196F3"), QColor("#03A9F4"), QColor("#00BCD4")],
            [QColor("#009688"), QColor("#4CAF50"), QColor("#8BC34A"), QColor("#CDDC39")],
            [QColor("#FFEB3B"), QColor("#FFC107"), QColor("#FF9800"), QColor("#FF5722")]
        ]
        
        for row_colors in material_colors:
            row_layout = QHBoxLayout()
            for color in row_colors:
                color_widget = self.create_color_sample(color, color.name())
                row_layout.addWidget(color_widget)
            palette_layout.addLayout(row_layout)
            
        palette_group.setLayout(palette_layout)
        layout.addWidget(palette_group)
        
    def create_demo_section(self, layout):
        """
        デモセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # デモグループ
        demo_group = QGroupBox("色の実用例")
        demo_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #27ae60;
                border-radius: 8px;
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
        
        demo_layout = QHBoxLayout()
        
        # テーマ切り替えボタン
        theme_layout = QVBoxLayout()
        
        self.light_btn = QPushButton("ライトテーマ")
        self.light_btn.clicked.connect(self.apply_light_theme)
        self.light_btn.setStyleSheet("""
            QPushButton {
                background-color: #ecf0f1;
                color: #2c3e50;
                border: 2px solid #bdc3c7;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d5dbdb;
            }
        """)
        theme_layout.addWidget(self.light_btn)
        
        self.dark_btn = QPushButton("ダークテーマ")
        self.dark_btn.clicked.connect(self.apply_dark_theme)
        self.dark_btn.setStyleSheet("""
            QPushButton {
                background-color: #34495e;
                color: #ecf0f1;
                border: 2px solid #5d6d7e;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5d6d7e;
            }
        """)
        theme_layout.addWidget(self.dark_btn)
        
        demo_layout.addLayout(theme_layout)
        
        # 色情報表示
        info_layout = QVBoxLayout()
        self.demo_info = QLabel("""
色の作成方法:

# RGB値から
color = QColor(255, 0, 0)

# 16進数から  
color = QColor("#FF0000")

# 色名から
color = QColor("red")

# HSV値から
color = QColor()
color.setHsv(0, 255, 255)
        """)
        self.demo_info.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Courier New', monospace;
            }
        """)
        info_layout.addWidget(self.demo_info)
        
        demo_layout.addLayout(info_layout)
        demo_group.setLayout(demo_layout)
        layout.addWidget(demo_group)
        
    def create_color_sample(self, color, text):
        """
        色サンプルウィジェットの作成
        
        Args:
            color (QColor): 表示する色
            text (str): 表示するテキスト
            
        Returns:
            QWidget: 色サンプルウィジェット
        """
        widget = QWidget()
        widget.setFixedSize(80, 60)
        
        # 色に基づいてテキストの色を決定
        luminance = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
        text_color = "white" if luminance < 0.5 else "black"
        
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {color.name()};
                border: 1px solid #333;
                border-radius: 4px;
            }}
        """)
        
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(f"color: {text_color}; font-size: 10px; font-weight: bold;")
        label.setWordWrap(True)
        layout.addWidget(label)
        widget.setLayout(layout)
        
        return widget
        
    def update_rgb_color(self):
        """
        RGB値の変更に基づいて色を更新
        """
        r = self.r_slider.value()
        g = self.g_slider.value() 
        b = self.b_slider.value()
        
        # スピンボックスを同期
        self.r_spinbox.setValue(r)
        self.g_spinbox.setValue(g)
        self.b_spinbox.setValue(b)
        
        self.update_color_display(r, g, b)
        
    def update_rgb_from_spinbox(self):
        """
        スピンボックスの変更に基づいて色を更新
        """
        r = self.r_spinbox.value()
        g = self.g_spinbox.value()
        b = self.b_spinbox.value()
        
        # スライダーを同期
        self.r_slider.setValue(r)
        self.g_slider.setValue(g)
        self.b_slider.setValue(b)
        
        self.update_color_display(r, g, b)
        
    def update_color_display(self, r, g, b):
        """
        色表示の更新
        
        Args:
            r (int): 赤成分
            g (int): 緑成分
            b (int): 青成分
        """
        color = QColor(r, g, b)
        
        # 背景色を更新
        self.color_display.setStyleSheet(f"""
            QLabel {{
                border: 2px solid black;
                background-color: rgb({r}, {g}, {b});
                color: {'white' if (0.299 * r + 0.587 * g + 0.114 * b) < 128 else 'black'};
                font-weight: bold;
            }}
        """)
        
        # 色情報を更新
        self.color_info.setText(f"RGB({r}, {g}, {b})\n{color.name().upper()}")
        
    def apply_light_theme(self):
        """
        ライトテーマの適用
        """
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                color: #2c3e50;
            }
            QGroupBox {
                background-color: #f8f9fa;
            }
        """)
        
    def apply_dark_theme(self):
        """
        ダークテーマの適用
        """
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
            }
            QGroupBox {
                background-color: #34495e;
            }
        """)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QColorの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = ColorDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 