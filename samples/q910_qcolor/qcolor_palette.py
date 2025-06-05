"""
QColor基本サンプル - カラーパレットとテーマ

このモジュールは、PySide6のQColorクラスを使用したカラーパレットとテーマ切り替えを示します。
Material Designカラーパレットの表示と、ライト/ダークテーマの切り替えを実演します。

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class PaletteWindow(QWidget):
    """カラーパレットとテーマを示すウィンドウクラス"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """UIの初期化"""
        self.setWindowTitle("QColor基本サンプル - カラーパレットとテーマ")
        self.setGeometry(200, 200, 600, 400)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # タイトル
        title_label = QLabel("Material Design カラーパレット")
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
        
        # パレットグループ
        palette_group = QGroupBox("カラーパレット")
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
        main_layout.addWidget(palette_group)
        
        # テーマ切り替えボタン
        theme_group = QGroupBox("テーマ切り替え")
        theme_group.setStyleSheet("""
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
            }
        """)
        
        theme_layout = QHBoxLayout()
        
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
        
        theme_group.setLayout(theme_layout)
        main_layout.addWidget(theme_group)
        
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
        
    def apply_light_theme(self):
        """ライトテーマの適用"""
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
        """ダークテーマの適用"""
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
    """アプリケーションのメインエントリーポイント"""
    app = QApplication(sys.argv)
    window = PaletteWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 