"""
QLineEdit基本サンプル - テキスト入力フィールドの基本操作

このモジュールは、PySide6のQLineEditクラスの基本的な使用方法を示します。
QLineEditは、1行のテキスト入力を可能にするウィジェットで、
フォーム、検索ボックス、設定画面などで広く使用されます。

主要な学習ポイント:
- 基本的なテキスト入力フィールドの作成
- プレースホルダーテキストの設定
- 入力検証とマスクの使用
- エコーモード（パスワード入力）
- シグナルとスロットによるイベント処理

Authors: PySide6 Learning Team
Date: 2024
"""

import re
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class LineEditDemoWindow(QWidget):
    """
    QLineEditの使用例を示すウィンドウクラス
    
    様々なタイプのテキスト入力フィールドと機能を実演します。
    """
    
    def __init__(self):
        """
        LineEditDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とQLineEditサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQLineEditの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QLineEdit基本サンプル - テキスト入力フィールド")
        self.setGeometry(200, 200, 600, 700)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_title_section(main_layout)
        self.create_basic_inputs_section(main_layout)
        self.create_validation_section(main_layout)
        self.create_mask_section(main_layout)
        self.create_password_section(main_layout)
        self.create_interactive_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QLineEdit デモンストレーション")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                background-color: #ecf0f1;
                padding: 15px;
                border-radius: 8px;
                border: 2px solid #bdc3c7;
                margin-bottom: 15px;
            }
        """)
        layout.addWidget(title_label)
        
    def create_basic_inputs_section(self, layout):
        """
        基本的な入力フィールドセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 基本入力グループ
        basic_group = QGroupBox("基本的なテキスト入力")
        basic_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        basic_layout = QFormLayout()
        
        # 通常のテキスト入力
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("例: 山田太郎")
        self.name_edit.textChanged.connect(self.on_name_changed)
        basic_layout.addRow("名前:", self.name_edit)
        
        # 最大文字数制限付き
        self.short_edit = QLineEdit()
        self.short_edit.setMaxLength(10)
        self.short_edit.setPlaceholderText("最大10文字まで")
        basic_layout.addRow("短いテキスト:", self.short_edit)
        
        # 読み取り専用
        readonly_edit = QLineEdit("これは読み取り専用です")
        readonly_edit.setReadOnly(True)
        readonly_edit.setStyleSheet("background-color: #f8f9fa; color: #6c757d;")
        basic_layout.addRow("読み取り専用:", readonly_edit)
        
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
    def create_validation_section(self, layout):
        """
        入力検証セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 検証グループ
        validation_group = QGroupBox("入力検証")
        validation_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #e74c3c;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        validation_layout = QFormLayout()
        
        # 数値のみ（整数）
        self.number_edit = QLineEdit()
        int_validator = QIntValidator(0, 999)
        self.number_edit.setValidator(int_validator)
        self.number_edit.setPlaceholderText("0-999の整数のみ")
        validation_layout.addRow("整数入力:", self.number_edit)
        
        # メールアドレス形式
        self.email_edit = QLineEdit()
        # 簡単なメールアドレスの正規表現
        email_regex = QRegularExpressionValidator()
        email_regex.setRegularExpression(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        self.email_edit.setValidator(email_regex)
        self.email_edit.setPlaceholderText("example@email.com")
        self.email_edit.textChanged.connect(self.validate_email)
        validation_layout.addRow("メールアドレス:", self.email_edit)
        
        validation_group.setLayout(validation_layout)
        layout.addWidget(validation_group)
        
    def create_mask_section(self, layout):
        """
        入力マスクセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # マスクグループ
        mask_group = QGroupBox("入力マスク")
        mask_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #f39c12;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        mask_layout = QFormLayout()
        
        # 電話番号
        phone_edit = QLineEdit()
        phone_edit.setInputMask("000-0000-0000")
        phone_edit.setPlaceholderText("090-1234-5678")
        mask_layout.addRow("電話番号:", phone_edit)
        
        # 郵便番号
        zip_edit = QLineEdit()
        zip_edit.setInputMask("000-0000")
        zip_edit.setPlaceholderText("123-4567")
        mask_layout.addRow("郵便番号:", zip_edit)
        
        # 日付
        date_edit = QLineEdit()
        date_edit.setInputMask("0000/00/00")
        date_edit.setPlaceholderText("2024/12/31")
        mask_layout.addRow("日付:", date_edit)
        
        mask_group.setLayout(mask_layout)
        layout.addWidget(mask_group)
        
    def create_password_section(self, layout):
        """
        パスワード入力セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # パスワードグループ
        password_group = QGroupBox("パスワード入力")
        password_group.setStyleSheet("""
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
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        password_layout = QFormLayout()
        
        # 通常のパスワード
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.setPlaceholderText("パスワードを入力")
        password_layout.addRow("パスワード:", self.password_edit)
        
        # 確認用パスワード
        self.confirm_edit = QLineEdit()
        self.confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_edit.setPlaceholderText("パスワードを再入力")
        self.confirm_edit.textChanged.connect(self.validate_password_match)
        password_layout.addRow("パスワード確認:", self.confirm_edit)
        
        # パスワード表示切り替えボタン
        show_password_btn = QPushButton("パスワードを表示")
        show_password_btn.setCheckable(True)
        show_password_btn.toggled.connect(self.toggle_password_visibility)
        show_password_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:checked {
                background-color: #e74c3c;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:checked:hover {
                background-color: #c0392b;
            }
        """)
        password_layout.addRow("", show_password_btn)
        
        password_group.setLayout(password_layout)
        layout.addWidget(password_group)
        
    def create_interactive_section(self, layout):
        """
        インタラクティブセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # インタラクティブグループ
        interactive_group = QGroupBox("インタラクティブ機能")
        interactive_group.setStyleSheet("""
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
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        interactive_layout = QVBoxLayout()
        
        # リアルタイム更新フィールド
        realtime_layout = QHBoxLayout()
        realtime_layout.addWidget(QLabel("リアルタイム更新:"))
        self.realtime_edit = QLineEdit()
        self.realtime_edit.setPlaceholderText("入力すると即座に下に表示されます")
        self.realtime_edit.textChanged.connect(self.update_realtime_display)
        realtime_layout.addWidget(self.realtime_edit)
        interactive_layout.addLayout(realtime_layout)
        
        # リアルタイム表示エリア
        self.realtime_display = QLabel("入力待ち...")
        self.realtime_display.setStyleSheet("""
            QLabel {
                background-color: #e8f5e8;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #27ae60;
                margin: 5px 0;
            }
        """)
        interactive_layout.addWidget(self.realtime_display)
        
        # コントロールボタン
        button_layout = QHBoxLayout()
        
        clear_all_btn = QPushButton("すべてクリア")
        clear_all_btn.clicked.connect(self.clear_all_fields)
        clear_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        button_layout.addWidget(clear_all_btn)
        
        fill_sample_btn = QPushButton("サンプルデータ入力")
        fill_sample_btn.clicked.connect(self.fill_sample_data)
        fill_sample_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        button_layout.addWidget(fill_sample_btn)
        
        get_values_btn = QPushButton("入力値を取得")
        get_values_btn.clicked.connect(self.get_all_values)
        get_values_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        button_layout.addWidget(get_values_btn)
        
        interactive_layout.addLayout(button_layout)
        
        # 結果表示エリア
        self.result_display = QTextEdit()
        self.result_display.setMaximumHeight(100)
        self.result_display.setPlaceholderText("結果がここに表示されます...")
        self.result_display.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 5px;
                font-family: 'Courier New', monospace;
            }
        """)
        interactive_layout.addWidget(self.result_display)
        
        interactive_group.setLayout(interactive_layout)
        layout.addWidget(interactive_group)
        
    def on_name_changed(self, text):
        """
        名前フィールドの変更処理
        
        Args:
            text (str): 入力されたテキスト
        """
        # 簡単な入力検証
        if len(text) > 20:
            self.name_edit.setStyleSheet("border: 2px solid red;")
        else:
            self.name_edit.setStyleSheet("")
            
    def validate_email(self, text):
        """
        メールアドレスの検証
        
        Args:
            text (str): 入力されたテキスト
        """
        if text and "@" in text and "." in text:
            self.email_edit.setStyleSheet("border: 2px solid green;")
        elif text:
            self.email_edit.setStyleSheet("border: 2px solid orange;")
        else:
            self.email_edit.setStyleSheet("")
            
    def validate_password_match(self, text):
        """
        パスワード一致の検証
        
        Args:
            text (str): 確認用パスワード
        """
        password = self.password_edit.text()
        if text and password:
            if text == password:
                self.confirm_edit.setStyleSheet("border: 2px solid green;")
            else:
                self.confirm_edit.setStyleSheet("border: 2px solid red;")
        else:
            self.confirm_edit.setStyleSheet("")
            
    def toggle_password_visibility(self, show):
        """
        パスワード表示の切り替え
        
        Args:
            show (bool): 表示するかどうか
        """
        if show:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirm_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
            
    def update_realtime_display(self, text):
        """
        リアルタイム表示の更新
        
        Args:
            text (str): 入力されたテキスト
        """
        if text:
            self.realtime_display.setText(f"入力中: '{text}' (文字数: {len(text)})")
        else:
            self.realtime_display.setText("入力待ち...")
            
    def clear_all_fields(self):
        """
        すべてのフィールドをクリア
        """
        self.name_edit.clear()
        self.short_edit.clear()
        self.number_edit.clear()
        self.email_edit.clear()
        self.password_edit.clear()
        self.confirm_edit.clear()
        self.realtime_edit.clear()
        self.result_display.clear()
        
        # スタイルもリセット
        for edit in [self.name_edit, self.email_edit, self.confirm_edit]:
            edit.setStyleSheet("")
            
    def fill_sample_data(self):
        """
        サンプルデータの入力
        """
        self.name_edit.setText("山田太郎")
        self.short_edit.setText("サンプル")
        self.number_edit.setText("123")
        self.email_edit.setText("yamada@example.com")
        self.password_edit.setText("password123")
        self.confirm_edit.setText("password123")
        self.realtime_edit.setText("リアルタイムテスト")
        
    def get_all_values(self):
        """
        すべての入力値を取得して表示
        """
        values = {
            "名前": self.name_edit.text(),
            "短いテキスト": self.short_edit.text(),
            "整数": self.number_edit.text(),
            "メールアドレス": self.email_edit.text(),
            "パスワード": "●" * len(self.password_edit.text()),
            "リアルタイム": self.realtime_edit.text()
        }
        
        result_text = "=== 入力値一覧 ===\n"
        for key, value in values.items():
            result_text += f"{key}: {value or '(空)'}\n"
            
        self.result_display.setText(result_text)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QLineEditの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = LineEditDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 