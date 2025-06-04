"""
QWidget基本サンプル - ウィジェットの基本構造

このモジュールは、PySide6のQWidgetクラスの基本的な使用方法を示します。
QWidgetは、すべてのユーザーインターフェース要素の基底クラスです。

主要な学習ポイント:
- QWidgetの基本的な作成と表示
- ウィンドウプロパティの設定
- サイズと位置の制御
- 基本的なスタイリング
- 子ウィジェットの配置

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget


class BasicWidgetWindow(QWidget):
    """
    基本的なQWidgetの使用例を示すウィンドウクラス
    
    QWidgetの基本的なプロパティと機能を実演します。
    """
    
    def __init__(self):
        """
        BasicWidgetWindowクラスのコンストラクタ
        
        ウィンドウの初期設定と子ウィジェットの配置を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        ウィンドウの基本設定と子ウィジェットの配置を行います。
        """
        # ウィンドウの基本設定
        self.setWindowTitle("QWidget基本サンプル")
        self.setGeometry(300, 300, 500, 400)
        
        # ウィンドウの最小・最大サイズ設定
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)
        
        # 背景色とスタイルの設定
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: 'Yu Gothic UI', 'Meiryo', sans-serif;
            }
        """)
        
        # 子ウィジェットの作成と配置
        self.create_child_widgets()
        
    def create_child_widgets(self):
        """
        子ウィジェットの作成と配置
        
        絶対位置を使用してウィジェットを配置します。
        """
        # タイトルラベル
        title_label = QLabel("QWidget基本機能デモ", self)
        title_label.setGeometry(50, 30, 400, 40)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                background-color: #ecf0f1;
                padding: 10px;
                border-radius: 8px;
                border: 2px solid #bdc3c7;
            }
        """)
        
        # 説明ラベル
        description_label = QLabel(
            "このウィンドウはQWidgetの基本機能を示します。\n"
            "QWidgetは以下の特徴があります：\n"
            "• すべてのUIコンポーネントの基底クラス\n"
            "• ウィンドウやダイアログとして使用可能\n"
            "• 他のウィジェットのコンテナとしても機能",
            self
        )
        description_label.setGeometry(50, 90, 400, 120)
        description_label.setWordWrap(True)
        description_label.setStyleSheet("""
            QLabel {
                background-color: white;
                padding: 15px;
                border-radius: 6px;
                border: 1px solid #d5d5d5;
                line-height: 1.6;
                color: #34495e;
            }
        """)
        
        # 情報表示ラベル
        self.info_label = QLabel("ウィンドウ情報が表示されます", self)
        self.info_label.setGeometry(50, 230, 400, 60)
        self.info_label.setStyleSheet("""
            QLabel {
                background-color: #e8f5e8;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #27ae60;
                color: #2d5a2d;
            }
        """)
        
        # 情報更新ボタン
        update_button = QPushButton("ウィンドウ情報を更新", self)
        update_button.setGeometry(50, 310, 150, 35)
        update_button.clicked.connect(self.update_window_info)
        update_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        
        # ウィンドウを閉じるボタン
        close_button = QPushButton("ウィンドウを閉じる", self)
        close_button.setGeometry(220, 310, 150, 35)
        close_button.clicked.connect(self.close)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)
        
        # 初期情報の表示
        self.update_window_info()
        
    def update_window_info(self):
        """
        ウィンドウ情報の更新
        
        現在のウィンドウの状態情報を表示します。
        """
        # ウィンドウのサイズと位置を取得
        geometry = self.geometry()
        size = self.size()
        position = self.pos()
        
        info_text = (
            f"サイズ: {size.width()} x {size.height()}\n"
            f"位置: ({position.x()}, {position.y()})\n"
            f"表示状態: {'表示中' if self.isVisible() else '非表示'}"
        )
        
        self.info_label.setText(info_text)
        
    def resizeEvent(self, event):
        """
        ウィンドウサイズ変更イベントのオーバーライド
        
        Args:
            event: リサイズイベント
        """
        super().resizeEvent(event)
        self.update_window_info()
        
    def moveEvent(self, event):
        """
        ウィンドウ移動イベントのオーバーライド
        
        Args:
            event: 移動イベント
        """
        super().moveEvent(event)
        self.update_window_info()
        
    def closeEvent(self, event):
        """
        ウィンドウクローズイベントのオーバーライド
        
        Args:
            event: クローズイベント
        """
        print("QWidgetウィンドウが閉じられました")
        event.accept()


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QWidgetの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = BasicWidgetWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 