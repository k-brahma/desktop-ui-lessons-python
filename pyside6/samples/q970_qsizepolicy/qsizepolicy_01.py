"""
QSizePolicy基本サンプル - サイズポリシー

このモジュールは、PySide6のQSizePolicyクラスの基本的な使用方法を示します。
QSizePolicyは、ウィジェットがレイアウト内でどのようにサイズ変更されるかを制御します。

主要な学習ポイント:
- サイズポリシーの種類と効果
- 水平・垂直方向の独立制御
- ストレッチファクターの使用
- 最小・最大・推奨サイズの設定
- 実用的なレイアウト例

"""

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class SizePolicyDemoWindow(QWidget):
    """
    QSizePolicyの使用例を示すウィンドウクラス
    
    様々なサイズポリシーの動作を実演します。
    """
    
    def __init__(self):
        """
        SizePolicyDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とサイズポリシーサンプルの作成を行います。
        """
        super().__init__()
        self.demo_widgets = []
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQSizePolicyの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QSizePolicy基本サンプル - サイズポリシー")
        self.setGeometry(200, 200, 1000, 700)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # タイトル
        self.create_title_section(main_layout)
        
        # 水平レイアウトで左右に分割
        horizontal_layout = QHBoxLayout()
        
        # 左側：コントロールパネル
        self.create_control_panel(horizontal_layout)
        
        # 右側：デモエリア
        self.create_demo_area(horizontal_layout)
        
        main_layout.addLayout(horizontal_layout)
        
        # ログエリア
        self.create_log_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QSizePolicy デモンストレーション")
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
        
    def create_control_panel(self, layout):
        """
        コントロールパネルの作成
        
        Args:
            layout (QHBoxLayout): 追加先のレイアウト
        """
        control_widget = QWidget()
        control_widget.setFixedWidth(350)
        control_layout = QVBoxLayout()
        control_widget.setLayout(control_layout)
        
        # サイズポリシー設定
        self.create_policy_settings_section(control_layout)
        
        # ストレッチ設定
        self.create_stretch_settings_section(control_layout)
        
        # サイズ制約設定
        self.create_size_constraints_section(control_layout)
        
        # デモボタン
        self.create_demo_buttons_section(control_layout)
        
        layout.addWidget(control_widget)
        
    def create_policy_settings_section(self, layout):
        """
        ポリシー設定セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        policy_group = QGroupBox("サイズポリシー設定")
        policy_group.setStyleSheet("""
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
        
        policy_layout = QVBoxLayout()
        
        # 水平ポリシー
        h_policy_layout = QHBoxLayout()
        h_policy_layout.addWidget(QLabel("水平:"))
        self.h_policy_combo = QComboBox()
        self.h_policy_combo.addItems([
            "Fixed",
            "Minimum", 
            "Maximum",
            "Preferred",
            "Expanding",
            "MinimumExpanding",
            "Ignored"
        ])
        self.h_policy_combo.setCurrentText("Preferred")
        h_policy_layout.addWidget(self.h_policy_combo)
        policy_layout.addLayout(h_policy_layout)
        
        # 垂直ポリシー
        v_policy_layout = QHBoxLayout()
        v_policy_layout.addWidget(QLabel("垂直:"))
        self.v_policy_combo = QComboBox()
        self.v_policy_combo.addItems([
            "Fixed",
            "Minimum",
            "Maximum", 
            "Preferred",
            "Expanding",
            "MinimumExpanding",
            "Ignored"
        ])
        self.v_policy_combo.setCurrentText("Preferred")
        v_policy_layout.addWidget(self.v_policy_combo)
        policy_layout.addLayout(v_policy_layout)
        
        # 適用ボタン
        apply_policy_btn = QPushButton("ポリシーを適用")
        apply_policy_btn.clicked.connect(self.apply_size_policy)
        apply_policy_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        policy_layout.addWidget(apply_policy_btn)
        
        policy_group.setLayout(policy_layout)
        layout.addWidget(policy_group)
        
    def create_stretch_settings_section(self, layout):
        """
        ストレッチ設定セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        stretch_group = QGroupBox("ストレッチファクター")
        stretch_group.setStyleSheet("""
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
        
        stretch_layout = QVBoxLayout()
        
        # 水平ストレッチ
        h_stretch_layout = QHBoxLayout()
        h_stretch_layout.addWidget(QLabel("水平:"))
        self.h_stretch_spinbox = QSpinBox()
        self.h_stretch_spinbox.setRange(0, 10)
        self.h_stretch_spinbox.setValue(1)
        h_stretch_layout.addWidget(self.h_stretch_spinbox)
        stretch_layout.addLayout(h_stretch_layout)
        
        # 垂直ストレッチ
        v_stretch_layout = QHBoxLayout()
        v_stretch_layout.addWidget(QLabel("垂直:"))
        self.v_stretch_spinbox = QSpinBox()
        self.v_stretch_spinbox.setRange(0, 10)
        self.v_stretch_spinbox.setValue(1)
        v_stretch_layout.addWidget(self.v_stretch_spinbox)
        stretch_layout.addLayout(v_stretch_layout)
        
        stretch_group.setLayout(stretch_layout)
        layout.addWidget(stretch_group)
        
    def create_size_constraints_section(self, layout):
        """
        サイズ制約設定セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        size_group = QGroupBox("サイズ制約")
        size_group.setStyleSheet("""
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
        
        size_layout = QVBoxLayout()
        
        # 最小サイズ
        min_size_layout = QHBoxLayout()
        min_size_layout.addWidget(QLabel("最小:"))
        self.min_width_spinbox = QSpinBox()
        self.min_width_spinbox.setRange(0, 500)
        self.min_width_spinbox.setValue(50)
        min_size_layout.addWidget(self.min_width_spinbox)
        min_size_layout.addWidget(QLabel("×"))
        self.min_height_spinbox = QSpinBox()
        self.min_height_spinbox.setRange(0, 500)
        self.min_height_spinbox.setValue(30)
        min_size_layout.addWidget(self.min_height_spinbox)
        size_layout.addLayout(min_size_layout)
        
        # 最大サイズ
        max_size_layout = QHBoxLayout()
        max_size_layout.addWidget(QLabel("最大:"))
        self.max_width_spinbox = QSpinBox()
        self.max_width_spinbox.setRange(0, 1000)
        self.max_width_spinbox.setValue(300)
        max_size_layout.addWidget(self.max_width_spinbox)
        max_size_layout.addWidget(QLabel("×"))
        self.max_height_spinbox = QSpinBox()
        self.max_height_spinbox.setRange(0, 1000)
        self.max_height_spinbox.setValue(200)
        max_size_layout.addWidget(self.max_height_spinbox)
        size_layout.addLayout(max_size_layout)
        
        # サイズ制約適用
        apply_size_btn = QPushButton("サイズ制約を適用")
        apply_size_btn.clicked.connect(self.apply_size_constraints)
        apply_size_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d68910;
            }
        """)
        size_layout.addWidget(apply_size_btn)
        
        size_group.setLayout(size_layout)
        layout.addWidget(size_group)
        
    def create_demo_buttons_section(self, layout):
        """
        デモボタンセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        demo_group = QGroupBox("デモパターン")
        demo_group.setStyleSheet("""
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
        
        demo_layout = QVBoxLayout()
        
        # 基本レイアウト
        basic_layout_btn = QPushButton("基本レイアウト")
        basic_layout_btn.clicked.connect(self.demo_basic_layout)
        basic_layout_btn.setStyleSheet(self.get_button_style("#27ae60"))
        demo_layout.addWidget(basic_layout_btn)
        
        # フォームレイアウト
        form_layout_btn = QPushButton("フォームレイアウト")
        form_layout_btn.clicked.connect(self.demo_form_layout)
        form_layout_btn.setStyleSheet(self.get_button_style("#e67e22"))
        demo_layout.addWidget(form_layout_btn)
        
        # ツールバーレイアウト
        toolbar_layout_btn = QPushButton("ツールバー")
        toolbar_layout_btn.clicked.connect(self.demo_toolbar_layout)
        toolbar_layout_btn.setStyleSheet(self.get_button_style("#16a085"))
        demo_layout.addWidget(toolbar_layout_btn)
        
        # クリア
        clear_btn = QPushButton("クリア")
        clear_btn.clicked.connect(self.clear_demo_area)
        clear_btn.setStyleSheet(self.get_button_style("#95a5a6"))
        demo_layout.addWidget(clear_btn)
        
        demo_group.setLayout(demo_layout)
        layout.addWidget(demo_group)
        
    def create_demo_area(self, layout):
        """
        デモエリアの作成
        
        Args:
            layout (QHBoxLayout): 追加先のレイアウト
        """
        demo_area_group = QGroupBox("サイズポリシー デモエリア")
        demo_area_group.setStyleSheet("""
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
        
        demo_area_layout = QVBoxLayout()
        
        # スクロールエリア
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumSize(400, 400)
        
        # デモコンテナ
        self.demo_container = QWidget()
        self.demo_layout = QVBoxLayout()
        self.demo_container.setLayout(self.demo_layout)
        
        scroll_area.setWidget(self.demo_container)
        demo_area_layout.addWidget(scroll_area)
        
        # 情報表示
        self.info_label = QLabel("デモパターンを選択してください")
        self.info_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 5px;
                color: #6c757d;
                font-style: italic;
            }
        """)
        demo_area_layout.addWidget(self.info_label)
        
        demo_area_group.setLayout(demo_area_layout)
        layout.addWidget(demo_area_group)
        
    def create_log_section(self, layout):
        """
        ログセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        self.log_display = QTextEdit()
        self.log_display.setMaximumHeight(100)
        self.log_display.setPlaceholderText("サイズポリシーの操作ログがここに表示されます...")
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
        layout.addWidget(self.log_display)
        
    def get_button_style(self, color: str) -> str:
        """ボタンスタイルの取得"""
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {color}dd;
            }}
        """
        
    def log_action(self, message: str):
        """ログに記録"""
        self.log_display.append(f"[SizePolicy] {message}")
        
    def get_size_policy(self, policy_text: str):
        """サイズポリシーの取得"""
        policy_map = {
            "Fixed": QSizePolicy.Policy.Fixed,
            "Minimum": QSizePolicy.Policy.Minimum,
            "Maximum": QSizePolicy.Policy.Maximum,
            "Preferred": QSizePolicy.Policy.Preferred,
            "Expanding": QSizePolicy.Policy.Expanding,
            "MinimumExpanding": QSizePolicy.Policy.MinimumExpanding,
            "Ignored": QSizePolicy.Policy.Ignored
        }
        return policy_map.get(policy_text, QSizePolicy.Policy.Preferred)
        
    def apply_size_policy(self):
        """サイズポリシーの適用"""
        if not self.demo_widgets:
            self.log_action("適用するウィジェットがありません")
            return
            
        h_policy = self.get_size_policy(self.h_policy_combo.currentText())
        v_policy = self.get_size_policy(self.v_policy_combo.currentText())
        h_stretch = self.h_stretch_spinbox.value()
        v_stretch = self.v_stretch_spinbox.value()
        
        for widget in self.demo_widgets:
            size_policy = QSizePolicy(h_policy, v_policy)
            size_policy.setHorizontalStretch(h_stretch)
            size_policy.setVerticalStretch(v_stretch)
            widget.setSizePolicy(size_policy)
            
        self.log_action(f"ポリシー適用: 水平={self.h_policy_combo.currentText()}, 垂直={self.v_policy_combo.currentText()}")
        self.log_action(f"ストレッチ: 水平={h_stretch}, 垂直={v_stretch}")
        
    def apply_size_constraints(self):
        """サイズ制約の適用"""
        if not self.demo_widgets:
            self.log_action("適用するウィジェットがありません")
            return
            
        min_width = self.min_width_spinbox.value()
        min_height = self.min_height_spinbox.value()
        max_width = self.max_width_spinbox.value()
        max_height = self.max_height_spinbox.value()
        
        for widget in self.demo_widgets:
            widget.setMinimumSize(QSize(min_width, min_height))
            widget.setMaximumSize(QSize(max_width, max_height))
            
        self.log_action(f"サイズ制約: 最小={min_width}×{min_height}, 最大={max_width}×{max_height}")
        
    def clear_demo_area(self):
        """デモエリアのクリア"""
        # レイアウトからウィジェットを削除
        while self.demo_layout.count():
            child = self.demo_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
                
        self.demo_widgets.clear()
        self.info_label.setText("デモパターンを選択してください")
        self.log_action("デモエリアをクリアしました")
        
    def demo_basic_layout(self):
        """基本レイアウトのデモ"""
        self.clear_demo_area()
        
        # 説明
        info_text = """基本レイアウト: 3つのボタンの異なるサイズポリシー
