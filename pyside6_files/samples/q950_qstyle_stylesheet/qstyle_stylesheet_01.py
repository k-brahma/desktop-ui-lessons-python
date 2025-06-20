"""
QStyle & StyleSheet基本サンプル - CSSライクなスタイリング

このモジュールは、PySide6のStyleSheetとQStyleの基本的な使用方法を示します。
StyleSheetはCSSライクな記法でウィジェットの外観をカスタマイズできる機能です。

主要な学習ポイント:
- 基本的なStyleSheetの記法
- セレクタと擬似クラスの使用
- 色、フォント、ボーダー、背景のカスタマイズ
- アニメーション効果とホバー効果
- テーマの切り替えとスタイル管理

"""

import sys

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QRect, Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class StyleSheetDemoWindow(QWidget):
    """
    StyleSheetとQStyleの使用例を示すウィンドウクラス
    
    様々なスタイリング機能を実演します。
    """
    
    def __init__(self):
        super().__init__()
        self.current_theme = "default"
        self.init_ui()
        self.setup_themes()
        
    def init_ui(self):
        """ユーザーインターフェースの初期化"""
        self.setWindowTitle("QStyle & StyleSheet基本サンプル - CSSライクなスタイリング")
        self.setGeometry(200, 200, 1000, 700)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # タイトルとテーマ切り替え
        self.create_header_section(main_layout)
        
        # コンテンツエリア
        content_layout = QHBoxLayout()
        
        # 左側：基本ウィジェット
        self.create_basic_widgets_section(content_layout)
        
        # 右側：高度なスタイリング
        self.create_advanced_styling_section(content_layout)
        
        main_layout.addLayout(content_layout)
        
        # ログエリア
        self.create_log_section(main_layout)
        
    def create_header_section(self, layout):
        """ヘッダーセクションの作成"""
        header_group = QGroupBox("テーマとスタイル設定")
        header_layout = QHBoxLayout()
        
        # タイトル
        title_label = QLabel("StyleSheet デモンストレーション")
        title_label.setObjectName("title")
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # テーマ選択
        theme_label = QLabel("テーマ:")
        header_layout.addWidget(theme_label)
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Default", "Dark", "Material", "Flat", "Gradient"])
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        header_layout.addWidget(self.theme_combo)
        
        header_group.setLayout(header_layout)
        layout.addWidget(header_group)
        
    def create_basic_widgets_section(self, layout):
        """基本ウィジェットセクションの作成"""
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_widget.setLayout(left_layout)
        
        # ボタンスタイリング
        button_group = QGroupBox("ボタンスタイリング")
        button_layout = QVBoxLayout()
        
        self.primary_btn = QPushButton("プライマリボタン")
        self.primary_btn.setObjectName("primary")
        self.primary_btn.clicked.connect(lambda: self.log_action("プライマリボタンがクリックされました"))
        button_layout.addWidget(self.primary_btn)
        
        self.secondary_btn = QPushButton("セカンダリボタン")
        self.secondary_btn.setObjectName("secondary")
        self.secondary_btn.clicked.connect(lambda: self.log_action("セカンダリボタンがクリックされました"))
        button_layout.addWidget(self.secondary_btn)
        
        self.danger_btn = QPushButton("危険ボタン")
        self.danger_btn.setObjectName("danger")
        self.danger_btn.clicked.connect(lambda: self.log_action("危険ボタンがクリックされました"))
        button_layout.addWidget(self.danger_btn)
        
        button_group.setLayout(button_layout)
        left_layout.addWidget(button_group)
        
        # フォーム要素
        form_group = QGroupBox("フォーム要素")
        form_layout = QVBoxLayout()
        
        # 入力フィールド
        self.styled_input = QLineEdit()
        self.styled_input.setPlaceholderText("スタイル付き入力フィールド")
        self.styled_input.setObjectName("styledInput")
        form_layout.addWidget(self.styled_input)
        
        # スライダー
        self.styled_slider = QSlider(Qt.Orientation.Horizontal)
        self.styled_slider.setRange(0, 100)
        self.styled_slider.setValue(50)
        self.styled_slider.setObjectName("styledSlider")
        form_layout.addWidget(self.styled_slider)
        
        # プログレスバー
        self.styled_progress = QProgressBar()
        self.styled_progress.setValue(75)
        self.styled_progress.setObjectName("styledProgress")
        form_layout.addWidget(self.styled_progress)
        
        form_group.setLayout(form_layout)
        left_layout.addWidget(form_group)
        
        layout.addWidget(left_widget)
        
    def create_advanced_styling_section(self, layout):
        """高度なスタイリングセクションの作成"""
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)
        
        # カスタムカード
        card_group = QGroupBox("カスタムカード")
        card_layout = QVBoxLayout()
        
        self.card_widget = QWidget()
        self.card_widget.setObjectName("card")
        card_content_layout = QVBoxLayout()
        
        card_title = QLabel("カード タイトル")
        card_title.setObjectName("cardTitle")
        card_content_layout.addWidget(card_title)
        
        card_text = QLabel("これはカスタムスタイルが適用されたカードウィジェットです。\n背景、ボーダー、シャドウ効果が設定されています。")
        card_text.setObjectName("cardText")
        card_text.setWordWrap(True)
        card_content_layout.addWidget(card_text)
        
        self.card_widget.setLayout(card_content_layout)
        card_layout.addWidget(self.card_widget)
        card_group.setLayout(card_layout)
        right_layout.addWidget(card_group)
        
        # アニメーション効果
        animation_group = QGroupBox("アニメーション効果")
        animation_layout = QVBoxLayout()
        
        self.animated_btn = QPushButton("アニメーションボタン")
        self.animated_btn.setObjectName("animated")
        self.animated_btn.clicked.connect(self.animate_button)
        animation_layout.addWidget(self.animated_btn)
        
        animation_group.setLayout(animation_layout)
        right_layout.addWidget(animation_group)
        
        # カスタムスタイル
        custom_group = QGroupBox("カスタムスタイル")
        custom_layout = QVBoxLayout()
        
        style_demo_btn = QPushButton("スタイルデモ")
        style_demo_btn.clicked.connect(self.show_style_demo)
        custom_layout.addWidget(style_demo_btn)
        
        custom_group.setLayout(custom_layout)
        right_layout.addWidget(custom_group)
        
        layout.addWidget(right_widget)
        
    def create_log_section(self, layout):
        """ログセクションの作成"""
        self.log_display = QTextEdit()
        self.log_display.setMaximumHeight(120)
        self.log_display.setPlaceholderText("操作ログがここに表示されます...")
        self.log_display.setObjectName("logDisplay")
        layout.addWidget(self.log_display)
        
    def setup_themes(self):
        """テーマの設定"""
        self.themes = {
            "Default": self.get_default_theme(),
            "Dark": self.get_dark_theme(),
            "Material": self.get_material_theme(),
            "Flat": self.get_flat_theme(),
            "Gradient": self.get_gradient_theme()
        }
        
    def get_default_theme(self):
        """デフォルトテーマ"""
        return """
            QWidget {
                background-color: #ffffff;
                color: #333333;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            #title {
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
            }
            
            QPushButton#primary {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton#primary:hover {
                background-color: #2980b9;
            }
            
            QPushButton#secondary {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton#secondary:hover {
                background-color: #7f8c8d;
            }
            
            QPushButton#danger {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton#danger:hover {
                background-color: #c0392b;
            }
        """
        
    def get_dark_theme(self):
        """ダークテーマ"""
        return """
            QWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            QGroupBox {
                border: 2px solid #34495e;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
                color: #ecf0f1;
            }
            
            QPushButton {
                background-color: #34495e;
                color: #ecf0f1;
                border: 1px solid #5d6d7e;
                padding: 10px 20px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5d6d7e;
            }
            
            QLineEdit {
                background-color: #34495e;
                border: 1px solid #5d6d7e;
                border-radius: 4px;
                padding: 8px;
                color: #ecf0f1;
            }
        """
        
    def get_material_theme(self):
        """マテリアルテーマ"""
        return """
            QWidget {
                background-color: #fafafa;
                color: #212121;
                font-family: 'Roboto', Arial, sans-serif;
            }
            
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 4px;
                font-weight: 500;
                text-transform: uppercase;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
            
            QLineEdit {
                border: none;
                border-bottom: 2px solid #2196F3;
                padding: 8px 0px;
                background-color: transparent;
            }
            QLineEdit:focus {
                border-bottom: 2px solid #1976D2;
            }
        """
        
    def get_flat_theme(self):
        """フラットテーマ"""
        return """
            QWidget {
                background-color: #ffffff;
                color: #2c3e50;
            }
            
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px 30px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            
            QLineEdit {
                border: 2px solid #bdc3c7;
                padding: 10px;
                background-color: #ffffff;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """
        
    def get_gradient_theme(self):
        """グラデーションテーマ"""
        return """
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
            }
            
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff6b6b, stop:1 #feca57);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ee5a52, stop:1 #feca57);
            }
        """
        
    def change_theme(self, theme_name):
        """テーマの変更"""
        if theme_name in self.themes:
            self.setStyleSheet(self.themes[theme_name])
            self.current_theme = theme_name.lower()
            self.log_action(f"テーマを '{theme_name}' に変更しました")
            
    def animate_button(self):
        """ボタンのアニメーション"""
        self.animation = QPropertyAnimation(self.animated_btn, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.animated_btn.geometry())
        
        # 少し大きくしてから元に戻す
        current_geo = self.animated_btn.geometry()
        enlarged_geo = QRect(
            current_geo.x() - 10,
            current_geo.y() - 5,
            current_geo.width() + 20,
            current_geo.height() + 10
        )
        
        self.animation.setKeyValueAt(0.5, enlarged_geo)
        self.animation.setEndValue(current_geo)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.animation.start()
        
        self.log_action("ボタンアニメーションを実行しました")
        
    def show_style_demo(self):
        """スタイルデモの表示"""
        demo_style = """
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff9a9e, stop:1 #fecfef);
                border: 2px solid #ff6b9d;
                border-radius: 15px;
                padding: 10px 20px;
                color: #ad1457;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff6b9d, stop:1 #c2185b);
                color: white;
            }
        """
        
        sender = self.sender()
        sender.setStyleSheet(demo_style)
        self.log_action("カスタムスタイルを適用しました")
        
    def log_action(self, message):
        """ログに記録"""
        self.log_display.append(f"[StyleSheet] {message}")


def main():
    """メインエントリーポイント"""
    app = QApplication(sys.argv)
    
    window = StyleSheetDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 