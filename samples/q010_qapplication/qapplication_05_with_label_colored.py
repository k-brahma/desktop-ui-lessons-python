"""
QApplication基本サンプル4 - カラーテーマ付きウィンドウ
=========================================

このモジュールは、PySide6のQApplicationクラスを使用した、
カラーテーマを適用したウィンドウの実装例を示します。

学習ポイント
----------

- QApplicationインスタンスの作成
- ウィンドウの表示
- ラベルの追加と配置
- カラーテーマの適用
- イベントループの開始と終了
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class ColoredWindow(QWidget):
    """カラーテーマ付きウィンドウクラス
    
    QWidgetを継承し、カラーテーマを適用したウィンドウを作成します。
    
    :param theme: 適用するテーマ（'light' または 'dark'）
    :type theme: str
    """
    
    def __init__(self, theme="light"):
        """ColoredWindowクラスのコンストラクタ
        
        ウィンドウのタイトル、サイズ、ラベル、カラーテーマを設定します。
        
        :param theme: 適用するテーマ（'light' または 'dark'）
        :type theme: str
        """
        super().__init__()
        self.setWindowTitle("カラーテーマ付きウィンドウ")
        self.setGeometry(300, 300, 400, 300)  # ウィンドウサイズを大きく
        
        # レイアウトの作成
        layout = QVBoxLayout()
        
        # ラベルの作成と設定
        label = QLabel("こんにちは、PySide6!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 中央揃え
        
        # フォントの設定
        font = QFont()
        font.setPointSize(24)  # フォントサイズを24ptに
        font.setBold(True)     # 太字に
        label.setFont(font)
        
        # ラベルをレイアウトに追加
        layout.addWidget(label)
        
        # レイアウトをウィンドウに設定
        self.setLayout(layout)

        # テーマに応じたパレットを設定
        palette = self.palette()
        if theme == "dark":
            palette.setColor(QPalette.ColorRole.Window, QColor(43, 43, 43))  # 背景色
            palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))  # 文字色
        else:  # light theme
            palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))  # 背景色
            palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))  # 文字色
        
        self.setPalette(palette)


def main():
    """アプリケーションのメインエントリーポイント
    
    QApplicationの基本的なライフサイクルを示します:
    1. QApplicationインスタンスの作成
    2. ウィンドウの作成と表示
    3. イベントループの開始
    4. アプリケーションの終了
    """
    # 1. QApplicationインスタンスを作成
    app = QApplication(sys.argv)
    
    # 2. ウィンドウを作成
    window = ColoredWindow(theme="dark")
    
    # 3. ウィンドウを表示
    window.show()
    
    # 4. イベントループを開始し、アプリケーションの終了コードで終了
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 