• ボタン1: Fixed - 固定サイズ
• ボタン2: Expanding - 拡張可能
• ボタン3: Minimum - 最小サイズ保証"""
        self.info_label.setText(info_text)
        
        # 水平レイアウト
        h_layout = QHBoxLayout()
        
        # ボタン1: Fixed
        btn1 = QPushButton("Fixed")
        btn1.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btn1.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px;")
        h_layout.addWidget(btn1)
        self.demo_widgets.append(btn1)
        
        # ボタン2: Expanding
        btn2 = QPushButton("Expanding")
        btn2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        btn2.setStyleSheet("background-color: #27ae60; color: white; padding: 10px;")
        h_layout.addWidget(btn2)
        self.demo_widgets.append(btn2)
        
        # ボタン3: Minimum
        btn3 = QPushButton("Minimum")
        btn3.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        btn3.setStyleSheet("background-color: #3498db; color: white; padding: 10px;")
        h_layout.addWidget(btn3)
        self.demo_widgets.append(btn3)
        
        container = QWidget()
        container.setLayout(h_layout)
        self.demo_layout.addWidget(container)
        
        self.log_action("基本レイアウトデモを作成しました")
        
    def demo_form_layout(self):
        """フォームレイアウトのデモ"""
        self.clear_demo_area()
        
        info_text = """フォームレイアウト: ラベルとフィールドの配置
