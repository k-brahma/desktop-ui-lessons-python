"""
QLabel基本サンプル - テキストラベルの基本機能

このモジュールは、PySide6のQLabelクラスの基本的な使用方法を示します。
QLabelは、読み取り専用のテキストや画像を表示するためのウィジェットです。

主要な学習ポイント:
- 基本的なテキスト表示
- フォントとスタイルの設定
- 配置（アライメント）の設定
- 基本的なレイアウトでの使用

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class BasicLabelWindow(QWidget):
    """
    基本的なQLabelの使用例を示すウィンドウクラス
    
    様々なスタイルと設定のQLabelを配置したウィンドウを作成します。
    """
    
    def __init__(self):
        """
        BasicLabelWindowクラスのコンストラクタ
        
        ウィンドウの初期設定と各種ラベルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        ウィンドウのレイアウトと各種QLabelの設定を行います。
        """
        self.setWindowTitle("QLabel基本サンプル")
        self.setGeometry(200, 200, 500, 400)
        
        # メインレイアウト
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 基本的なラベルの作成
        self.create_basic_labels(layout)
        
    def create_basic_labels(self, layout):
        """
        基本的なラベルの作成と設定
        
        Args:
            layout (QVBoxLayout): ラベルを追加するレイアウト
        """
        # 1. シンプルなテキストラベル
        simple_label = QLabel("これはシンプルなQLabelです")
        layout.addWidget(simple_label)
        
        # 2. 太字のラベル
        bold_label = QLabel("これは太字のテキストです")
        bold_font = QFont()
        bold_font.setBold(True)
        bold_font.setPointSize(12)
        bold_label.setFont(bold_font)
        layout.addWidget(bold_label)
        
        # 3. 中央揃えのラベル
        center_label = QLabel("中央揃えのテキスト")
        center_label.setAlignment(Qt.AlignCenter)
        center_label.setStyleSheet("""
            QLabel {
                background-color: #e3f2fd;
                padding: 10px;
                border: 1px solid #2196f3;
                border-radius: 5px;
            }
        """)
        layout.addWidget(center_label)
        
        # 4. 右揃えのラベル
        right_label = QLabel("右揃えのテキスト")
        right_label.setAlignment(Qt.AlignRight)
        right_label.setStyleSheet("""
            QLabel {
                background-color: #f3e5f5;
                padding: 10px;
                border: 1px solid #9c27b0;
                border-radius: 5px;
            }
        """)
        layout.addWidget(right_label)
        
        # 5. カスタムフォントのラベル
        custom_font_label = QLabel("カスタムフォントのラベル")
        custom_font = QFont("Arial", 14)
        custom_font.setItalic(True)
        custom_font_label.setFont(custom_font)
        custom_font_label.setStyleSheet("""
            QLabel {
                color: #4caf50;
                background-color: #e8f5e8;
                padding: 8px;
                border-left: 4px solid #4caf50;
            }
        """)
        layout.addWidget(custom_font_label)
        
        # 6. 複数行テキストのラベル
        multiline_label = QLabel(
            "これは複数行のテキストを表示するラベルです。\n"
            "改行文字を使って複数行にできます。\n"
            "長いテキストも表示可能です。"
        )
        multiline_label.setWordWrap(True)  # 単語で折り返し
        multiline_label.setAlignment(Qt.AlignTop)
        multiline_label.setStyleSheet("""
            QLabel {
                background-color: #fff3e0;
                padding: 15px;
                border: 1px solid #ff9800;
                border-radius: 8px;
                line-height: 1.5;
            }
        """)
        layout.addWidget(multiline_label)
        
        # 7. インタラクティブなラベル（選択可能）
        selectable_label = QLabel("このテキストは選択可能です（マウスでドラッグしてみてください）")
        selectable_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        selectable_label.setStyleSheet("""
            QLabel {
                background-color: #fce4ec;
                padding: 12px;
                border: 1px solid #e91e63;
                border-radius: 6px;
            }
        """)
        layout.addWidget(selectable_label)
        
        # 8. 固定サイズのラベル
        fixed_size_label = QLabel("固定サイズ (200x50)")
        fixed_size_label.setFixedSize(200, 50)
        fixed_size_label.setAlignment(Qt.AlignCenter)
        fixed_size_label.setStyleSheet("""
            QLabel {
                background-color: #e0f2f1;
                border: 2px solid #009688;
                border-radius: 10px;
                font-weight: bold;
            }
        """)
        layout.addWidget(fixed_size_label)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QLabelの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = BasicLabelWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 