"""
Qt定数基本サンプル - Qt定数とフラグの活用

このモジュールは、PySide6のQtクラスの基本的な使用方法を示します。
Qtクラスは、アライメント、キーボード、マウス、ウィンドウフラグなど、
PySide6全体で使用される重要な定数を提供します。

主要な学習ポイント:
- アライメント定数の使用
- キーボードとマウスの定数
- ウィンドウフラグとウィンドウ状態
- テキスト選択とインタラクション
- フォーカスポリシーの設定

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
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


class QtConstantsWindow(QWidget):
    """
    Qt定数の使用例を示すウィンドウクラス
    
    様々なQt定数を使用したウィジェットの設定例を実演します。
    """
    
    def __init__(self):
        """
        QtConstantsWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とQt定数サンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQt定数を使用したコンポーネントを配置します。
        """
        self.setWindowTitle("Qt定数基本サンプル - 定数とフラグの活用")
        self.setGeometry(200, 200, 600, 700)
        
        # メインレイアウト
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 各セクションの作成
        self.create_title_section(layout)
        self.create_alignment_section(layout)
        self.create_text_interaction_section(layout)
        self.create_focus_policy_section(layout)
        self.create_window_flags_section(layout)
        self.create_keyboard_mouse_section(layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("Qt定数デモンストレーション")
        title_font = QFont()
        title_font.setPointSize(20)
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
        
    def create_alignment_section(self, layout):
        """
        アライメントセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        section_title = QLabel("アライメント定数の例")
        section_title.setFont(QFont("Arial", 14))
        section_title.setStyleSheet("color: #34495e; margin-top: 10px; margin-bottom: 5px; font-weight: bold;")
        layout.addWidget(section_title)
        
        # 左揃え
        left_label = QLabel("左揃えテキスト (Qt.AlignLeft)")
        # left_label.setAlignment(Qt.AlignLeft)  # デフォルトなので明示的に設定
        left_label.setStyleSheet("""
            QLabel {
                background-color: #ffe6e6;
                padding: 8px;
                border: 1px solid #ff9999;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(left_label)
        
        # 中央揃え
        center_label = QLabel("中央揃えテキスト (Qt.AlignCenter)")
        # center_label.setAlignment(Qt.AlignCenter)
        center_label.setStyleSheet("""
            QLabel {
                background-color: #e6f3ff;
                padding: 8px;
                border: 1px solid #99ccff;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(center_label)
        
        # 右揃え
        right_label = QLabel("右揃えテキスト (Qt.AlignRight)")
        # right_label.setAlignment(Qt.AlignRight)
        right_label.setStyleSheet("""
            QLabel {
                background-color: #e6ffe6;
                padding: 8px;
                border: 1px solid #99ff99;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(right_label)
        
    def create_text_interaction_section(self, layout):
        """
        テキストインタラクションセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        section_title = QLabel("テキストインタラクション定数の例")
        section_title.setFont(QFont("Arial", 14))
        section_title.setStyleSheet("color: #34495e; margin-top: 15px; margin-bottom: 5px; font-weight: bold;")
        layout.addWidget(section_title)
        
        # 選択不可テキスト
        no_select_label = QLabel("選択できないテキスト (Qt.NoTextInteraction)")
        # no_select_label.setTextInteractionFlags(Qt.NoTextInteraction)  # デフォルト
        no_select_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                padding: 8px;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(no_select_label)
        
        # マウス選択可能テキスト
        mouse_select_label = QLabel("マウスで選択可能なテキスト (Qt.TextSelectableByMouse)")
        # mouse_select_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        mouse_select_label.setStyleSheet("""
            QLabel {
                background-color: #fff3cd;
                padding: 8px;
                border: 1px solid #ffeaa7;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(mouse_select_label)
        
        # キーボード選択可能テキスト
        keyboard_select_label = QLabel("キーボードで選択可能なテキスト (Qt.TextSelectableByKeyboard)")
        # keyboard_select_label.setTextInteractionFlags(Qt.TextSelectableByKeyboard)
        keyboard_select_label.setStyleSheet("""
            QLabel {
                background-color: #d4edda;
                padding: 8px;
                border: 1px solid #c3e6cb;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(keyboard_select_label)
        
    def create_focus_policy_section(self, layout):
        """
        フォーカスポリシーセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        section_title = QLabel("フォーカスポリシー定数の例")
        section_title.setFont(QFont("Arial", 14))
        section_title.setStyleSheet("color: #34495e; margin-top: 15px; margin-bottom: 5px; font-weight: bold;")
        layout.addWidget(section_title)
        
        # フォーカスなし
        no_focus_edit = QLineEdit("フォーカスなし (Qt.NoFocus)")
        # no_focus_edit.setFocusPolicy(Qt.NoFocus)
        no_focus_edit.setReadOnly(True)
        no_focus_edit.setStyleSheet("""
            QLineEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                padding: 6px;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(no_focus_edit)
        
        # タブフォーカス
        tab_focus_edit = QLineEdit("タブでフォーカス可能 (Qt.TabFocus)")
        # tab_focus_edit.setFocusPolicy(Qt.TabFocus)
        tab_focus_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #007bff;
                padding: 6px;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(tab_focus_edit)
        
        # クリックフォーカス
        click_focus_edit = QLineEdit("クリックでフォーカス可能 (Qt.ClickFocus)")
        # click_focus_edit.setFocusPolicy(Qt.ClickFocus)
        click_focus_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #28a745;
                padding: 6px;
                border-radius: 4px;
                margin: 2px;
            }
        """)
        layout.addWidget(click_focus_edit)
        
    def create_window_flags_section(self, layout):
        """
        ウィンドウフラグセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        section_title = QLabel("ウィンドウフラグ制御")
        section_title.setFont(QFont("Arial", 14))
        section_title.setStyleSheet("color: #34495e; margin-top: 15px; margin-bottom: 5px; font-weight: bold;")
        layout.addWidget(section_title)
        
        # ウィンドウフラグ制御ボタン
        button_layout = QHBoxLayout()
        
        # 常に最前面ボタン
        self.always_on_top_btn = QPushButton("常に最前面切り替え")
        self.always_on_top_btn.clicked.connect(self.toggle_always_on_top)
        self.always_on_top_btn.setStyleSheet("""
            QPushButton {
                background-color: #6f42c1;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #5a32a3;
            }
        """)
        button_layout.addWidget(self.always_on_top_btn)
        
        # 最小化無効ボタン
        self.disable_minimize_btn = QPushButton("最小化無効切り替え")
        self.disable_minimize_btn.clicked.connect(self.toggle_minimize_disabled)
        self.disable_minimize_btn.setStyleSheet("""
            QPushButton {
                background-color: #fd7e14;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #e66100;
            }
        """)
        button_layout.addWidget(self.disable_minimize_btn)
        
        layout.addLayout(button_layout)
        
        # 状態表示
        self.window_state_label = QLabel("現在の状態: 通常ウィンドウ")
        self.window_state_label.setStyleSheet("""
            QLabel {
                background-color: #e9ecef;
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                margin: 5px 0;
            }
        """)
        layout.addWidget(self.window_state_label)
        
    def create_keyboard_mouse_section(self, layout):
        """
        キーボード・マウスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        section_title = QLabel("キーボード・マウス定数の例")
        section_title.setFont(QFont("Arial", 14))
        section_title.setStyleSheet("color: #34495e; margin-top: 15px; margin-bottom: 5px; font-weight: bold;")
        layout.addWidget(section_title)
        
        # キーボード修飾キー情報
        modifier_info = QLabel(
            "修飾キーの例:\n"
            "• Qt.ControlModifier - Ctrlキー\n"
            "• Qt.AltModifier - Altキー\n"
            "• Qt.ShiftModifier - Shiftキー\n"
            "• Qt.MetaModifier - Windowsキー/Cmdキー"
        )
        modifier_info.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                padding: 10px;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                margin: 2px;
                line-height: 1.5;
            }
        """)
        layout.addWidget(modifier_info)
        
        # マウスボタン情報
        mouse_info = QLabel(
            "マウスボタンの例:\n"
            "• Qt.LeftButton - 左クリック\n"
            "• Qt.RightButton - 右クリック\n"
            "• Qt.MiddleButton - 中クリック"
        )
        mouse_info.setStyleSheet("""
            QLabel {
                background-color: #fff3cd;
                padding: 10px;
                border: 1px solid #ffeaa7;
                border-radius: 4px;
                margin: 2px;
                line-height: 1.5;
            }
        """)
        layout.addWidget(mouse_info)
        
        # イベント検知用エリア
        self.event_display = QTextEdit()
        self.event_display.setPlaceholderText("ここをクリックまたはキーを押してイベントを確認...")
        self.event_display.setMaximumHeight(80)
        self.event_display.setStyleSheet("""
            QTextEdit {
                background-color: #e6f3ff;
                border: 2px solid #007bff;
                border-radius: 4px;
                padding: 5px;
                font-family: monospace;
            }
        """)
        layout.addWidget(self.event_display)
        
        # 状態変数
        self.is_always_on_top = False
        self.is_minimize_disabled = False
        
    def toggle_always_on_top(self):
        """
        常に最前面表示の切り替え
        """
        self.is_always_on_top = not self.is_always_on_top
        
        if self.is_always_on_top:
            # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.window_state_label.setText("現在の状態: 常に最前面")
            self.always_on_top_btn.setText("最前面解除")
        else:
            # self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.window_state_label.setText("現在の状態: 通常ウィンドウ")
            self.always_on_top_btn.setText("常に最前面切り替え")
            
        # ウィンドウを再表示（フラグ変更を適用するため）
        self.show()
        
    def toggle_minimize_disabled(self):
        """
        最小化無効の切り替え
        """
        self.is_minimize_disabled = not self.is_minimize_disabled
        
        if self.is_minimize_disabled:
            self.window_state_label.setText("現在の状態: 最小化無効")
            self.disable_minimize_btn.setText("最小化有効化")
        else:
            self.window_state_label.setText("現在の状態: 最小化可能")
            self.disable_minimize_btn.setText("最小化無効切り替え")
            
    def mousePressEvent(self, event):
        """
        マウスクリックイベントの処理
        
        Args:
            event: マウスイベント
        """
        button_name = "不明"
        # if event.button() == Qt.LeftButton:
        #     button_name = "左ボタン"
        # elif event.button() == Qt.RightButton:
        #     button_name = "右ボタン"
        # elif event.button() == Qt.MiddleButton:
        #     button_name = "中ボタン"
            
        self.event_display.append(f"マウス: {button_name} ({event.pos().x()}, {event.pos().y()})")
        super().mousePressEvent(event)
        
    def keyPressEvent(self, event):
        """
        キーボードイベントの処理
        
        Args:
            event: キーボードイベント
        """
        key_text = event.text() if event.text().isprintable() else f"特殊キー({event.key()})"
        
        modifiers = []
        # if event.modifiers() & Qt.ControlModifier:
        #     modifiers.append("Ctrl")
        # if event.modifiers() & Qt.AltModifier:
        #     modifiers.append("Alt")
        # if event.modifiers() & Qt.ShiftModifier:
        #     modifiers.append("Shift")
            
        modifier_text = "+".join(modifiers) if modifiers else "なし"
        self.event_display.append(f"キー: {key_text}, 修飾キー: {modifier_text}")
        super().keyPressEvent(event)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    Qt定数の基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = QtConstantsWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 