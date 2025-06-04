"""
QMainWindow基本サンプル - メインウィンドウの基本構造

このモジュールは、PySide6のQMainWindowクラスの基本的な使用方法を示します。
QMainWindowは、メニューバー、ツールバー、ステータスバー、中央ウィジェット
などの標準的なアプリケーションウィンドウ要素を提供します。

主要な学習ポイント:
- QMainWindowの基本構造
- 中央ウィジェットの設定
- ウィンドウのタイトルとサイズ設定
- 基本的なレイアウト管理

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class BasicMainWindow(QMainWindow):
    """
    基本的なメインウィンドウクラス
    
    QMainWindowを継承し、中央ウィジェットを配置した
    シンプルなメインウィンドウを作成します。
    """
    
    def __init__(self):
        """
        BasicMainWindowクラスのコンストラクタ
        
        メインウィンドウの基本設定と中央ウィジェットの配置を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        ウィンドウのタイトル、サイズ、中央ウィジェットを設定します。
        """
        # ウィンドウの基本設定
        self.setWindowTitle("QMainWindow基本サンプル")
        self.setGeometry(100, 100, 600, 400)
        
        # 中央ウィジェットの作成と設定
        self.setup_central_widget()
        
    def setup_central_widget(self):
        """
        中央ウィジェットの設定
        
        QMainWindowの中央領域にウィジェットを配置します。
        QMainWindowでは、中央ウィジェットの設定が必須です。
        """
        # 中央ウィジェットの作成
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # レイアウトの作成
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # ウェルカムメッセージ
        welcome_label = QLabel("QMainWindowへようこそ！")
        welcome_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                padding: 20px;
                text-align: center;
            }
        """)
        layout.addWidget(welcome_label)
        
        # 説明ラベル
        description_label = QLabel(
            "これは基本的なQMainWindowの例です。\n"
            "QMainWindowは以下の要素を持つことができます：\n"
            "• メニューバー\n"
            "• ツールバー\n"
            "• ステータスバー\n"
            "• 中央ウィジェット\n"
            "• ドックウィジェット"
        )
        description_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #34495e;
                padding: 20px;
                line-height: 1.5;
            }
        """)
        layout.addWidget(description_label)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QMainWindowを使用したアプリケーションの基本的な構造を示します。
    """
    # アプリケーションの作成
    app = QApplication(sys.argv)
    
    # メインウィンドウの作成
    main_window = BasicMainWindow()
    
    # ウィンドウの表示
    main_window.show()
    
    # イベントループの開始
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 