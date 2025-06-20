"""
QHBoxLayout基本サンプル - 水平方向レイアウト管理

このモジュールは、PySide6のQHBoxLayoutクラスの基本的な使用方法を示します。
QHBoxLayoutは、ウィジェットを水平方向（左から右）に配置するレイアウトマネージャーです。

主要な学習ポイント:
- 基本的な水平レイアウトの作成
- ウィジェットの配置とスペーシング
- ストレッチファクターによる領域配分
- QVBoxLayoutとの組み合わせ
- マージンとパディングの制御

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSlider,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class HBoxLayoutDemoWindow(QWidget):
    """
    QHBoxLayoutの使用例を示すウィンドウクラス
    
    様々な水平レイアウトのパターンと機能を実演します。
    """
    
    def __init__(self):
        """
        HBoxLayoutDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とレイアウトサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQHBoxLayoutの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QHBoxLayout基本サンプル - 水平方向レイアウト管理")
        self.setGeometry(200, 200, 800, 700)
        
        # メインレイアウト（垂直）
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_title_section(main_layout)
        self.create_basic_horizontal_section(main_layout)
        self.create_stretch_demo_section(main_layout)
        self.create_spacing_demo_section(main_layout)
        self.create_form_layout_section(main_layout)
        self.create_toolbar_section(main_layout)
        self.create_complex_layout_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QHBoxLayout デモンストレーション")
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
        
    def create_basic_horizontal_section(self, layout):
        """
        基本的な水平レイアウトセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 基本水平レイアウトグループ
        basic_group = QGroupBox("基本的な水平配置")
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
        
        # シンプルなボタン配列
        button_layout = QHBoxLayout()
        
        button1 = QPushButton("ボタン1")
        button2 = QPushButton("ボタン2")
        button3 = QPushButton("ボタン3")
        
        button1.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px;")
        button2.setStyleSheet("background-color: #3498db; color: white; padding: 8px;")
        button3.setStyleSheet("background-color: #27ae60; color: white; padding: 8px;")
        
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        
        # 説明ラベル
        desc_label = QLabel("3つのボタンが水平に配置されています")
        desc_label.setStyleSheet("color: #7f8c8d; font-style: italic; margin: 5px;")
        
        basic_layout.addWidget(desc_label)
        basic_layout.addLayout(button_layout)
        
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
    def create_stretch_demo_section(self, layout):
        """
        ストレッチファクターデモセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # ストレッチデモグループ
        stretch_group = QGroupBox("ストレッチファクターの例")
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
        
        # ストレッチなし
        no_stretch_label = QLabel("ストレッチなし（固定サイズ）:")
        no_stretch_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        stretch_layout.addWidget(no_stretch_label)
        
        no_stretch_hlayout = QHBoxLayout()
        btn_fixed1 = QPushButton("固定1")
        btn_fixed2 = QPushButton("固定2")
        btn_fixed3 = QPushButton("固定3")
        
        for btn in [btn_fixed1, btn_fixed2, btn_fixed3]:
            btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px;")
            
        no_stretch_hlayout.addWidget(btn_fixed1)
        no_stretch_hlayout.addWidget(btn_fixed2)
        no_stretch_hlayout.addWidget(btn_fixed3)
        
        stretch_layout.addLayout(no_stretch_hlayout)
        
        # ストレッチ付き
        with_stretch_label = QLabel("ストレッチ付き（比率 1:2:1）:")
        with_stretch_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        stretch_layout.addWidget(with_stretch_label)
        
        with_stretch_hlayout = QHBoxLayout()
        btn_stretch1 = QPushButton("ストレッチ1")
        btn_stretch2 = QPushButton("ストレッチ2（2倍）")
        btn_stretch3 = QPushButton("ストレッチ3")
        
        btn_stretch1.setStyleSheet("background-color: #3498db; color: white; padding: 8px;")
        btn_stretch2.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px;")
        btn_stretch3.setStyleSheet("background-color: #3498db; color: white; padding: 8px;")
        
        with_stretch_hlayout.addWidget(btn_stretch1, 1)  # ストレッチファクター 1
        with_stretch_hlayout.addWidget(btn_stretch2, 2)  # ストレッチファクター 2
        with_stretch_hlayout.addWidget(btn_stretch3, 1)  # ストレッチファクター 1
        
        stretch_layout.addLayout(with_stretch_hlayout)
        
        # スペースと固定要素の組み合わせ
        mixed_label = QLabel("固定要素とストレッチスペースの組み合わせ:")
        mixed_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        stretch_layout.addWidget(mixed_label)
        
        mixed_hlayout = QHBoxLayout()
        btn_left = QPushButton("左固定")
        btn_right = QPushButton("右固定")
        
        btn_left.setStyleSheet("background-color: #27ae60; color: white; padding: 8px;")
        btn_right.setStyleSheet("background-color: #f39c12; color: white; padding: 8px;")
        
        mixed_hlayout.addWidget(btn_left)
        mixed_hlayout.addStretch()  # 中央に伸縮可能なスペース
        mixed_hlayout.addWidget(btn_right)
        
        stretch_layout.addLayout(mixed_hlayout)
        
        stretch_group.setLayout(stretch_layout)
        layout.addWidget(stretch_group)
        
    def create_spacing_demo_section(self, layout):
        """
        スペーシングデモセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # スペーシングデモグループ
        spacing_group = QGroupBox("スペーシングとマージンの制御")
        spacing_group.setStyleSheet("""
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
        
        spacing_layout = QVBoxLayout()
        
        # スペーシング調整コントロール
        control_hlayout = QHBoxLayout()
        
        spacing_label = QLabel("スペーシング:")
        self.spacing_slider = QSlider(Qt.Orientation.Horizontal)
        self.spacing_slider.setRange(0, 50)
        self.spacing_slider.setValue(10)
        self.spacing_slider.valueChanged.connect(self.update_spacing)
        
        self.spacing_value_label = QLabel("10px")
        self.spacing_value_label.setMinimumWidth(40)
        
        control_hlayout.addWidget(spacing_label)
        control_hlayout.addWidget(self.spacing_slider, 1)
        control_hlayout.addWidget(self.spacing_value_label)
        
        spacing_layout.addLayout(control_hlayout)
        
        # スペーシングが適用されるサンプルレイアウト
        self.demo_spacing_layout = QHBoxLayout()
        
        for i in range(4):
            btn = QPushButton(f"ボタン{i+1}")
            btn.setStyleSheet("background-color: #9b59b6; color: white; padding: 8px;")
            self.demo_spacing_layout.addWidget(btn)
            
        # 初期スペーシング設定
        self.demo_spacing_layout.setSpacing(10)
        
        spacing_layout.addLayout(self.demo_spacing_layout)
        
        spacing_group.setLayout(spacing_layout)
        layout.addWidget(spacing_group)
        
    def create_form_layout_section(self, layout):
        """
        フォームレイアウトセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # フォームレイアウトグループ
        form_group = QGroupBox("フォーム風レイアウト")
        form_group.setStyleSheet("""
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
        
        form_layout = QVBoxLayout()
        
        # 名前入力行
        name_hlayout = QHBoxLayout()
        name_label = QLabel("名前:")
        name_label.setMinimumWidth(80)
        name_edit = QLineEdit()
        name_edit.setPlaceholderText("山田太郎")
        
        name_hlayout.addWidget(name_label)
        name_hlayout.addWidget(name_edit, 1)  # 入力フィールドが拡張
        
        # 年齢入力行
        age_hlayout = QHBoxLayout()
        age_label = QLabel("年齢:")
        age_label.setMinimumWidth(80)
        age_spinbox = QSpinBox()
        age_spinbox.setRange(0, 120)
        age_spinbox.setValue(25)
        age_unit_label = QLabel("歳")
        
        age_hlayout.addWidget(age_label)
        age_hlayout.addWidget(age_spinbox)
        age_hlayout.addWidget(age_unit_label)
        age_hlayout.addStretch()  # 右側に余白
        
        # 設定チェックボックス行
        settings_hlayout = QHBoxLayout()
        settings_label = QLabel("設定:")
        settings_label.setMinimumWidth(80)
        checkbox1 = QCheckBox("メール通知")
        checkbox2 = QCheckBox("プライベート")
        
        settings_hlayout.addWidget(settings_label)
        settings_hlayout.addWidget(checkbox1)
        settings_hlayout.addWidget(checkbox2)
        settings_hlayout.addStretch()
        
        form_layout.addLayout(name_hlayout)
        form_layout.addLayout(age_hlayout)
        form_layout.addLayout(settings_hlayout)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
    def create_toolbar_section(self, layout):
        """
        ツールバー風セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # ツールバーグループ
        toolbar_group = QGroupBox("ツールバー風レイアウト")
        toolbar_group.setStyleSheet("""
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
        
        toolbar_layout = QVBoxLayout()
        
        # メインツールバー
        main_toolbar = QHBoxLayout()
        
        # 左側のツールボタン群
        new_btn = QPushButton("新規")
        open_btn = QPushButton("開く")
        save_btn = QPushButton("保存")
        
        for btn in [new_btn, open_btn, save_btn]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #34495e;
                    color: white;
                    border: none;
                    padding: 8px 12px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #2c3e50;
                }
            """)
            
        main_toolbar.addWidget(new_btn)
        main_toolbar.addWidget(open_btn)
        main_toolbar.addWidget(save_btn)
        
        # セパレーター（スペース）
        main_toolbar.addSpacing(20)
        
        # 中央のツールボタン群
        cut_btn = QPushButton("切り取り")
        copy_btn = QPushButton("コピー")
        paste_btn = QPushButton("貼り付け")
        
        for btn in [cut_btn, copy_btn, paste_btn]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #16a085;
                    color: white;
                    border: none;
                    padding: 8px 12px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #138d75;
                }
            """)
            
        main_toolbar.addWidget(cut_btn)
        main_toolbar.addWidget(copy_btn)
        main_toolbar.addWidget(paste_btn)
        
        # 右側に検索ボックス
        main_toolbar.addStretch()  # 左右を分離
        
        search_label = QLabel("検索:")
        search_edit = QLineEdit()
        search_edit.setPlaceholderText("検索語を入力...")
        search_edit.setMaximumWidth(200)
        
        main_toolbar.addWidget(search_label)
        main_toolbar.addWidget(search_edit)
        
        toolbar_layout.addLayout(main_toolbar)
        
        toolbar_group.setLayout(toolbar_layout)
        layout.addWidget(toolbar_group)
        
    def create_complex_layout_section(self, layout):
        """
        複合レイアウトセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 複合レイアウトグループ
        complex_group = QGroupBox("複合レイアウト（ヘッダー・コンテンツ・フッター）")
        complex_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #8e44ad;
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
        
        complex_layout = QVBoxLayout()
        
        # ヘッダー（水平レイアウト）
        header_layout = QHBoxLayout()
        
        app_title = QLabel("アプリケーション名")
        app_title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        app_title.setStyleSheet("color: #2c3e50; padding: 5px;")
        
        minimize_btn = QPushButton("−")
        maximize_btn = QPushButton("□")
        close_btn = QPushButton("×")
        
        for btn in [minimize_btn, maximize_btn, close_btn]:
            btn.setFixedSize(30, 30)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
            """)
            
        header_layout.addWidget(app_title)
        header_layout.addStretch()
        header_layout.addWidget(minimize_btn)
        header_layout.addWidget(maximize_btn)
        header_layout.addWidget(close_btn)
        
        # コンテンツエリア
        content_area = QTextEdit()
        content_area.setPlaceholderText("ここにメインコンテンツが表示されます...")
        content_area.setMaximumHeight(100)
        content_area.setStyleSheet("""
            QTextEdit {
                background-color: #ecf0f1;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        
        # フッター（水平レイアウト）
        footer_layout = QHBoxLayout()
        
        status_label = QLabel("準備完了")
        status_label.setStyleSheet("color: #27ae60; padding: 5px;")
        
        progress_label = QLabel("進行状況:")
        progress_label.setStyleSheet("padding: 5px;")
        
        # プログレスバーの代わりにラベルで表現
        progress_display = QLabel("████████░░ 80%")
        progress_display.setStyleSheet("""
            QLabel {
                background-color: #34495e;
                color: #ecf0f1;
                padding: 5px;
                border-radius: 4px;
                font-family: monospace;
            }
        """)
        
        footer_layout.addWidget(status_label)
        footer_layout.addStretch()
        footer_layout.addWidget(progress_label)
        footer_layout.addWidget(progress_display)
        
        # すべてを結合
        complex_layout.addLayout(header_layout)
        complex_layout.addWidget(content_area, 1)  # コンテンツエリアが拡張
        complex_layout.addLayout(footer_layout)
        
        complex_group.setLayout(complex_layout)
        layout.addWidget(complex_group)
        
    def update_spacing(self, value):
        """
        スペーシングの更新
        
        Args:
            value (int): 新しいスペーシング値
        """
        self.demo_spacing_layout.setSpacing(value)
        self.spacing_value_label.setText(f"{value}px")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QHBoxLayoutの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = HBoxLayoutDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 