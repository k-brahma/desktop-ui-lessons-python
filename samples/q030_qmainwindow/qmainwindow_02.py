"""
QMainWindow高度サンプル - メニュー、ツールバー、ステータスバー

このモジュールは、QMainWindowクラスの高度な機能を示します。
メニューバー、ツールバー、ステータスバーを含む完全なメインウィンドウを作成します。

主要な学習ポイント:
- メニューバーの作成と設定
- ツールバーの追加
- ステータスバーの活用
- アクションの作成と接続
- ウィンドウの状態管理

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenuBar,
    QStatusBar,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class AdvancedMainWindow(QMainWindow):
    """
    高度なメインウィンドウクラス
    
    メニューバー、ツールバー、ステータスバーを持つ
    完全なメインウィンドウアプリケーションを作成します。
    """
    
    def __init__(self):
        """
        AdvancedMainWindowクラスのコンストラクタ
        
        メインウィンドウの詳細設定とすべてのUI要素の初期化を行います。
        """
        super().__init__()
        self.init_ui()
        self.create_actions()
        self.create_menu_bar()
        self.create_tool_bar()
        self.create_status_bar()
        
    def init_ui(self):
        """
        基本UIの初期化
        
        ウィンドウの基本設定と中央ウィジェットを設定します。
        """
        self.setWindowTitle("QMainWindow高度サンプル - メニュー・ツールバー・ステータスバー")
        self.setGeometry(100, 100, 800, 600)
        
        # 中央ウィジェットとしてテキストエディタを設定
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("ここにテキストを入力してください...")
        self.setCentralWidget(self.text_edit)
        
        # テキスト変更時の処理を接続
        self.text_edit.textChanged.connect(self.on_text_changed)
        
    def create_actions(self):
        """
        アクションの作成
        
        メニューとツールバーで使用するアクションを作成します。
        """
        # 新規作成アクション
        self.new_action = QAction("新規(&N)", self)
        self.new_action.setShortcut(QKeySequence.New)
        self.new_action.setStatusTip("新しいドキュメントを作成")
        self.new_action.triggered.connect(self.new_document)
        
        # 開くアクション
        self.open_action = QAction("開く(&O)", self)
        self.open_action.setShortcut(QKeySequence.Open)
        self.open_action.setStatusTip("既存のファイルを開く")
        self.open_action.triggered.connect(self.open_document)
        
        # 保存アクション
        self.save_action = QAction("保存(&S)", self)
        self.save_action.setShortcut(QKeySequence.Save)
        self.save_action.setStatusTip("現在のドキュメントを保存")
        self.save_action.triggered.connect(self.save_document)
        
        # 終了アクション
        self.exit_action = QAction("終了(&X)", self)
        self.exit_action.setShortcut(QKeySequence.Quit)
        self.exit_action.setStatusTip("アプリケーションを終了")
        self.exit_action.triggered.connect(self.close)
        
        # 切り取りアクション
        self.cut_action = QAction("切り取り(&T)", self)
        self.cut_action.setShortcut(QKeySequence.Cut)
        self.cut_action.setStatusTip("選択テキストを切り取り")
        self.cut_action.triggered.connect(self.text_edit.cut)
        
        # コピーアクション
        self.copy_action = QAction("コピー(&C)", self)
        self.copy_action.setShortcut(QKeySequence.Copy)
        self.copy_action.setStatusTip("選択テキストをコピー")
        self.copy_action.triggered.connect(self.text_edit.copy)
        
        # 貼り付けアクション
        self.paste_action = QAction("貼り付け(&P)", self)
        self.paste_action.setShortcut(QKeySequence.Paste)
        self.paste_action.setStatusTip("クリップボードから貼り付け")
        self.paste_action.triggered.connect(self.text_edit.paste)
        
    def create_menu_bar(self):
        """
        メニューバーの作成
        
        ファイルメニューと編集メニューを作成します。
        """
        menubar = self.menuBar()
        
        # ファイルメニュー
        file_menu = menubar.addMenu("ファイル(&F)")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)
        
        # 編集メニュー
        edit_menu = menubar.addMenu("編集(&E)")
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)
        
    def create_tool_bar(self):
        """
        ツールバーの作成
        
        よく使用するアクションをツールバーに配置します。
        """
        toolbar = self.addToolBar("メイン")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        # ツールバーにアクションを追加
        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()
        toolbar.addAction(self.cut_action)
        toolbar.addAction(self.copy_action)
        toolbar.addAction(self.paste_action)
        
    def create_status_bar(self):
        """
        ステータスバーの作成
        
        アプリケーションの状態情報を表示するステータスバーを設定します。
        """
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("準備完了", 2000)
        
        # 文字数カウンター
        self.char_count_label = self.status_bar.addPermanentWidget(None)
        self.update_char_count()
        
    def new_document(self):
        """
        新規ドキュメントの作成
        
        テキストエディタをクリアして新しいドキュメントを開始します。
        """
        self.text_edit.clear()
        self.status_bar.showMessage("新しいドキュメントを作成しました", 2000)
        
    def open_document(self):
        """
        ドキュメントを開く
        
        実際のファイル操作は実装せず、プレースホルダーとして機能します。
        """
        self.status_bar.showMessage("ファイルを開く機能（未実装）", 2000)
        
    def save_document(self):
        """
        ドキュメントを保存
        
        実際のファイル操作は実装せず、プレースホルダーとして機能します。
        """
        self.status_bar.showMessage("ファイルを保存しました（模擬）", 2000)
        
    def on_text_changed(self):
        """
        テキスト変更時の処理
        
        テキストが変更された際に文字数を更新します。
        """
        self.update_char_count()
        self.status_bar.showMessage("テキストが変更されました", 1000)
        
    def update_char_count(self):
        """
        文字数カウンターの更新
        
        現在のテキストの文字数を計算してステータスバーに表示します。
        """
        text = self.text_edit.toPlainText()
        char_count = len(text)
        line_count = text.count('\n') + 1 if text else 1
        
        count_text = f"文字数: {char_count} | 行数: {line_count}"
        
        # ステータスバーの右端に文字数を表示
        if hasattr(self, 'char_count_label') and self.char_count_label:
            self.status_bar.removeWidget(self.char_count_label)
        
        from PySide6.QtWidgets import QLabel
        self.char_count_label = QLabel(count_text)
        self.status_bar.addPermanentWidget(self.char_count_label)


def main():
    """
    アプリケーションのメインエントリーポイント
    
    高度なQMainWindowの機能を実演します。
    """
    app = QApplication(sys.argv)
    
    # メインウィンドウの作成
    main_window = AdvancedMainWindow()
    main_window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 