• ラベル: Fixed - 必要な分だけ
• テキストフィールド: Expanding - 残りスペースを使用"""
        self.info_label.setText(info_text)
        
        # フォーム行1
        row1_layout = QHBoxLayout()
        label1 = QLabel("名前:")
        label1.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        label1.setStyleSheet("background-color: #f39c12; color: white; padding: 5px;")
        
        field1 = QLabel("入力フィールド（Expanding）")
        field1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        field1.setStyleSheet("background-color: #ecf0f1; border: 1px solid #bdc3c7; padding: 5px;")
        
        row1_layout.addWidget(label1)
        row1_layout.addWidget(field1)
        self.demo_widgets.extend([label1, field1])
        
        # フォーム行2
        row2_layout = QHBoxLayout()
        label2 = QLabel("メールアドレス:")
        label2.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        label2.setStyleSheet("background-color: #f39c12; color: white; padding: 5px;")
        
        field2 = QLabel("入力フィールド（Expanding）")
        field2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        field2.setStyleSheet("background-color: #ecf0f1; border: 1px solid #bdc3c7; padding: 5px;")
        
        row2_layout.addWidget(label2)
        row2_layout.addWidget(field2)
        self.demo_widgets.extend([label2, field2])
        
        # コンテナに追加
        container1 = QWidget()
        container1.setLayout(row1_layout)
        container2 = QWidget()
        container2.setLayout(row2_layout)
        
        self.demo_layout.addWidget(container1)
        self.demo_layout.addWidget(container2)
        
        self.log_action("フォームレイアウトデモを作成しました")
        
    def demo_toolbar_layout(self):
        """ツールバーレイアウトのデモ"""
        self.clear_demo_area()
        
        info_text = """ツールバーレイアウト: ボタンとスペーサーの配置
