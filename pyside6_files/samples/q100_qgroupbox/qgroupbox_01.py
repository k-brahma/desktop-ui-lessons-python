"""
QGroupBox基本サンプル - ウィジェットのグループ化と整理

このモジュールは、PySide6のQGroupBoxクラスの基本的な使用方法を示します。
QGroupBoxは、関連するウィジェットをグループ化し、視覚的に整理するためのコンテナです。

主要な学習ポイント:
- 基本的なグループボックスの作成
- タイトルとチェック可能なグループボックス
- グループボックス内でのレイアウト管理
- スタイリングとカスタマイズ
- ネストしたグループボックス

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class GroupBoxDemoWindow(QWidget):
    """
    QGroupBoxの使用例を示すウィンドウクラス
    
    様々なタイプのグループボックスとその機能を実演します。
    """
    
    def __init__(self):
        """
        GroupBoxDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とグループボックスサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQGroupBoxの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QGroupBox基本サンプル - ウィジェットのグループ化")
        self.setGeometry(200, 200, 900, 800)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_title_section(main_layout)
        
        # 水平レイアウトで左右に分割
        horizontal_layout = QHBoxLayout()
        
        # 左側のカラム
        left_column = QVBoxLayout()
        self.create_basic_groupbox_section(left_column)
        self.create_checkable_groupbox_section(left_column)
        self.create_form_groupbox_section(left_column)
        
        # 右側のカラム
        right_column = QVBoxLayout()
        self.create_settings_groupbox_section(right_column)
        self.create_nested_groupbox_section(right_column)
        self.create_styled_groupbox_section(right_column)
        
        horizontal_layout.addLayout(left_column)
        horizontal_layout.addLayout(right_column)
        main_layout.addLayout(horizontal_layout)
        
        # 結果表示エリア
        self.create_result_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QGroupBox デモンストレーション")
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
        
    def create_basic_groupbox_section(self, layout):
        """
        基本的なグループボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 基本グループボックス
        basic_group = QGroupBox("基本的なグループボックス")
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
        
        basic_layout = QVBoxLayout()
        
        # 情報表示
        info_label = QLabel("これは基本的なグループボックスです。\n関連するウィジェットをまとめることができます。")
        info_label.setWordWrap(True)
        info_label.setStyleSheet("color: #5d6d7e; padding: 5px;")
        basic_layout.addWidget(info_label)
        
        # ボタン群
        button_layout = QHBoxLayout()
        button1 = QPushButton("操作1")
        button2 = QPushButton("操作2")
        button3 = QPushButton("操作3")
        
        button1.clicked.connect(lambda: self.log_action("基本グループ - 操作1が実行されました"))
        button2.clicked.connect(lambda: self.log_action("基本グループ - 操作2が実行されました"))
        button3.clicked.connect(lambda: self.log_action("基本グループ - 操作3が実行されました"))
        
        for btn in [button1, button2, button3]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 8px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
        
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        
        basic_layout.addLayout(button_layout)
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
    def create_checkable_groupbox_section(self, layout):
        """
        チェック可能なグループボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # チェック可能なグループボックス
        self.checkable_group = QGroupBox("有効/無効切り替え可能なグループ")
        self.checkable_group.setCheckable(True)
        self.checkable_group.setChecked(True)
        self.checkable_group.toggled.connect(self.on_checkable_group_toggled)
        self.checkable_group.setStyleSheet("""
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
        
        checkable_layout = QVBoxLayout()
        
        # 通知設定
        self.email_checkbox = QCheckBox("メール通知")
        self.email_checkbox.setChecked(True)
        self.sms_checkbox = QCheckBox("SMS通知")
        self.push_checkbox = QCheckBox("プッシュ通知")
        self.push_checkbox.setChecked(True)
        
        checkable_layout.addWidget(self.email_checkbox)
        checkable_layout.addWidget(self.sms_checkbox)
        checkable_layout.addWidget(self.push_checkbox)
        
        # 通知頻度
        frequency_layout = QHBoxLayout()
        frequency_layout.addWidget(QLabel("通知頻度:"))
        self.frequency_combo = QComboBox()
        self.frequency_combo.addItems(["即座に", "5分ごと", "1時間ごと", "1日1回"])
        frequency_layout.addWidget(self.frequency_combo)
        
        checkable_layout.addLayout(frequency_layout)
        
        self.checkable_group.setLayout(checkable_layout)
        layout.addWidget(self.checkable_group)
        
    def create_form_groupbox_section(self, layout):
        """
        フォーム風グループボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # フォーム風グループボックス
        form_group = QGroupBox("ユーザー情報入力")
        form_group.setStyleSheet("""
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
        
        form_layout = QVBoxLayout()
        
        # 名前入力
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("名前:"))
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("山田太郎")
        name_layout.addWidget(self.name_edit)
        form_layout.addLayout(name_layout)
        
        # 年齢入力
        age_layout = QHBoxLayout()
        age_layout.addWidget(QLabel("年齢:"))
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setRange(0, 120)
        self.age_spinbox.setValue(25)
        age_layout.addWidget(self.age_spinbox)
        age_layout.addWidget(QLabel("歳"))
        age_layout.addStretch()
        form_layout.addLayout(age_layout)
        
        # 性別選択
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QLabel("性別:"))
        self.gender_group = QButtonGroup()
        self.male_radio = QRadioButton("男性")
        self.female_radio = QRadioButton("女性")
        self.other_radio = QRadioButton("その他")
        self.male_radio.setChecked(True)
        
        self.gender_group.addButton(self.male_radio)
        self.gender_group.addButton(self.female_radio)
        self.gender_group.addButton(self.other_radio)
        
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_layout.addWidget(self.other_radio)
        gender_layout.addStretch()
        form_layout.addLayout(gender_layout)
        
        # 送信ボタン
        submit_btn = QPushButton("情報を送信")
        submit_btn.clicked.connect(self.submit_user_info)
        submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        form_layout.addWidget(submit_btn)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
    def create_settings_groupbox_section(self, layout):
        """
        設定グループボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 設定グループボックス
        settings_group = QGroupBox("アプリケーション設定")
        settings_group.setStyleSheet("""
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
        
        settings_layout = QVBoxLayout()
        
        # 音量設定
        volume_layout = QVBoxLayout()
        volume_layout.addWidget(QLabel("音量:"))
        
        volume_control_layout = QHBoxLayout()
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.update_volume_display)
        
        self.volume_label = QLabel("50%")
        self.volume_label.setMinimumWidth(40)
        
        volume_control_layout.addWidget(self.volume_slider)
        volume_control_layout.addWidget(self.volume_label)
        
        volume_layout.addLayout(volume_control_layout)
        settings_layout.addLayout(volume_layout)
        
        # テーマ選択
        theme_layout = QVBoxLayout()
        theme_layout.addWidget(QLabel("テーマ:"))
        
        self.theme_group = QButtonGroup()
        self.light_theme = QRadioButton("ライトテーマ")
        self.dark_theme = QRadioButton("ダークテーマ")
        self.auto_theme = QRadioButton("自動（システムに従う）")
        self.light_theme.setChecked(True)
        
        self.theme_group.addButton(self.light_theme)
        self.theme_group.addButton(self.dark_theme)
        self.theme_group.addButton(self.auto_theme)
        
        theme_layout.addWidget(self.light_theme)
        theme_layout.addWidget(self.dark_theme)
        theme_layout.addWidget(self.auto_theme)
        
        settings_layout.addLayout(theme_layout)
        
        # その他設定
        other_settings_layout = QVBoxLayout()
        self.auto_save_checkbox = QCheckBox("自動保存を有効にする")
        self.auto_save_checkbox.setChecked(True)
        self.startup_checkbox = QCheckBox("システム起動時に開始")
        self.update_checkbox = QCheckBox("自動アップデートを確認")
        self.update_checkbox.setChecked(True)
        
        other_settings_layout.addWidget(self.auto_save_checkbox)
        other_settings_layout.addWidget(self.startup_checkbox)
        other_settings_layout.addWidget(self.update_checkbox)
        
        settings_layout.addLayout(other_settings_layout)
        
        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)
        
    def create_nested_groupbox_section(self, layout):
        """
        ネストしたグループボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # メイングループボックス
        main_group = QGroupBox("ネストしたグループボックス")
        main_group.setStyleSheet("""
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
        
        main_layout = QVBoxLayout()
        
        # サブグループ1: ネットワーク設定
        network_group = QGroupBox("ネットワーク設定")
        network_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #e67e22;
                border-radius: 4px;
                margin-top: 5px;
                padding-top: 8px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 3px 0 3px;
                color: #d35400;
                background-color: white;
            }
        """)
        
        network_layout = QVBoxLayout()
        self.proxy_checkbox = QCheckBox("プロキシを使用")
        self.ssl_checkbox = QCheckBox("SSL/TLS暗号化を使用")
        self.ssl_checkbox.setChecked(True)
        
        network_layout.addWidget(self.proxy_checkbox)
        network_layout.addWidget(self.ssl_checkbox)
        network_group.setLayout(network_layout)
        
        # サブグループ2: セキュリティ設定
        security_group = QGroupBox("セキュリティ設定")
        security_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #e67e22;
                border-radius: 4px;
                margin-top: 5px;
                padding-top: 8px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 3px 0 3px;
                color: #d35400;
                background-color: white;
            }
        """)
        
        security_layout = QVBoxLayout()
        self.remember_password_checkbox = QCheckBox("パスワードを記憶")
        self.two_factor_checkbox = QCheckBox("二段階認証を有効化")
        
        security_layout.addWidget(self.remember_password_checkbox)
        security_layout.addWidget(self.two_factor_checkbox)
        security_group.setLayout(security_layout)
        
        main_layout.addWidget(network_group)
        main_layout.addWidget(security_group)
        main_group.setLayout(main_layout)
        layout.addWidget(main_group)
        
    def create_styled_groupbox_section(self, layout):
        """
        スタイル付きグループボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # スタイル付きグループボックス
        styled_group = QGroupBox("カスタムスタイル")
        styled_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 3px solid #e74c3c;
                border-radius: 10px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: #fdf2f2;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 8px 0 8px;
                color: #c0392b;
                background-color: #fdf2f2;
                font-size: 14px;
            }
        """)
        
        styled_layout = QVBoxLayout()
        
        # カスタムスタイルの説明
        style_info = QLabel("このグループボックスはカスタムスタイルが適用されています。\n背景色、ボーダー、フォントなどを自由にカスタマイズできます。")
        style_info.setWordWrap(True)
        style_info.setStyleSheet("""
            QLabel {
                color: #7b2d26;
                background-color: #f8d7da;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #f5c6cb;
            }
        """)
        styled_layout.addWidget(style_info)
        
        # アクションボタン
        action_layout = QHBoxLayout()
        
        primary_btn = QPushButton("プライマリ")
        secondary_btn = QPushButton("セカンダリ")
        
        primary_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        secondary_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #c0392b;
                border: 2px solid #c0392b;
                padding: 8px 18px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
                color: white;
            }
        """)
        
        primary_btn.clicked.connect(lambda: self.log_action("スタイル付きグループ - プライマリボタンがクリックされました"))
        secondary_btn.clicked.connect(lambda: self.log_action("スタイル付きグループ - セカンダリボタンがクリックされました"))
        
        action_layout.addWidget(primary_btn)
        action_layout.addWidget(secondary_btn)
        action_layout.addStretch()
        
        styled_layout.addLayout(action_layout)
        styled_group.setLayout(styled_layout)
        layout.addWidget(styled_group)
        
    def create_result_section(self, layout):
        """
        結果表示セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 結果表示グループ
        result_group = QGroupBox("操作ログ")
        result_group.setStyleSheet("""
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
        
        result_layout = QVBoxLayout()
        
        self.result_display = QTextEdit()
        self.result_display.setMaximumHeight(120)
        self.result_display.setPlaceholderText("操作の結果がここに表示されます...")
        self.result_display.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Courier New', monospace;
            }
        """)
        result_layout.addWidget(self.result_display)
        
        # クリアボタン
        clear_btn = QPushButton("ログをクリア")
        clear_btn.clicked.connect(self.clear_log)
        clear_btn.setStyleSheet("""
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
        result_layout.addWidget(clear_btn)
        
        result_group.setLayout(result_layout)
        layout.addWidget(result_group)
        
    def log_action(self, message):
        """
        アクションをログに記録
        
        Args:
            message (str): ログメッセージ
        """
        self.result_display.append(f"[{self.__class__.__name__}] {message}")
        
    def on_checkable_group_toggled(self, checked):
        """
        チェック可能グループボックスの状態変更処理
        
        Args:
            checked (bool): チェック状態
        """
        status = "有効" if checked else "無効"
        self.log_action(f"通知設定グループが{status}になりました")
        
    def update_volume_display(self, value):
        """
        音量表示の更新
        
        Args:
            value (int): 音量値
        """
        self.volume_label.setText(f"{value}%")
        
    def submit_user_info(self):
        """
        ユーザー情報の送信
        """
        name = self.name_edit.text().strip()
        age = self.age_spinbox.value()
        
        # 性別の取得
        if self.male_radio.isChecked():
            gender = "男性"
        elif self.female_radio.isChecked():
            gender = "女性"
        else:
            gender = "その他"
            
        if not name:
            self.log_action("エラー: 名前が入力されていません")
            return
            
        self.log_action(f"ユーザー情報を送信しました - 名前: {name}, 年齢: {age}歳, 性別: {gender}")
        
    def clear_log(self):
        """
        ログのクリア
        """
        self.result_display.clear()


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QGroupBoxの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = GroupBoxDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 