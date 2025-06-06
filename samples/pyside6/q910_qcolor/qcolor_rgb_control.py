"""
QColor基本サンプル - RGB値の制御

このモジュールは、PySide6のQColorクラスのRGB値制御機能を示します。
スライダーとスピンボックスを使用してRGB値を調整し、色を作成する方法を実演します。

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class RGBControlWindow(QWidget):
    """RGB値制御を示すウィンドウクラス"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """UIの初期化"""
        self.setWindowTitle("QColor基本サンプル - RGB値の制御")
        self.setGeometry(200, 200, 500, 400)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # タイトル
        title_label = QLabel("RGB値の制御")
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
        main_layout.addWidget(title_label)
        
        # RGB制御グループ
        rgb_group = QGroupBox("RGB値の調整")
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
            }
        """)
        
        rgb_layout = QHBoxLayout()
        
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
        rgb_layout.addLayout(r_layout)
        
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
        rgb_layout.addLayout(g_layout)
        
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
        rgb_layout.addLayout(b_layout)
        
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
        
        rgb_layout.addLayout(result_layout)
        
        rgb_group.setLayout(rgb_layout)
        main_layout.addWidget(rgb_group)
        
    def update_rgb_color(self):
        """RGB値の変更に基づいて色を更新"""
        r = self.r_slider.value()
        g = self.g_slider.value()
        b = self.b_slider.value()
        
        # スピンボックスを同期
        self.r_spinbox.setValue(r)
        self.g_spinbox.setValue(g)
        self.b_spinbox.setValue(b)
        
        self.update_color_display(r, g, b)
        
    def update_rgb_from_spinbox(self):
        """スピンボックスの変更に基づいて色を更新"""
        r = self.r_spinbox.value()
        g = self.g_spinbox.value()
        b = self.b_spinbox.value()
        
        # スライダーを同期
        self.r_slider.setValue(r)
        self.g_slider.setValue(g)
        self.b_slider.setValue(b)
        
        self.update_color_display(r, g, b)
        
    def update_color_display(self, r, g, b):
        """色表示の更新"""
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


def main():
    """アプリケーションのメインエントリーポイント"""
    app = QApplication(sys.argv)
    window = RGBControlWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  