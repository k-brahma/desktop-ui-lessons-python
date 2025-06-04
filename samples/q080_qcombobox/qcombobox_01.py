"""
QComboBox基本サンプル - ドロップダウンリストと選択コンポーネント

このモジュールは、PySide6のQComboBoxクラスの基本的な使用方法を示します。
QComboBoxは、複数の選択肢から一つを選択できるドロップダウンリストウィジェットです。

主要な学習ポイント:
- 基本的なコンボボックスの作成と操作
- アイテムの追加・削除・管理
- 編集可能なコンボボックス
- データ付きアイテムの使用
- シグナルとスロットによるイベント処理

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class ComboBoxDemoWindow(QWidget):
    """
    QComboBoxの使用例を示すウィンドウクラス
    
    様々なタイプのコンボボックスと機能を実演します。
    """
    
    def __init__(self):
        """
        ComboBoxDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とコンボボックスサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQComboBoxの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QComboBox基本サンプル - ドロップダウンリストと選択")
        self.setGeometry(200, 200, 700, 750)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_title_section(main_layout)
        self.create_basic_combo_section(main_layout)
        self.create_data_combo_section(main_layout)
        self.create_editable_combo_section(main_layout)
        self.create_dynamic_combo_section(main_layout)
        self.create_interactive_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QComboBox デモンストレーション")
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
        
    def create_basic_combo_section(self, layout):
        """
        基本的なコンボボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 基本コンボボックスグループ
        basic_group = QGroupBox("基本的なコンボボックス")
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
        
        # 国選択コンボボックス
        country_row = QHBoxLayout()
        country_label = QLabel("国を選択:")
        country_label.setMinimumWidth(100)
        
        self.country_combo = QComboBox()
        countries = ["日本", "アメリカ", "イギリス", "フランス", "ドイツ", "中国", "韓国", "オーストラリア"]
        self.country_combo.addItems(countries)
        self.country_combo.setCurrentText("日本")  # デフォルト選択
        self.country_combo.currentTextChanged.connect(self.on_country_changed)
        
        country_row.addWidget(country_label)
        country_row.addWidget(self.country_combo, 1)
        
        # 優先度選択コンボボックス
        priority_row = QHBoxLayout()
        priority_label = QLabel("優先度:")
        priority_label.setMinimumWidth(100)
        
        self.priority_combo = QComboBox()
        priorities = ["低", "中", "高", "緊急"]
        self.priority_combo.addItems(priorities)
        self.priority_combo.setCurrentIndex(1)  # デフォルト: 中
        self.priority_combo.currentIndexChanged.connect(self.on_priority_changed)
        
        priority_row.addWidget(priority_label)
        priority_row.addWidget(self.priority_combo, 1)
        
        # ステータス表示
        self.basic_status = QLabel("国: 日本, 優先度: 中")
        self.basic_status.setStyleSheet("""
            QLabel {
                background-color: #e8f5e8;
                padding: 8px;
                border-radius: 4px;
                border-left: 4px solid #27ae60;
                margin: 5px 0;
            }
        """)
        
        basic_layout.addLayout(country_row)
        basic_layout.addLayout(priority_row)
        basic_layout.addWidget(self.basic_status)
        
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
    def create_data_combo_section(self, layout):
        """
        データ付きコンボボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # データ付きコンボボックスグループ
        data_group = QGroupBox("データ付きコンボボックス")
        data_group.setStyleSheet("""
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
        
        data_layout = QVBoxLayout()
        
        # 言語選択（表示名とコードを分離）
        lang_row = QHBoxLayout()
        lang_label = QLabel("言語:")
        lang_label.setMinimumWidth(100)
        
        self.language_combo = QComboBox()
        languages = [
            ("日本語", "ja"),
            ("English", "en"),
            ("Français", "fr"),
            ("Deutsch", "de"),
            ("中文", "zh"),
            ("Español", "es")
        ]
        
        for display_name, code in languages:
            self.language_combo.addItem(display_name, code)
            
        self.language_combo.currentIndexChanged.connect(self.on_language_changed)
        
        lang_row.addWidget(lang_label)
        lang_row.addWidget(self.language_combo, 1)
        
        # 通貨選択
        currency_row = QHBoxLayout()
        currency_label = QLabel("通貨:")
        currency_label.setMinimumWidth(100)
        
        self.currency_combo = QComboBox()
        currencies = [
            ("日本円 (¥)", {"code": "JPY", "symbol": "¥", "rate": 1.0}),
            ("米ドル ($)", {"code": "USD", "symbol": "$", "rate": 0.0067}),
            ("ユーロ (€)", {"code": "EUR", "symbol": "€", "rate": 0.0062}),
            ("英ポンド (£)", {"code": "GBP", "symbol": "£", "rate": 0.0053}),
        ]
        
        for display_name, data in currencies:
            self.currency_combo.addItem(display_name, data)
            
        self.currency_combo.currentIndexChanged.connect(self.on_currency_changed)
        
        currency_row.addWidget(currency_label)
        currency_row.addWidget(self.currency_combo, 1)
        
        # データ表示エリア
        self.data_display = QLabel("言語コード: ja, 通貨コード: JPY")
        self.data_display.setStyleSheet("""
            QLabel {
                background-color: #fff3cd;
                padding: 8px;
                border-radius: 4px;
                border-left: 4px solid #f39c12;
                margin: 5px 0;
            }
        """)
        
        data_layout.addLayout(lang_row)
        data_layout.addLayout(currency_row)
        data_layout.addWidget(self.data_display)
        
        data_group.setLayout(data_layout)
        layout.addWidget(data_group)
        
    def create_editable_combo_section(self, layout):
        """
        編集可能なコンボボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 編集可能コンボボックスグループ
        editable_group = QGroupBox("編集可能なコンボボックス")
        editable_group.setStyleSheet("""
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
        
        editable_layout = QVBoxLayout()
        
        # 検索履歴コンボボックス
        search_row = QHBoxLayout()
        search_label = QLabel("検索履歴:")
        search_label.setMinimumWidth(100)
        
        self.search_combo = QComboBox()
        self.search_combo.setEditable(True)
        self.search_combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAtTop)
        
        # 初期の検索履歴
        self.search_history = ["PySide6", "Qt Framework", "Python GUI", "PyQt", "Tkinter"]
        self.search_combo.addItems(self.search_history)
        
        search_button = QPushButton("検索")
        search_button.clicked.connect(self.perform_search)
        search_button.setStyleSheet("""
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
        
        search_row.addWidget(search_label)
        search_row.addWidget(self.search_combo, 1)
        search_row.addWidget(search_button)
        
        # カスタム入力コンボボックス
        custom_row = QHBoxLayout()
        custom_label = QLabel("カスタム値:")
        custom_label.setMinimumWidth(100)
        
        self.custom_combo = QComboBox()
        self.custom_combo.setEditable(True)
        custom_options = ["オプション1", "オプション2", "オプション3"]
        self.custom_combo.addItems(custom_options)
        self.custom_combo.editTextChanged.connect(self.on_custom_text_changed)
        
        custom_row.addWidget(custom_label)
        custom_row.addWidget(self.custom_combo, 1)
        
        # 入力状態表示
        self.edit_status = QLabel("入力待ち...")
        self.edit_status.setStyleSheet("""
            QLabel {
                background-color: #f8d7da;
                padding: 8px;
                border-radius: 4px;
                border-left: 4px solid #e74c3c;
                margin: 5px 0;
            }
        """)
        
        editable_layout.addLayout(search_row)
        editable_layout.addLayout(custom_row)
        editable_layout.addWidget(self.edit_status)
        
        editable_group.setLayout(editable_layout)
        layout.addWidget(editable_group)
        
    def create_dynamic_combo_section(self, layout):
        """
        動的コンボボックスセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 動的コンボボックスグループ
        dynamic_group = QGroupBox("動的コンボボックス（連動選択）")
        dynamic_group.setStyleSheet("""
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
        
        dynamic_layout = QVBoxLayout()
        
        # カテゴリ選択
        category_row = QHBoxLayout()
        category_label = QLabel("カテゴリ:")
        category_label.setMinimumWidth(100)
        
        self.category_combo = QComboBox()
        
        # カテゴリデータ
        self.category_data = {
            "果物": ["りんご", "バナナ", "オレンジ", "いちご", "ぶどう"],
            "野菜": ["にんじん", "じゃがいも", "玉ねぎ", "ピーマン", "トマト"],
            "肉類": ["牛肉", "豚肉", "鶏肉", "羊肉", "魚"],
            "飲み物": ["水", "お茶", "コーヒー", "ジュース", "牛乳"]
        }
        
        self.category_combo.addItems(list(self.category_data.keys()))
        self.category_combo.currentTextChanged.connect(self.update_items)
        
        category_row.addWidget(category_label)
        category_row.addWidget(self.category_combo, 1)
        
        # アイテム選択
        item_row = QHBoxLayout()
        item_label = QLabel("アイテム:")
        item_label.setMinimumWidth(100)
        
        self.item_combo = QComboBox()
        
        item_row.addWidget(item_label)
        item_row.addWidget(self.item_combo, 1)
        
        # 初期値の設定
        self.update_items(self.category_combo.currentText())
        
        dynamic_layout.addLayout(category_row)
        dynamic_layout.addLayout(item_row)
        
        dynamic_group.setLayout(dynamic_layout)
        layout.addWidget(dynamic_group)
        
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
        button_row = QHBoxLayout()
        
        get_values_btn = QPushButton("選択値を取得")
        get_values_btn.clicked.connect(self.get_all_values)
        get_values_btn.setStyleSheet("""
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
        
        clear_history_btn = QPushButton("履歴をクリア")
        clear_history_btn.clicked.connect(self.clear_search_history)
        clear_history_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
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
        
        button_row.addWidget(get_values_btn)
        button_row.addWidget(clear_history_btn)
        button_row.addWidget(reset_btn)
        
        # 結果表示エリア
        self.result_display = QTextEdit()
        self.result_display.setMaximumHeight(120)
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
        
        interactive_layout.addLayout(button_row)
        interactive_layout.addWidget(self.result_display)
        
        interactive_group.setLayout(interactive_layout)
        layout.addWidget(interactive_group)
        
    def on_country_changed(self, text):
        """
        国選択の変更処理
        
        Args:
            text (str): 選択された国名
        """
        self.update_basic_status()
        
    def on_priority_changed(self, index):
        """
        優先度選択の変更処理
        
        Args:
            index (int): 選択されたインデックス
        """
        self.update_basic_status()
        
    def update_basic_status(self):
        """
        基本ステータスの更新
        """
        country = self.country_combo.currentText()
        priority = self.priority_combo.currentText()
        self.basic_status.setText(f"国: {country}, 優先度: {priority}")
        
    def on_language_changed(self, index):
        """
        言語選択の変更処理
        
        Args:
            index (int): 選択されたインデックス
        """
        self.update_data_display()
        
    def on_currency_changed(self, index):
        """
        通貨選択の変更処理
        
        Args:
            index (int): 選択されたインデックス
        """
        self.update_data_display()
        
    def update_data_display(self):
        """
        データ表示の更新
        """
        lang_code = self.language_combo.currentData()
        currency_data = self.currency_combo.currentData()
        
        if currency_data:
            currency_code = currency_data.get("code", "N/A")
            self.data_display.setText(f"言語コード: {lang_code}, 通貨コード: {currency_code}")
        else:
            self.data_display.setText(f"言語コード: {lang_code}")
            
    def perform_search(self):
        """
        検索実行
        """
        query = self.search_combo.currentText()
        if query and query not in self.search_history:
            self.search_combo.insertItem(0, query)
            self.search_history.insert(0, query)
            
        self.edit_status.setText(f"検索実行: '{query}'")
        
    def on_custom_text_changed(self, text):
        """
        カスタムテキスト変更処理
        
        Args:
            text (str): 入力されたテキスト
        """
        if text:
            self.edit_status.setText(f"入力中: '{text}'")
        else:
            self.edit_status.setText("入力待ち...")
            
    def update_items(self, category):
        """
        アイテムコンボボックスの更新
        
        Args:
            category (str): 選択されたカテゴリ
        """
        self.item_combo.clear()
        if category in self.category_data:
            self.item_combo.addItems(self.category_data[category])
            
    def get_all_values(self):
        """
        すべての選択値を取得して表示
        """
        result_text = "=== 選択値一覧 ===\n\n"
        
        result_text += f"国: {self.country_combo.currentText()}\n"
        result_text += f"優先度: {self.priority_combo.currentText()}\n"
        result_text += f"言語: {self.language_combo.currentText()} ({self.language_combo.currentData()})\n"
        
        currency_data = self.currency_combo.currentData()
        if currency_data:
            result_text += f"通貨: {self.currency_combo.currentText()} ({currency_data['code']})\n"
        else:
            result_text += f"通貨: {self.currency_combo.currentText()}\n"
            
        result_text += f"検索: {self.search_combo.currentText()}\n"
        result_text += f"カスタム: {self.custom_combo.currentText()}\n"
        result_text += f"カテゴリ: {self.category_combo.currentText()}\n"
        result_text += f"アイテム: {self.item_combo.currentText()}\n"
        
        self.result_display.setText(result_text)
        
    def clear_search_history(self):
        """
        検索履歴のクリア
        """
        self.search_combo.clear()
        self.search_history.clear()
        self.edit_status.setText("検索履歴をクリアしました")
        
    def reset_to_defaults(self):
        """
        すべての設定をデフォルトに戻す
        """
        self.country_combo.setCurrentText("日本")
        self.priority_combo.setCurrentIndex(1)
        self.language_combo.setCurrentIndex(0)
        self.currency_combo.setCurrentIndex(0)
        self.category_combo.setCurrentIndex(0)
        
        # 検索履歴を復元
        self.search_combo.clear()
        self.search_history = ["PySide6", "Qt Framework", "Python GUI", "PyQt", "Tkinter"]
        self.search_combo.addItems(self.search_history)
        
        self.custom_combo.setCurrentIndex(0)
        self.result_display.clear()
        self.edit_status.setText("デフォルト値に戻しました")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QComboBoxの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = ComboBoxDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 