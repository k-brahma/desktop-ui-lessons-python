"""
QColor基本サンプル - 基本的な色の作成

このモジュールは、PySide6のQColorクラスの基本的な色の作成方法を示します。
RGB値、16進数、色名からの色の作成方法を実演します。

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class BasicColorWindow(QWidget):
    """基本的な色の作成方法を示すウィンドウクラス"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """UIの初期化"""
        self.setWindowTitle("QColor基本サンプル - 色の作成")
        self.setGeometry(200, 200, 600, 400)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # タイトル
        title_label = QLabel("QColor 基本的な色の作成")
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
        
        # 基本色グループ
        basic_group = QGroupBox("色の作成方法")
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
        main_layout.addWidget(basic_group)
        
        # 説明テキスト
        info_label = QLabel("""
色の作成方法:

# RGB値から
color = QColor(255, 0, 0)

# 16進数から  
color = QColor("#FF0000")

# 色名から
color = QColor("red")
        """)
        info_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Courier New', monospace;
            }
        """)
        main_layout.addWidget(info_label)
        
    def create_color_sample(self, color, text):
        """色サンプルウィジェットの作成"""
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


def main():
    """アプリケーションのメインエントリーポイント"""
    app = QApplication(sys.argv)
    window = BasicColorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()