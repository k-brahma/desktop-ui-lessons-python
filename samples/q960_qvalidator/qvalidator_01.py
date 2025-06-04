"""
QValidator基本サンプル - 入力検証クラス

このモジュールは、PySide6のQValidatorクラスの基本的な使用方法を示します。
QValidatorは、ユーザー入力の妥当性を検証するためのクラス群です。

主要な学習ポイント:
- 数値検証（QIntValidator、QDoubleValidator）
- 正規表現検証（QRegularExpressionValidator）
- カスタムバリデーターの作成
- 入力制限とフィードバック表示
- 実用的な検証例（メール、電話番号、パスワード等）

Authors: PySide6 Learning Team
Date: 2024
"""

import re
import sys

from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import (
    QDoubleValidator,
    QFont,
    QIntValidator,
    QRegularExpressionValidator,
    QValidator,
)
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class EmailValidator(QValidator):
    """
    カスタムメールアドレスバリデーター
    """
    
    def validate(self, input_str: str, pos: int):
        """
        メールアドレスの検証
        
        Args:
            input_str (str): 入力文字列
            pos (int): カーソル位置
            
        Returns:
            tuple: (検証状態, 入力文字列, カーソル位置)
        """
        # 空文字列は中間状態
        if not input_str:
            return (QValidator.State.Intermediate, input_str, pos)
            
        # 基本的なメール形式チェック
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(email_pattern, input_str):
            return (QValidator.State.Acceptable, input_str, pos)
        elif self.is_partial_email(input_str):
            return (QValidator.State.Intermediate, input_str, pos)
        else:
            return (QValidator.State.Invalid, input_str, pos)
            
    def is_partial_email(self, input_str: str) -> bool:
        """
        部分的なメールアドレスかどうかをチェック
        
        Args:
            input_str (str): 入力文字列
            
        Returns:
            bool: 部分的なメールアドレスの場合True
        """
        # 許可された文字のみで構成されているか
        allowed_chars = re.match(r'^[a-zA-Z0-9._%+-@]*$', input_str)
        if not allowed_chars:
            return False
            
        # @が2個以上ある場合は無効
        if input_str.count('@') > 1:
            return False
            
        # @があればより詳細にチェック
        if '@' in input_str:
            parts = input_str.split('@')
            if len(parts) == 2:
                local, domain = parts
                # ローカル部が空でない、ドメイン部が有効な文字で構成
                return len(local) > 0 and bool(re.match(r'^[a-zA-Z0-9.-]*$', domain))
                
        return True


class PasswordValidator(QValidator):
    """
    カスタムパスワードバリデーター
    """
    
    def __init__(self, min_length=8):
        super().__init__()
        self.min_length = min_length
        
    def validate(self, input_str: str, pos: int):
        """
        パスワードの検証
        
        Args:
            input_str (str): 入力文字列
            pos (int): カーソル位置
            
        Returns:
            tuple: (検証状態, 入力文字列, カーソル位置)
        """
        if len(input_str) < self.min_length:
            return (QValidator.State.Intermediate, input_str, pos)
            
        # パスワード強度チェック
        has_upper = any(c.isupper() for c in input_str)
        has_lower = any(c.islower() for c in input_str)
        has_digit = any(c.isdigit() for c in input_str)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in input_str)
        
        if has_upper and has_lower and has_digit and has_special:
            return (QValidator.State.Acceptable, input_str, pos)
        else:
            return (QValidator.State.Intermediate, input_str, pos)


