"""
QVBoxLayout基本サンプル - 縦方向レイアウト管理

このモジュールは、PySide6のQVBoxLayoutクラスの基本的な使用方法を示します。
QVBoxLayoutは、ウィジェットを縦方向（垂直方向）に配置するレイアウトマネージャーです。

主要な学習ポイント:
- 基本的な縦方向レイアウトの作成
- ウィジェットの追加と配置
- スペーシングとマージンの設定
- ストレッチファクターの使用
- レイアウトの入れ子構造

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class VBoxLayoutWindow(QWidget):
    """
    QVBoxLayoutの使用例を示すウィンドウクラス
    
    様々なウィジェットを縦方向に配置し、レイアウト管理の基本を実演します。
    """
    
    def __init__(self):
        """
        VBoxLayoutWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とレイアウトの構築を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        QVBoxLayoutを使用してウィジェットを配置します。
        """
        self.setWindowTitle("QVBoxLayout基本サンプル")
        self.setGeometry(200, 200, 500, 600)
        
        # メインのVBoxレイアウトを作成
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_header_section(main_layout)
        self.create_input_section(main_layout)
        self.create_content_section(main_layout)
        self.create_control_section(main_layout)
        self.create_footer_section(main_layout)
        
        # レイアウトの詳細設定
        self.configure_layout_properties(main_layout)
        
    def create_header_section(self, layout):
        """
        ヘッダーセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # タイトルラベル
        title_label = QLabel("QVBoxLayout デモアプリケーション")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #2c3e50;
                background-color: #ecf0f1;
                padding: 15px;
                border-radius: 8px;
                border: 2px solid #bdc3c7;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(title_label)
        
        # 説明ラベル
        description_label = QLabel(
            "このウィンドウは、QVBoxLayoutを使用して各ウィジェットを\n"
            "縦方向に整然と配置する方法を示しています。"
        )
        description_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #7f8c8d;
                padding: 10px;
                background-color: #f8f9fa;
                border-radius: 5px;
            }
        """)
        layout.addWidget(description_label)
        
    def create_input_section(self, layout):
        """
        入力セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # セクションタイトル
        input_title = QLabel("入力フィールド")
        input_title.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #34495e;
                margin-top: 15px;
                margin-bottom: 5px;
            }
        """)
        layout.addWidget(input_title)
        
        # 名前入力
        name_label = QLabel("名前:")
        name_label.setStyleSheet("color: #555; margin-bottom: 2px;")
        layout.addWidget(name_label)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("ここに名前を入力してください")
        self.name_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
        """)
        layout.addWidget(self.name_input)
        
        # メール入力
        email_label = QLabel("メールアドレス:")
        email_label.setStyleSheet("color: #555; margin-bottom: 2px; margin-top: 10px;")
        layout.addWidget(email_label)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("example@email.com")
        self.email_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
        """)
        layout.addWidget(self.email_input)
        
    def create_content_section(self, layout):
        """
        コンテンツセクションの作成（ストレッチファクター使用）
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # コメント入力エリア
        comment_label = QLabel("コメント:")
        comment_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #34495e;
                margin-top: 15px;
                margin-bottom: 5px;
            }
        """)
        layout.addWidget(comment_label)
        
        self.comment_text = QTextEdit()
        self.comment_text.setPlaceholderText("長いテキストやコメントをここに入力してください...")
        self.comment_text.setStyleSheet("""
            QTextEdit {
                border: 2px solid #ddd;
                border-radius: 4px;
                padding: 8px;
                font-size: 12px;
            }
            QTextEdit:focus {
                border-color: #3498db;
            }
        """)
        # ストレッチファクターを設定（他のウィジェットより多くの領域を占有）
        layout.addWidget(self.comment_text, stretch=1)
        
    def create_control_section(self, layout):
        """
        コントロールセクションの作成（水平レイアウトの入れ子）
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # オプション設定
        options_label = QLabel("オプション:")
        options_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #34495e;
                margin-top: 15px;
                margin-bottom: 5px;
            }
        """)
        layout.addWidget(options_label)
        
        # チェックボックス群
        self.newsletter_check = QCheckBox("ニュースレターを受け取る")
        self.newsletter_check.setStyleSheet("color: #555; margin: 5px;")
        layout.addWidget(self.newsletter_check)
        
        self.terms_check = QCheckBox("利用規約に同意する")
        self.terms_check.setStyleSheet("color: #555; margin: 5px;")
        layout.addWidget(self.terms_check)
        
        # 水平レイアウトでボタンを配置
        button_layout = QHBoxLayout()
        
        # クリアボタン
        clear_button = QPushButton("クリア")
        clear_button.clicked.connect(self.clear_form)
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        button_layout.addWidget(clear_button)
        
        # 送信ボタン
        submit_button = QPushButton("送信")
        submit_button.clicked.connect(self.submit_form)
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        button_layout.addWidget(submit_button)
        
        # 水平レイアウトをメインレイアウトに追加
        layout.addLayout(button_layout)
        
    def create_footer_section(self, layout):
        """
        フッターセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # ステータス表示
        self.status_label = QLabel("準備完了")
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #d4edda;
                color: #155724;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #c3e6cb;
                margin-top: 10px;
            }
        """)
        layout.addWidget(self.status_label)
        
    def configure_layout_properties(self, layout):
        """
        レイアウトプロパティの設定
        
        Args:
            layout (QVBoxLayout): 設定対象のレイアウト
        """
        # ウィジェット間のスペーシング
        layout.setSpacing(10)
        
        # レイアウトのマージン（上、下、左、右）
        layout.setContentsMargins(20, 20, 20, 20)
        
    def clear_form(self):
        """
        フォームのクリア処理
        
        すべての入力フィールドをクリアします。
        """
        self.name_input.clear()
        self.email_input.clear()
        self.comment_text.clear()
        self.newsletter_check.setChecked(False)
        self.terms_check.setChecked(False)
        self.status_label.setText("フォームをクリアしました")
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #fff3cd;
                color: #856404;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ffeaa7;
                margin-top: 10px;
            }
        """)
        
    def submit_form(self):
        """
        フォームの送信処理
        
        入力内容を検証し、結果を表示します。
        """
        name = self.name_input.text()
        email = self.email_input.text()
        comment = self.comment_text.toPlainText()
        newsletter = self.newsletter_check.isChecked()
        terms = self.terms_check.isChecked()
        
        if not name or not email:
            self.status_label.setText("名前とメールアドレスは必須です")
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #f8d7da;
                    color: #721c24;
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #f5c6cb;
                    margin-top: 10px;
                }
            """)
            return
            
        if not terms:
            self.status_label.setText("利用規約への同意が必要です")
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #f8d7da;
                    color: #721c24;
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #f5c6cb;
                    margin-top: 10px;
                }
            """)
            return
            
        # 送信成功
        success_message = f"送信完了！ {name}さん、ありがとうございました。"
        self.status_label.setText(success_message)
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #d4edda;
                color: #155724;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #c3e6cb;
                margin-top: 10px;
            }
        """)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QVBoxLayoutの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = VBoxLayoutWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 