• ツールボタン: Fixed - 統一サイズ
• スペーサー: Expanding - 残りスペースを埋める
• 設定ボタン: Fixed - 右端に配置"""
        self.info_label.setText(info_text)
        
        toolbar_layout = QHBoxLayout()
        
        # ツールボタン群
        for i, (text, color) in enumerate([("新規", "#3498db"), ("開く", "#27ae60"), ("保存", "#e74c3c")]):
            btn = QPushButton(text)
            btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            btn.setFixedSize(60, 30)
            btn.setStyleSheet(f"background-color: {color}; color: white;")
            toolbar_layout.addWidget(btn)
            self.demo_widgets.append(btn)
            
        # スペーサー
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        spacer.setStyleSheet("background-color: #f8f9fa; border: 1px dashed #dee2e6;")
        toolbar_layout.addWidget(spacer)
        self.demo_widgets.append(spacer)
        
        # 設定ボタン
        settings_btn = QPushButton("設定")
        settings_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        settings_btn.setFixedSize(60, 30)
        settings_btn.setStyleSheet("background-color: #95a5a6; color: white;")
        toolbar_layout.addWidget(settings_btn)
        self.demo_widgets.append(settings_btn)
        
        container = QWidget()
        container.setLayout(toolbar_layout)
        self.demo_layout.addWidget(container)
        
        self.log_action("ツールバーレイアウトデモを作成しました")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QSizePolicyの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = SizePolicyDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 