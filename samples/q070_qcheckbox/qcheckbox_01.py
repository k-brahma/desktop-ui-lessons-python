"""
QCheckBox基本サンプル - チェックボックスとラジオボタンの基本操作

このモジュールは、PySide6のQCheckBoxとQRadioButtonクラスの基本的な使用方法を示します。
QCheckBoxは複数選択可能なオプション、QRadioButtonは単一選択のオプションに使用されます。

主要な学習ポイント:
- 基本的なチェックボックスの作成と操作
- ラジオボタンによる排他選択
- 三状態チェックボックス（部分選択）
- チェック状態の管理と同期
- シグナルとスロットによるイベント処理

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class CheckBoxDemoWindow(QWidget):
    """
    QCheckBoxとQRadioButtonの使用例を示すウィンドウクラス
    
    様々なタイプの選択コントロールの機能を実演します。
    """
    
    def __init__(self):
        """
        CheckBoxDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とチェックボックスサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々な選択コントロールの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QCheckBox基本サンプル - チェックボックスとラジオボタン")
        self.setGeometry(200, 200, 700, 800)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_title_section(main_layout)
        self.create_basic_checkbox_section(main_layout)
        self.create_radio_button_section(main_layout)
        self.create_tristate_section(main_layout)
        self.create_notification_section(main_layout)
        self.create_interactive_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QCheckBox & QRadioButton デモンストレーション")
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
        
    def create_basic_checkbox_section(self, layout):
        """
        基本的なチェックボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 基本チェックボックスグループ
        checkbox_group = QGroupBox("基本的なチェックボックス")
        checkbox_group.setStyleSheet("""
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
        
        checkbox_layout = QVBoxLayout()
        
        # 基本的なチェックボックス群
        self.basic_checkboxes = []
        basic_options = [
            ("auto_save", "自動保存を有効にする"),
            ("notifications", "通知を受け取る"),
            ("dark_mode", "ダークモードを使用する"),
            ("sound_effects", "効果音を再生する"),
            ("auto_update", "自動アップデートを有効にする")
        ]
        
        for key, text in basic_options:
            checkbox = QCheckBox(text)
            checkbox.setObjectName(key)
            checkbox.toggled.connect(lambda checked, cb=checkbox: self.on_checkbox_toggled(cb, checked))
            self.basic_checkboxes.append(checkbox)
            checkbox_layout.addWidget(checkbox)
            
        # デフォルトでいくつかをチェック
        self.basic_checkboxes[0].setChecked(True)  # 自動保存
        self.basic_checkboxes[1].setChecked(True)  # 通知
        
        checkbox_group.setLayout(checkbox_layout)
        layout.addWidget(checkbox_group)
        
    def create_radio_button_section(self, layout):
        """
        ラジオボタンセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # ラジオボタングループ
        radio_group = QGroupBox("ラジオボタン（単一選択）")
        radio_group.setStyleSheet("""
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
        
        radio_layout = QVBoxLayout()
        
        # テーマ選択
        theme_label = QLabel("テーマ選択:")
        theme_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        radio_layout.addWidget(theme_label)
        
        self.theme_group = QButtonGroup()
        self.theme_radios = []
        theme_options = [
            ("light", "ライトテーマ", True),
            ("dark", "ダークテーマ", False),
            ("auto", "システムに従う", False)
        ]
        
        for key, text, default in theme_options:
            radio = QRadioButton(text)
            radio.setObjectName(key)
            radio.setChecked(default)
            radio.toggled.connect(lambda checked, rb=radio: self.on_radio_toggled(rb, checked))
            self.theme_group.addButton(radio)
            self.theme_radios.append(radio)
            radio_layout.addWidget(radio)
            
        radio_layout.addWidget(QLabel(""))  # スペーサー
        
        # 言語選択
        lang_label = QLabel("言語選択:")
        lang_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        radio_layout.addWidget(lang_label)
        
        self.lang_group = QButtonGroup()
        self.lang_radios = []
        lang_options = [
            ("ja", "日本語", True),
            ("en", "English", False),
            ("zh", "中文", False),
            ("ko", "한국어", False)
        ]
        
        for key, text, default in lang_options:
            radio = QRadioButton(text)
            radio.setObjectName(key)
            radio.setChecked(default)
            radio.toggled.connect(lambda checked, rb=radio: self.on_radio_toggled(rb, checked))
            self.lang_group.addButton(radio)
            self.lang_radios.append(radio)
            radio_layout.addWidget(radio)
            
        radio_group.setLayout(radio_layout)
        layout.addWidget(radio_group)
        
    def create_tristate_section(self, layout):
        """
        三状態チェックボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 三状態グループ
        tristate_group = QGroupBox("三状態チェックボックス（親子関係）")
        tristate_group.setStyleSheet("""
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
        
        tristate_layout = QVBoxLayout()
        
        # 親チェックボックス（すべて選択）
        self.select_all_checkbox = QCheckBox("すべて選択")
        self.select_all_checkbox.setTristate(True)
        self.select_all_checkbox.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.select_all_checkbox.stateChanged.connect(self.on_select_all_changed)
        tristate_layout.addWidget(self.select_all_checkbox)
        
        # 子チェックボックス群
        self.child_checkboxes = []
        child_options = [
            "ドキュメントファイル",
            "画像ファイル",
            "動画ファイル",
            "音声ファイル",
            "アーカイブファイル"
        ]
        
        child_container = QWidget()
        child_layout = QVBoxLayout()
        child_layout.setContentsMargins(30, 0, 0, 0)  # 左側にインデント
        
        for option in child_options:
            checkbox = QCheckBox(option)
            checkbox.toggled.connect(self.update_select_all_state)
            self.child_checkboxes.append(checkbox)
            child_layout.addWidget(checkbox)
            
        child_container.setLayout(child_layout)
        tristate_layout.addWidget(child_container)
        
        tristate_group.setLayout(tristate_layout)
        layout.addWidget(tristate_group)
        
    def create_notification_section(self, layout):
        """
        通知設定セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 通知設定グループ
        notification_group = QGroupBox("通知設定")
        notification_group.setCheckable(True)
        notification_group.setChecked(True)
        notification_group.toggled.connect(self.on_notification_group_toggled)
        notification_group.setStyleSheet("""
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
        
        notification_layout = QVBoxLayout()
        
        # 通知方法選択
        self.notification_checkboxes = []
        notification_options = [
            ("email", "メール通知"),
            ("push", "プッシュ通知"),
            ("sms", "SMS通知"),
            ("desktop", "デスクトップ通知")
        ]
        
        for key, text in notification_options:
            checkbox = QCheckBox(text)
            checkbox.setObjectName(key)
            self.notification_checkboxes.append(checkbox)
            notification_layout.addWidget(checkbox)
            
        # デフォルト設定
        self.notification_checkboxes[0].setChecked(True)  # メール
        self.notification_checkboxes[3].setChecked(True)  # デスクトップ
        
        notification_group.setLayout(notification_layout)
        layout.addWidget(notification_group)
        
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
        
        # コントロールボタン
        button_layout = QHBoxLayout()
        
        get_status_btn = QPushButton("選択状態を取得")
        get_status_btn.clicked.connect(self.get_selection_status)
        get_status_btn.setStyleSheet("""
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
        button_layout.addWidget(get_status_btn)
        
        toggle_all_btn = QPushButton("すべて切り替え")
        toggle_all_btn.clicked.connect(self.toggle_all_checkboxes)
        toggle_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #d68910;
            }
        """)
        button_layout.addWidget(toggle_all_btn)
        
        reset_btn = QPushButton("デフォルトに戻す")
        reset_btn.clicked.connect(self.reset_to_defaults)
        reset_btn.setStyleSheet("""
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
        button_layout.addWidget(reset_btn)
        
        interactive_layout.addLayout(button_layout)
        
        # 状態表示エリア
        self.status_display = QTextEdit()
        self.status_display.setMaximumHeight(150)
        self.status_display.setPlaceholderText("選択状態がここに表示されます...")
        self.status_display.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 5px;
                font-family: 'Courier New', monospace;
            }
        """)
        interactive_layout.addWidget(self.status_display)
        
        interactive_group.setLayout(interactive_layout)
        layout.addWidget(interactive_group)
        
    def on_checkbox_toggled(self, checkbox, checked):
        """
        チェックボックスの状態変更処理
        
        Args:
            checkbox (QCheckBox): 変更されたチェックボックス
            checked (bool): チェック状態
        """
        name = checkbox.objectName() or checkbox.text()
        status = "有効" if checked else "無効"
        print(f"{name}: {status}")
        
    def on_radio_toggled(self, radio, checked):
        """
        ラジオボタンの状態変更処理
        
        Args:
            radio (QRadioButton): 変更されたラジオボタン
            checked (bool): 選択状態
        """
        if checked:  # 選択された時のみ処理
            name = radio.objectName() or radio.text()
            print(f"選択された: {name}")
            
    def on_select_all_changed(self, state):
        """
        すべて選択チェックボックスの状態変更処理
        
        Args:
            state (int): チェック状態（0: 未選択, 1: 部分選択, 2: 全選択）
        """
        if state == Qt.CheckState.Checked.value:  # 全選択
            for checkbox in self.child_checkboxes:
                checkbox.setChecked(True)
        elif state == Qt.CheckState.Unchecked.value:  # 全解除
            for checkbox in self.child_checkboxes:
                checkbox.setChecked(False)
        # 部分選択(PartiallyChecked)の場合は何もしない
        
    def update_select_all_state(self):
        """
        子チェックボックスの状態に基づいて親チェックボックスの状態を更新
        """
        checked_count = sum(1 for cb in self.child_checkboxes if cb.isChecked())
        total_count = len(self.child_checkboxes)
        
        if checked_count == 0:
            self.select_all_checkbox.setCheckState(Qt.CheckState.Unchecked)
        elif checked_count == total_count:
            self.select_all_checkbox.setCheckState(Qt.CheckState.Checked)
        else:
            self.select_all_checkbox.setCheckState(Qt.CheckState.PartiallyChecked)
            
    def on_notification_group_toggled(self, enabled):
        """
        通知グループの有効/無効切り替え
        
        Args:
            enabled (bool): 有効かどうか
        """
        status = "有効" if enabled else "無効"
        print(f"通知設定: {status}")
        
    def get_selection_status(self):
        """
        すべての選択状態を取得して表示
        """
        status_text = "=== 選択状態 ===\n\n"
        
        # 基本チェックボックス
        status_text += "[基本設定]\n"
        for checkbox in self.basic_checkboxes:
            name = checkbox.text()
            status = "✓" if checkbox.isChecked() else "✗"
            status_text += f"  {status} {name}\n"
            
        # テーマ選択
        status_text += "\n[テーマ]\n"
        for radio in self.theme_radios:
            if radio.isChecked():
                status_text += f"  ● {radio.text()}\n"
                break
                
        # 言語選択
        status_text += "\n[言語]\n"
        for radio in self.lang_radios:
            if radio.isChecked():
                status_text += f"  ● {radio.text()}\n"
                break
                
        # ファイルタイプ選択
        status_text += "\n[ファイルタイプ]\n"
        for checkbox in self.child_checkboxes:
            name = checkbox.text()
            status = "✓" if checkbox.isChecked() else "✗"
            status_text += f"  {status} {name}\n"
            
        # 通知設定
        status_text += "\n[通知設定]\n"
        for checkbox in self.notification_checkboxes:
            name = checkbox.text()
            status = "✓" if checkbox.isChecked() else "✗"
            status_text += f"  {status} {name}\n"
            
        self.status_display.setText(status_text)
        
    def toggle_all_checkboxes(self):
        """
        すべてのチェックボックスの状態を切り替え
        """
        # 基本チェックボックス
        for checkbox in self.basic_checkboxes:
            checkbox.toggle()
            
        # 子チェックボックス
        for checkbox in self.child_checkboxes:
            checkbox.toggle()
            
        # 通知チェックボックス
        for checkbox in self.notification_checkboxes:
            checkbox.toggle()
            
    def reset_to_defaults(self):
        """
        すべての設定をデフォルト状態に戻す
        """
        # 基本チェックボックス
        for i, checkbox in enumerate(self.basic_checkboxes):
            checkbox.setChecked(i in [0, 1])  # 最初の2つのみチェック
            
        # テーマ選択（ライトテーマ）
        self.theme_radios[0].setChecked(True)
        
        # 言語選択（日本語）
        self.lang_radios[0].setChecked(True)
        
        # 子チェックボックス（すべて未選択）
        for checkbox in self.child_checkboxes:
            checkbox.setChecked(False)
            
        # 通知チェックボックス
        for i, checkbox in enumerate(self.notification_checkboxes):
            checkbox.setChecked(i in [0, 3])  # メールとデスクトップのみ
            
        self.status_display.clear()


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QCheckBoxとQRadioButtonの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = CheckBoxDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 