class ValidatorDemoWindow(QWidget):
    """
    QValidatorの使用例を示すウィンドウクラス
    
    様々なバリデーション機能を実演します。
    """
    
    def __init__(self):
        """
        ValidatorDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とバリデーションサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQValidatorの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QValidator基本サンプル - 入力検証クラス")
        self.setGeometry(200, 200, 800, 700)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # タイトル
        self.create_title_section(main_layout)
        
        # 水平レイアウトで左右に分割
        horizontal_layout = QHBoxLayout()
        
        # 左側のカラム
        left_column = QVBoxLayout()
        self.create_numeric_validators_section(left_column)
        self.create_regex_validators_section(left_column)
        
        # 右側のカラム
        right_column = QVBoxLayout()
        self.create_custom_validators_section(right_column)
        self.create_validation_feedback_section(right_column)
        
        horizontal_layout.addLayout(left_column)
        horizontal_layout.addLayout(right_column)
        main_layout.addLayout(horizontal_layout)
        
        # ログ表示エリア
        self.create_log_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QValidator デモンストレーション")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        
    def create_numeric_validators_section(self, layout):
        """
        数値バリデーターセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        numeric_group = QGroupBox("数値バリデーター")
        numeric_group.setStyleSheet("""
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
        
        numeric_layout = QFormLayout()
        
        # 整数バリデーター
        self.int_input = QLineEdit()
        int_validator = QIntValidator(-100, 100)
        self.int_input.setValidator(int_validator)
        self.int_input.setPlaceholderText("整数 (-100 ～ 100)")
        self.int_input.textChanged.connect(lambda text: self.validate_and_log("整数", text, self.int_input))
        numeric_layout.addRow("整数入力:", self.int_input)
        
        # 浮動小数点バリデーター
        self.double_input = QLineEdit()
        double_validator = QDoubleValidator(0.0, 999.99, 2)
        self.double_input.setValidator(double_validator)
        self.double_input.setPlaceholderText("小数 (0.00 ～ 999.99)")
        self.double_input.textChanged.connect(lambda text: self.validate_and_log("小数", text, self.double_input))
        numeric_layout.addRow("小数入力:", self.double_input)
        
        # 年齢入力（カスタム範囲）
        self.age_input = QLineEdit()
        age_validator = QIntValidator(0, 150)
        self.age_input.setValidator(age_validator)
        self.age_input.setPlaceholderText("年齢 (0 ～ 150)")
        self.age_input.textChanged.connect(lambda text: self.validate_and_log("年齢", text, self.age_input))
        numeric_layout.addRow("年齢:", self.age_input)
        
        numeric_group.setLayout(numeric_layout)
        layout.addWidget(numeric_group)
        
    def create_regex_validators_section(self, layout):
        """
        正規表現バリデーターセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        regex_group = QGroupBox("正規表現バリデーター")
        regex_group.setStyleSheet("""
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
        
        regex_layout = QFormLayout()
        
        # 郵便番号バリデーター（日本）
        self.postal_input = QLineEdit()
        postal_regex = QRegularExpression(r'^\d{3}-\d{4}$')
        postal_validator = QRegularExpressionValidator(postal_regex)
        self.postal_input.setValidator(postal_validator)
        self.postal_input.setPlaceholderText("123-4567")
        self.postal_input.textChanged.connect(lambda text: self.validate_and_log("郵便番号", text, self.postal_input))
        regex_layout.addRow("郵便番号:", self.postal_input)
        
        # 電話番号バリデーター
        self.phone_input = QLineEdit()
        phone_regex = QRegularExpression(r'^0\d{1,4}-\d{1,4}-\d{4}$')
        phone_validator = QRegularExpressionValidator(phone_regex)
        self.phone_input.setValidator(phone_validator)
        self.phone_input.setPlaceholderText("090-1234-5678")
        self.phone_input.textChanged.connect(lambda text: self.validate_and_log("電話番号", text, self.phone_input))
        regex_layout.addRow("電話番号:", self.phone_input)
        
        # 英数字のみ
        self.alphanumeric_input = QLineEdit()
        alphanumeric_regex = QRegularExpression(r'^[a-zA-Z0-9]*$')
        alphanumeric_validator = QRegularExpressionValidator(alphanumeric_regex)
        self.alphanumeric_input.setValidator(alphanumeric_validator)
        self.alphanumeric_input.setPlaceholderText("英数字のみ")
        self.alphanumeric_input.textChanged.connect(lambda text: self.validate_and_log("英数字", text, self.alphanumeric_input))
        regex_layout.addRow("英数字:", self.alphanumeric_input)
        
        regex_group.setLayout(regex_layout)
        layout.addWidget(regex_group)
        
    def create_custom_validators_section(self, layout):
        """
        カスタムバリデーターセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        custom_group = QGroupBox("カスタムバリデーター")
        custom_group.setStyleSheet("""
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
        
        custom_layout = QFormLayout()
        
        # メールアドレスバリデーター
        self.email_input = QLineEdit()
        email_validator = EmailValidator()
        self.email_input.setValidator(email_validator)
        self.email_input.setPlaceholderText("user@example.com")
        self.email_input.textChanged.connect(lambda text: self.validate_and_log("メールアドレス", text, self.email_input))
        custom_layout.addRow("メールアドレス:", self.email_input)
        
        # パスワードバリデーター
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_validator = PasswordValidator()
        self.password_input.setValidator(password_validator)
        self.password_input.setPlaceholderText("8文字以上、大小英数記号")
        self.password_input.textChanged.connect(lambda text: self.validate_password(text))
        custom_layout.addRow("パスワード:", self.password_input)
        
        # パスワード強度表示
        self.password_strength = QLabel("強度: なし")
        self.password_strength.setStyleSheet("color: #7f8c8d; font-style: italic;")
        custom_layout.addRow("", self.password_strength)
        
        custom_group.setLayout(custom_layout)
        layout.addWidget(custom_group)
        
    def create_validation_feedback_section(self, layout):
        """
        検証フィードバックセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        feedback_group = QGroupBox("検証フィードバック")
        feedback_group.setStyleSheet("""
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
        
        feedback_layout = QVBoxLayout()
        
        # 検証状態表示
        self.validation_status = QLabel("入力待ち...")
        self.validation_status.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #6c757d;
            }
        """)
        feedback_layout.addWidget(self.validation_status)
        
        # テスト用ボタン
        test_layout = QHBoxLayout()
        
        validate_all_btn = QPushButton("全て検証")
        validate_all_btn.clicked.connect(self.validate_all_inputs)
        validate_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        test_layout.addWidget(validate_all_btn)
        
        clear_all_btn = QPushButton("全てクリア")
        clear_all_btn.clicked.connect(self.clear_all_inputs)
        clear_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        test_layout.addWidget(clear_all_btn)
        
        feedback_layout.addLayout(test_layout)
        
        feedback_group.setLayout(feedback_layout)
        layout.addWidget(feedback_group)
        
    def create_log_section(self, layout):
        """
        ログセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        log_group = QGroupBox("バリデーションログ")
        log_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #2c3e50;
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
        
        log_layout = QVBoxLayout()
        
        self.log_display = QTextEdit()
        self.log_display.setMaximumHeight(120)
        self.log_display.setPlaceholderText("バリデーション結果がここに表示されます...")
        self.log_display.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Courier New', monospace;
                font-size: 11px;
            }
        """)
        log_layout.addWidget(self.log_display)
        
        # クリアボタン
        clear_log_btn = QPushButton("ログをクリア")
        clear_log_btn.clicked.connect(self.log_display.clear)
        clear_log_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        log_layout.addWidget(clear_log_btn)
        
        log_group.setLayout(log_layout)
        layout.addWidget(log_group)
        
    def validate_and_log(self, field_name: str, text: str, input_widget: QLineEdit):
        """
        入力検証とログ記録
        
        Args:
            field_name (str): フィールド名
            text (str): 入力テキスト
            input_widget (QLineEdit): 入力ウィジェット
        """
        validator = input_widget.validator()
        if validator:
            state, _, _ = validator.validate(text, 0)
            
            # スタイルの更新
            if state == QValidator.State.Acceptable:
                input_widget.setStyleSheet("border: 2px solid #27ae60; background-color: #d5f4e6;")
                status = "✓ 有効"
                color = "#27ae60"
            elif state == QValidator.State.Intermediate:
                input_widget.setStyleSheet("border: 2px solid #f39c12; background-color: #fef9e7;")
                status = "⚠ 部分的"
                color = "#f39c12"
            else:
                input_widget.setStyleSheet("border: 2px solid #e74c3c; background-color: #fadbd8;")
                status = "✗ 無効"
                color = "#e74c3c"
                
            # ログに記録
            self.log_display.append(f"[{field_name}] '{text}' → {status}")
            
            # 全体ステータス更新
            self.validation_status.setText(f"最後の検証: {field_name} - {status}")
            self.validation_status.setStyleSheet(f"""
                QLabel {{
                    background-color: #f8f9fa;
                    padding: 10px;
                    border-radius: 5px;
                    border-left: 4px solid {color};
                    color: {color};
                }}
            """)
            
    def validate_password(self, text: str):
        """
        パスワードの検証と強度表示
        
        Args:
            text (str): パスワードテキスト
        """
        strength_score = 0
        criteria = []
        
        if len(text) >= 8:
            strength_score += 1
            criteria.append("✓ 8文字以上")
        else:
            criteria.append("✗ 8文字以上")
            
        if any(c.isupper() for c in text):
            strength_score += 1
            criteria.append("✓ 大文字")
        else:
            criteria.append("✗ 大文字")
            
        if any(c.islower() for c in text):
            strength_score += 1
            criteria.append("✓ 小文字")
        else:
            criteria.append("✗ 小文字")
            
        if any(c.isdigit() for c in text):
            strength_score += 1
            criteria.append("✓ 数字")
        else:
            criteria.append("✗ 数字")
            
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in text):
            strength_score += 1
            criteria.append("✓ 記号")
        else:
            criteria.append("✗ 記号")
            
        # 強度レベル
        if strength_score == 5:
            strength = "非常に強い"
            color = "#27ae60"
        elif strength_score >= 4:
            strength = "強い"
            color = "#f39c12"
        elif strength_score >= 3:
            strength = "普通"
            color = "#e67e22"
        elif strength_score >= 1:
            strength = "弱い"
            color = "#e74c3c"
        else:
            strength = "なし"
            color = "#7f8c8d"
            
        self.password_strength.setText(f"強度: {strength} ({strength_score}/5)")
        self.password_strength.setStyleSheet(f"color: {color}; font-weight: bold;")
        
        # ログに記録
        criteria_text = ', '.join(criteria)
        self.log_display.append(f"[パスワード強度] {strength} - {criteria_text}")
        
    def validate_all_inputs(self):
        """
        全ての入力フィールドを検証
        """
        inputs = [
            ("整数", self.int_input),
            ("小数", self.double_input),
            ("年齢", self.age_input),
            ("郵便番号", self.postal_input),
            ("電話番号", self.phone_input),
            ("英数字", self.alphanumeric_input),
            ("メールアドレス", self.email_input),
        ]
        
        self.log_display.append("=== 全フィールドの検証開始 ===")
        
        valid_count = 0
        total_count = len(inputs)
        
        for field_name, input_widget in inputs:
            text = input_widget.text()
            validator = input_widget.validator()
            
            if validator:
                state, _, _ = validator.validate(text, 0)
                if state == QValidator.State.Acceptable:
                    valid_count += 1
                    
        # パスワードも含める
        password_text = self.password_input.text()
        password_validator = self.password_input.validator()
        if password_validator:
            state, _, _ = password_validator.validate(password_text, 0)
            if state == QValidator.State.Acceptable:
                valid_count += 1
            total_count += 1
            
        self.log_display.append(f"検証結果: {valid_count}/{total_count} フィールドが有効")
        self.log_display.append("=== 検証終了 ===")
        
    def clear_all_inputs(self):
        """
        全ての入力フィールドをクリア
        """
        inputs = [
            self.int_input, self.double_input, self.age_input,
            self.postal_input, self.phone_input, self.alphanumeric_input,
            self.email_input, self.password_input
        ]
        
        for input_widget in inputs:
            input_widget.clear()
            input_widget.setStyleSheet("")  # スタイルもリセット
            
        self.password_strength.setText("強度: なし")
        self.password_strength.setStyleSheet("color: #7f8c8d; font-style: italic;")
        
        self.validation_status.setText("入力待ち...")
        self.validation_status.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #6c757d;
            }
        """)
        
        self.log_display.append("全てのフィールドをクリアしました")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QValidatorの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = ValidatorDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 