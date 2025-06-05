"""
QFont基本サンプル - フォント設定とタイポグラフィ

このモジュールは、PySide6のQFontクラスの基本的な使用方法を示します。
QFontは、テキストの表示に使用するフォントのプロパティを設定するクラスです。

主要な学習ポイント:
- 基本的なフォント設定
- フォントファミリーとサイズの指定
- 太字、斜体、下線などのスタイル設定
- システムフォントの取得と使用
- アプリケーション全体でのフォント統一

"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class FontDemoWindow(QWidget):
    """
    QFontの使用例を示すウィンドウクラス
    
    様々なフォント設定を適用したラベルとコントロールを表示します。
    """
    
    def __init__(self):
        """
        FontDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とフォントサンプルの作成を行います。
        """
        super().__init__()
        self.current_font_size = 12
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なフォント設定のサンプルを表示します。
        """
        self.setWindowTitle("QFont基本サンプル - フォント設定デモ")
        self.setGeometry(200, 200, 700, 600)
        
        # メインレイアウト
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # タイトルセクション
        self.create_title_section(layout)
        
        # フォントファミリーサンプル
        self.create_font_family_samples(layout)
        
        # フォントスタイルサンプル
        self.create_font_style_samples(layout)
        
        # インタラクティブコントロール
        self.create_interactive_controls(layout)
        
        # システムフォント情報
        self.create_system_font_info(layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QFont デモンストレーション")
        title_font = QFont()
        title_font.setFamily("Arial")
        title_font.setPointSize(24)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                background-color: #ecf0f1;
                padding: 20px;
                border-radius: 10px;
                border: 2px solid #bdc3c7;
                margin-bottom: 15px;
            }
        """)
        layout.addWidget(title_label)
        
    def create_font_family_samples(self, layout):
        """
        フォントファミリーサンプルの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        family_title = QLabel("フォントファミリーの例")
        family_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        family_title.setStyleSheet("color: #34495e; margin-top: 10px; margin-bottom: 5px;")
        layout.addWidget(family_title)
        
        # 各種フォントファミリーのサンプル
        font_families = [
            ("Arial", "Arial - サンセリフフォントの代表例"),
            ("Times New Roman", "Times New Roman - セリフフォントの代表例"),
            ("Courier New", "Courier New - 等幅フォント（プログラミング向け）"),
            ("Verdana", "Verdana - ウェブ用に最適化されたフォント"),
            ("Comic Sans MS", "Comic Sans MS - カジュアルなフォント")
        ]
        
        for family, description in font_families:
            label = QLabel(description)
            font = QFont()
            font.setFamily(family)
            font.setPointSize(12)
            label.setFont(font)
            label.setStyleSheet("""
                QLabel {
                    background-color: white;
                    padding: 8px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    margin: 2px;
                }
            """)
            layout.addWidget(label)
            
    def create_font_style_samples(self, layout):
        """
        フォントスタイルサンプルの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        style_title = QLabel("フォントスタイルの例")
        style_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        style_title.setStyleSheet("color: #34495e; margin-top: 15px; margin-bottom: 5px;")
        layout.addWidget(style_title)
        
        # 通常テキスト
        normal_label = QLabel("通常のテキスト - Normal text")
        normal_font = QFont("Arial", 12)
        normal_label.setFont(normal_font)
        normal_label.setStyleSheet("background-color: white; padding: 5px; border: 1px solid #ddd; margin: 1px;")
        layout.addWidget(normal_label)
        
        # 太字
        bold_label = QLabel("太字のテキスト - Bold text")
        bold_font = QFont("Arial", 12)
        bold_font.setBold(True)
        bold_label.setFont(bold_font)
        bold_label.setStyleSheet("background-color: white; padding: 5px; border: 1px solid #ddd; margin: 1px;")
        layout.addWidget(bold_label)
        
        # 斜体
        italic_label = QLabel("斜体のテキスト - Italic text")
        italic_font = QFont("Arial", 12)
        italic_font.setItalic(True)
        italic_label.setFont(italic_font)
        italic_label.setStyleSheet("background-color: white; padding: 5px; border: 1px solid #ddd; margin: 1px;")
        layout.addWidget(italic_label)
        
        # 下線
        underline_label = QLabel("下線付きテキスト - Underlined text")
        underline_font = QFont("Arial", 12)
        underline_font.setUnderline(True)
        underline_label.setFont(underline_font)
        underline_label.setStyleSheet("background-color: white; padding: 5px; border: 1px solid #ddd; margin: 1px;")
        layout.addWidget(underline_label)
        
        # 取り消し線
        strikeout_label = QLabel("取り消し線付きテキスト - Strikeout text")
        strikeout_font = QFont("Arial", 12)
        strikeout_font.setStrikeOut(True)
        strikeout_label.setFont(strikeout_font)
        strikeout_label.setStyleSheet("background-color: white; padding: 5px; border: 1px solid #ddd; margin: 1px;")
        layout.addWidget(strikeout_label)
        
        # 組み合わせ
        combined_label = QLabel("太字 + 斜体 + 下線の組み合わせ")
        combined_font = QFont("Arial", 12)
        combined_font.setBold(True)
        combined_font.setItalic(True)
        combined_font.setUnderline(True)
        combined_label.setFont(combined_font)
        combined_label.setStyleSheet("background-color: #fffacd; padding: 5px; border: 1px solid #ddd; margin: 1px;")
        layout.addWidget(combined_label)
        
    def create_interactive_controls(self, layout):
        """
        インタラクティブコントロールの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        control_title = QLabel("インタラクティブフォント制御")
        control_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        control_title.setStyleSheet("color: #34495e; margin-top: 15px; margin-bottom: 5px;")
        layout.addWidget(control_title)
        
        # 動的に変更可能なサンプルテキスト
        self.dynamic_label = QLabel("このテキストのフォントサイズを変更できます")
        self.update_dynamic_font()
        self.dynamic_label.setStyleSheet("""
            QLabel {
                background-color: #e8f5e8;
                padding: 15px;
                border: 2px solid #27ae60;
                border-radius: 5px;
                margin: 5px;
            }
        """)
        layout.addWidget(self.dynamic_label)
        
        # コントロールボタン
        button_layout = QHBoxLayout()
        
        # フォントサイズ縮小ボタン
        decrease_button = QPushButton("フォントサイズ -")
        decrease_button.clicked.connect(self.decrease_font_size)
        decrease_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        button_layout.addWidget(decrease_button)
        
        # フォントサイズ拡大ボタン
        increase_button = QPushButton("フォントサイズ +")
        increase_button.clicked.connect(self.increase_font_size)
        increase_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        button_layout.addWidget(increase_button)
        
        # リセットボタン
        reset_button = QPushButton("リセット")
        reset_button.clicked.connect(self.reset_font_size)
        reset_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        button_layout.addWidget(reset_button)
        
        layout.addLayout(button_layout)
        
    def create_system_font_info(self, layout):
        """
        システムフォント情報の表示
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        info_title = QLabel("システムフォント情報")
        info_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        info_title.setStyleSheet("color: #34495e; margin-top: 15px; margin-bottom: 5px;")
        layout.addWidget(info_title)
        
        # システムフォントデータベースから情報を取得
        font_db = QFontDatabase()
        
        # デフォルトフォント
        default_font = QApplication.font()
        default_info = QLabel(f"デフォルトフォント: {default_font.family()}, サイズ: {default_font.pointSize()}")
        default_info.setStyleSheet("background-color: #f8f9fa; padding: 5px; border: 1px solid #dee2e6; margin: 1px;")
        layout.addWidget(default_info)
        
        # 利用可能なフォントファミリー数
        families = font_db.families()
        family_count_info = QLabel(f"利用可能なフォントファミリー数: {len(families)}")
        family_count_info.setStyleSheet("background-color: #f8f9fa; padding: 5px; border: 1px solid #dee2e6; margin: 1px;")
        layout.addWidget(family_count_info)
        
        # いくつかの代表的なフォントファミリー
        sample_families = families[:5] if families else []
        if sample_families:
            sample_info = QLabel(f"代表的なフォント: {', '.join(sample_families)}")
            sample_info.setStyleSheet("background-color: #f8f9fa; padding: 5px; border: 1px solid #dee2e6; margin: 1px;")
            layout.addWidget(sample_info)
            
    def update_dynamic_font(self):
        """
        動的フォントラベルの更新
        """
        font = QFont("Arial", self.current_font_size)
        self.dynamic_label.setFont(font)
        self.dynamic_label.setText(f"フォントサイズ: {self.current_font_size}pt - このテキストのサイズが変わります")
        
    def increase_font_size(self):
        """
        フォントサイズの拡大
        """
        if self.current_font_size < 36:
            self.current_font_size += 2
            self.update_dynamic_font()
            
    def decrease_font_size(self):
        """
        フォントサイズの縮小
        """
        if self.current_font_size > 8:
            self.current_font_size -= 2
            self.update_dynamic_font()
            
    def reset_font_size(self):
        """
        フォントサイズのリセット
        """
        self.current_font_size = 12
        self.update_dynamic_font()


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QFontの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = FontDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 