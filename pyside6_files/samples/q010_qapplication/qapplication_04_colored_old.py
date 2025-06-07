"""
QApplication基本サンプル2 - テーマ対応ウィンドウ
=========================================

このモジュールは、PySide6のQApplicationクラスを使用した、
テーマ設定可能なウィンドウの実装例を示します。

学習ポイント
----------

- テーマパラメータを受け取るウィンドウクラスの実装
- QPaletteを使用したテーマ適用
- ウィンドウのカスタマイズ
"""

import sys

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QWidget


class ThemedWindow(QWidget):
    """テーマ対応ウィンドウクラス
    
    QWidgetを継承し、テーマパラメータを受け取って
    スタイルを適用できるウィンドウを作成します。
    
    :param theme: 適用するテーマ（'light' または 'dark'）
    :type theme: str
    """
    
    def __init__(self, theme="light"):
        """ThemedWindowクラスのコンストラクタ
        
        :param theme: 適用するテーマ（'light' または 'dark'）
        :type theme: str
        """
        super().__init__()
        self.setWindowTitle("テーマ対応ウィンドウ")
        self.setGeometry(300, 300, 400, 300)
        
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
    
    アプリケーションを初期化し、テーマ付きウィンドウを表示します。
    """
    app = QApplication(sys.argv)
    
    # テーマを指定してウィンドウを作成
    window = ThemedWindow(theme="dark")
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 