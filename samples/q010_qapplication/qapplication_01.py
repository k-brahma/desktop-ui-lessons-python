"""
QApplication基本サンプル - アプリケーションの基本構造

このモジュールは、PySide6のQApplicationクラスの最も基本的な使用方法を示します。
すべてのPySide6 GUIアプリケーションには1つのQApplicationインスタンスが必要です。

主要な学習ポイント:
- QApplicationインスタンスの作成
- ウィンドウの表示
- イベントループの開始と終了
- アプリケーションの適切な終了処理

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtWidgets import QApplication, QWidget


class SimpleWindow(QWidget):
    """
    最小限のウィンドウクラス
    
    QWidgetを継承したシンプルなウィンドウを作成します。
    このクラスは基本的なウィンドウ表示のみを行います。
    """
    
    def __init__(self):
        """
        SimpleWindowクラスのコンストラクタ
        
        ウィンドウのタイトルとサイズを設定します。
        """
        super().__init__()
        self.setWindowTitle("QApplication基本サンプル")
        self.setGeometry(300, 300, 300, 200)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QApplicationの基本的なライフサイクルを示します:
    1. QApplicationインスタンスの作成
    2. ウィンドウの作成と表示
    3. イベントループの開始
    4. アプリケーションの終了
    """
    # 1. QApplicationインスタンスを作成
    # sys.argvを渡すことで、コマンドライン引数を処理できる
    app = QApplication(sys.argv)
    
    # 2. ウィンドウを作成
    window = SimpleWindow()
    
    # 3. ウィンドウを表示
    window.show()
    
    # 4. イベントループを開始し、アプリケーションの終了コードで終了
    # app.exec()はユーザーがアプリケーションを終了するまでブロックされる
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 