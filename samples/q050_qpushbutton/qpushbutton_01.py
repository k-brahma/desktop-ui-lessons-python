"""
QPushButton基本サンプル - ボタンの基本機能

このモジュールは、PySide6のQPushButtonクラスの基本的な使用方法を示します。
QPushButtonは、クリック可能なボタンウィジェットで、最も一般的なUIコンポーネントです。

主要な学習ポイント:
- 基本的なボタンの作成と配置
- クリックイベントの処理
- ボタンのスタイリング
- 無効化と有効化
- シグナルとスロットの基本

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class BasicButtonWindow(QWidget):
    """
    基本的なQPushButtonの使用例を示すウィンドウクラス
    
    様々なスタイルと機能のQPushButtonを配置したウィンドウを作成します。
    """
    
    def __init__(self):
        """
        BasicButtonWindowクラスのコンストラクタ
        
        ウィンドウの初期設定と各種ボタンの作成を行います。
        """
        super().__init__()
        self.click_count = 0  # クリック回数をカウント
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        ウィンドウのレイアウトと各種QPushButtonの設定を行います。
        """
        self.setWindowTitle("QPushButton基本サンプル")
        self.setGeometry(200, 200, 500, 500)
        
        # メインレイアウト
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # ステータス表示用ラベル
        self.status_label = QLabel("ボタンをクリックしてください")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #f5f5f5;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.status_label)
        
        # 各種ボタンの作成
        self.create_basic_buttons(layout)
        
    def create_basic_buttons(self, layout):
        """
        基本的なボタンの作成と設定
        
        Args:
            layout (QVBoxLayout): ボタンを追加するレイアウト
        """
        # 1. シンプルなボタン
        simple_button = QPushButton("シンプルボタン")
        simple_button.clicked.connect(self.on_simple_click)
        layout.addWidget(simple_button)
        
        # 2. スタイル付きボタン
        styled_button = QPushButton("スタイル付きボタン")
        styled_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        styled_button.clicked.connect(self.on_styled_click)
        layout.addWidget(styled_button)
        
        # 3. カウンターボタン
        self.counter_button = QPushButton("クリック回数: 0")
        self.counter_button.clicked.connect(self.on_counter_click)
        self.counter_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: 2px solid #1976D2;
                padding: 12px;
                font-size: 14px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        layout.addWidget(self.counter_button)
        
        # 4. トグルボタン（チェック可能）
        self.toggle_button = QPushButton("トグルボタン (OFF)")
        self.toggle_button.setCheckable(True)  # チェック可能にする
        self.toggle_button.clicked.connect(self.on_toggle_click)
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #757575;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:checked {
                background-color: #FF5722;
            }
            QPushButton:hover {
                background-color: #616161;
            }
            QPushButton:checked:hover {
                background-color: #E64A19;
            }
        """)
        layout.addWidget(self.toggle_button)
        
        # 5. 無効化されたボタン
        disabled_button = QPushButton("無効化されたボタン")
        disabled_button.setEnabled(False)
        disabled_button.setStyleSheet("""
            QPushButton:disabled {
                background-color: #e0e0e0;
                color: #9e9e9e;
                border: 1px solid #bdbdbd;
                padding: 10px;
            }
        """)
        layout.addWidget(disabled_button)
        
        # 6. 有効化/無効化切り替えボタン
        self.enable_button = QPushButton("上のボタンを有効化")
        self.enable_button.clicked.connect(lambda: self.toggle_button_state(disabled_button))
        layout.addWidget(self.enable_button)
        
        # 7. 水平レイアウトでのボタン配置
        h_layout = QHBoxLayout()
        
        button1 = QPushButton("ボタン1")
        button1.clicked.connect(lambda: self.update_status("ボタン1がクリックされました"))
        button1.setStyleSheet("background-color: #E91E63; color: white; padding: 8px;")
        
        button2 = QPushButton("ボタン2")
        button2.clicked.connect(lambda: self.update_status("ボタン2がクリックされました"))
        button2.setStyleSheet("background-color: #9C27B0; color: white; padding: 8px;")
        
        button3 = QPushButton("ボタン3")
        button3.clicked.connect(lambda: self.update_status("ボタン3がクリックされました"))
        button3.setStyleSheet("background-color: #673AB7; color: white; padding: 8px;")
        
        h_layout.addWidget(button1)
        h_layout.addWidget(button2)
        h_layout.addWidget(button3)
        
        layout.addLayout(h_layout)
        
        # 8. 固定サイズボタン
        fixed_size_button = QPushButton("固定サイズ (150x50)")
        fixed_size_button.setFixedSize(150, 50)
        fixed_size_button.clicked.connect(self.on_fixed_size_click)
        fixed_size_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        layout.addWidget(fixed_size_button)
        
    def on_simple_click(self):
        """
        シンプルボタンのクリック処理
        """
        self.update_status("シンプルボタンがクリックされました")
        
    def on_styled_click(self):
        """
        スタイル付きボタンのクリック処理
        """
        self.update_status("スタイル付きボタンがクリックされました")
        
    def on_counter_click(self):
        """
        カウンターボタンのクリック処理
        
        クリック回数をカウントしてボタンのテキストを更新します。
        """
        self.click_count += 1
        self.counter_button.setText(f"クリック回数: {self.click_count}")
        self.update_status(f"カウンター: {self.click_count}回クリックされました")
        
    def on_toggle_click(self, checked):
        """
        トグルボタンのクリック処理
        
        Args:
            checked (bool): ボタンのチェック状態
        """
        if checked:
            self.toggle_button.setText("トグルボタン (ON)")
            self.update_status("トグルボタンが ON になりました")
        else:
            self.toggle_button.setText("トグルボタン (OFF)")
            self.update_status("トグルボタンが OFF になりました")
            
    def on_fixed_size_click(self):
        """
        固定サイズボタンのクリック処理
        """
        self.update_status("固定サイズボタンがクリックされました")
        
    def toggle_button_state(self, button):
        """
        ボタンの有効/無効状態を切り替え
        
        Args:
            button (QPushButton): 状態を切り替えるボタン
        """
        if button.isEnabled():
            button.setEnabled(False)
            self.enable_button.setText("上のボタンを有効化")
            self.update_status("ボタンを無効化しました")
        else:
            button.setEnabled(True)
            self.enable_button.setText("上のボタンを無効化")
            self.update_status("ボタンを有効化しました")
            
    def update_status(self, message):
        """
        ステータスラベルの更新
        
        Args:
            message (str): 表示するメッセージ
        """
        self.status_label.setText(message)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QPushButtonの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = BasicButtonWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 