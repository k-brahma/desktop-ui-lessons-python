"""
QApplication基本サンプル2 - ラベル付きウィンドウ
=========================================

このモジュールは、PySide6のQApplicationクラスを使用した、
ラベルを含む基本的なウィンドウの実装例を示します。

学習ポイント
----------

- QApplicationインスタンスの作成
- ウィンドウの表示
- ラベルの追加と配置
- イベントループの開始と終了
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class LabelWindow(QWidget):
    """ラベル付きウィンドウクラス
    
    QWidgetを継承し、ラベルを含むシンプルなウィンドウを作成します。
    """
    
    def __init__(self):
        """LabelWindowクラスのコンストラクタ
        
        ウィンドウのタイトル、サイズ、ラベルを設定します。
        """
        super().__init__()
        self.setWindowTitle("ラベル付きウィンドウ")
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
    window = LabelWindow()
    
    # 3. ウィンドウを表示
    window.show()
    
    # 4. イベントループを開始し、アプリケーションの終了コードで終了
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 