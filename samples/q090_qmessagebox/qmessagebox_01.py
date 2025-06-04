"""
QMessageBox基本サンプル - メッセージダイアログとユーザー通知

このモジュールは、PySide6のQMessageBoxクラスの基本的な使用方法を示します。
QMessageBoxは、ユーザーに情報を表示したり、確認を求めたりするためのダイアログです。

主要な学習ポイント:
- 基本的なメッセージボックスの表示
- 情報、警告、エラー、質問ダイアログの使い分け
- カスタムボタンの追加
- 戻り値による処理の分岐
- アイコンとテキストのカスタマイズ

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class MessageBoxDemoWindow(QWidget):
    """
    QMessageBoxの使用例を示すウィンドウクラス
    
    様々なタイプのメッセージダイアログと機能を実演します。
    """
    
    def __init__(self):
        """
        MessageBoxDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とメッセージボックスサンプルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なQMessageBoxの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("QMessageBox基本サンプル - メッセージダイアログ")
        self.setGeometry(200, 200, 800, 700)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 各セクションの作成
        self.create_title_section(main_layout)
        self.create_basic_messages_section(main_layout)
        self.create_question_dialogs_section(main_layout)
        self.create_custom_dialogs_section(main_layout)
        self.create_input_demo_section(main_layout)
        self.create_result_display_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("QMessageBox デモンストレーション")
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
        
    def create_basic_messages_section(self, layout):
        """
        基本メッセージセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 基本メッセージグループ
        basic_group = QGroupBox("基本的なメッセージダイアログ")
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
        
        basic_layout = QHBoxLayout()
        
        # 情報メッセージ
        info_btn = QPushButton("情報メッセージ")
        info_btn.clicked.connect(self.show_info_message)
        info_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        basic_layout.addWidget(info_btn)
        
        # 警告メッセージ
        warning_btn = QPushButton("警告メッセージ")
        warning_btn.clicked.connect(self.show_warning_message)
        warning_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #d68910;
            }
        """)
        basic_layout.addWidget(warning_btn)
        
        # エラーメッセージ
        error_btn = QPushButton("エラーメッセージ")
        error_btn.clicked.connect(self.show_error_message)
        error_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        basic_layout.addWidget(error_btn)
        
        # 成功メッセージ
        success_btn = QPushButton("成功メッセージ")
        success_btn.clicked.connect(self.show_success_message)
        success_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        basic_layout.addWidget(success_btn)
        
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
    def create_question_dialogs_section(self, layout):
        """
        質問ダイアログセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 質問ダイアロググループ
        question_group = QGroupBox("質問・確認ダイアログ")
        question_group.setStyleSheet("""
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
        
        question_layout = QHBoxLayout()
        
        # Yes/No質問
        yes_no_btn = QPushButton("Yes/No 質問")
        yes_no_btn.clicked.connect(self.show_yes_no_dialog)
        yes_no_btn.setStyleSheet("""
            QPushButton {
                background-color: #9b59b6;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
        """)
        question_layout.addWidget(yes_no_btn)
        
        # Yes/No/Cancel質問
        yes_no_cancel_btn = QPushButton("Yes/No/Cancel")
        yes_no_cancel_btn.clicked.connect(self.show_yes_no_cancel_dialog)
        yes_no_cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #16a085;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #138d75;
            }
        """)
        question_layout.addWidget(yes_no_cancel_btn)
        
        # 削除確認
        delete_confirm_btn = QPushButton("削除確認")
        delete_confirm_btn.clicked.connect(self.show_delete_confirmation)
        delete_confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        question_layout.addWidget(delete_confirm_btn)
        
        question_group.setLayout(question_layout)
        layout.addWidget(question_group)
        
    def create_custom_dialogs_section(self, layout):
        """
        カスタムダイアログセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # カスタムダイアロググループ
        custom_group = QGroupBox("カスタムダイアログ")
        custom_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #e67e22;
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
        
        custom_layout = QHBoxLayout()
        
        # カスタムボタン
        custom_buttons_btn = QPushButton("カスタムボタン")
        custom_buttons_btn.clicked.connect(self.show_custom_buttons_dialog)
        custom_buttons_btn.setStyleSheet("""
            QPushButton {
                background-color: #e67e22;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
        """)
        custom_layout.addWidget(custom_buttons_btn)
        
        # 詳細メッセージ
        detailed_btn = QPushButton("詳細メッセージ")
        detailed_btn.clicked.connect(self.show_detailed_message)
        detailed_btn.setStyleSheet("""
            QPushButton {
                background-color: #34495e;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2c3e50;
            }
        """)
        custom_layout.addWidget(detailed_btn)
        
        # 複数選択
        multiple_choice_btn = QPushButton("複数選択")
        multiple_choice_btn.clicked.connect(self.show_multiple_choice_dialog)
        multiple_choice_btn.setStyleSheet("""
            QPushButton {
                background-color: #7f8c8d;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #95a5a6;
            }
        """)
        custom_layout.addWidget(multiple_choice_btn)
        
        custom_group.setLayout(custom_layout)
        layout.addWidget(custom_group)
        
    def create_input_demo_section(self, layout):
        """
        入力デモセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 入力デモグループ
        input_group = QGroupBox("実用的な使用例")
        input_group.setStyleSheet("""
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
        
        input_layout = QVBoxLayout()
        
        # ファイル保存シミュレーション
        file_layout = QHBoxLayout()
        file_layout.addWidget(QLabel("ファイル名:"))
        self.filename_edit = QLineEdit("document.txt")
        self.filename_edit.setPlaceholderText("ファイル名を入力...")
        file_layout.addWidget(self.filename_edit)
        
        save_btn = QPushButton("保存")
        save_btn.clicked.connect(self.save_file_simulation)
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        file_layout.addWidget(save_btn)
        
        input_layout.addLayout(file_layout)
        
        # アプリケーション終了シミュレーション
        app_control_layout = QHBoxLayout()
        
        exit_btn = QPushButton("アプリケーション終了")
        exit_btn.clicked.connect(self.exit_application_simulation)
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #c0392b;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #a93226;
            }
        """)
        app_control_layout.addWidget(exit_btn)
        
        reset_btn = QPushButton("設定リセット")
        reset_btn.clicked.connect(self.reset_settings_simulation)
        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d68910;
            }
        """)
        app_control_layout.addWidget(reset_btn)
        
        input_layout.addLayout(app_control_layout)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
    def create_result_display_section(self, layout):
        """
        結果表示セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 結果表示グループ
        result_group = QGroupBox("ダイアログの結果")
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
        self.result_display.setMaximumHeight(150)
        self.result_display.setPlaceholderText("ダイアログの実行結果がここに表示されます...")
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
        clear_btn = QPushButton("結果をクリア")
        clear_btn.clicked.connect(self.clear_results)
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
        
    def log_result(self, message):
        """
        結果をログに追加
        
        Args:
            message (str): ログメッセージ
        """
        self.result_display.append(f"[{self.__class__.__name__}] {message}")
        
    def show_info_message(self):
        """
        情報メッセージの表示
        """
        QMessageBox.information(
            self,
            "情報",
            "これは情報メッセージです。\n操作が正常に完了しました。"
        )
        self.log_result("情報メッセージを表示しました")
        
    def show_warning_message(self):
        """
        警告メッセージの表示
        """
        QMessageBox.warning(
            self,
            "警告",
            "これは警告メッセージです。\n注意が必要な状況です。"
        )
        self.log_result("警告メッセージを表示しました")
        
    def show_error_message(self):
        """
        エラーメッセージの表示
        """
        QMessageBox.critical(
            self,
            "エラー",
            "これはエラーメッセージです。\n問題が発生しました。"
        )
        self.log_result("エラーメッセージを表示しました")
        
    def show_success_message(self):
        """
        成功メッセージの表示
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("成功")
        msg_box.setText("操作が成功しました！")
        msg_box.setInformativeText("すべての処理が正常に完了しました。")
        msg_box.exec()
        self.log_result("成功メッセージを表示しました")
        
    def show_yes_no_dialog(self):
        """
        Yes/No質問ダイアログの表示
        """
        reply = QMessageBox.question(
            self,
            "確認",
            "この操作を実行しますか？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.log_result("Yes/No質問: Yes が選択されました")
        else:
            self.log_result("Yes/No質問: No が選択されました")
            
    def show_yes_no_cancel_dialog(self):
        """
        Yes/No/Cancel質問ダイアログの表示
        """
        reply = QMessageBox.question(
            self,
            "ファイル保存確認",
            "変更を保存しますか？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Yes
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.log_result("ファイル保存確認: Yes (保存) が選択されました")
        elif reply == QMessageBox.StandardButton.No:
            self.log_result("ファイル保存確認: No (保存しない) が選択されました")
        else:
            self.log_result("ファイル保存確認: Cancel (キャンセル) が選択されました")
            
    def show_delete_confirmation(self):
        """
        削除確認ダイアログの表示
        """
        reply = QMessageBox.warning(
            self,
            "削除確認",
            "選択したファイルを削除しますか？\n\nこの操作は元に戻せません。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.log_result("削除確認: ファイルの削除が承認されました")
        else:
            self.log_result("削除確認: ファイルの削除がキャンセルされました")
            
    def show_custom_buttons_dialog(self):
        """
        カスタムボタンダイアログの表示
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("カスタムボタン")
        msg_box.setText("操作を選択してください")
        msg_box.setInformativeText("以下のオプションから選択できます:")
        
        # カスタムボタンの追加
        save_button = msg_box.addButton("保存", QMessageBox.ButtonRole.AcceptRole)
        save_as_button = msg_box.addButton("名前を付けて保存", QMessageBox.ButtonRole.AcceptRole)
        cancel_button = msg_box.addButton("キャンセル", QMessageBox.ButtonRole.RejectRole)
        
        msg_box.exec()
        
        clicked_button = msg_box.clickedButton()
        if clicked_button == save_button:
            self.log_result("カスタムボタン: 保存 が選択されました")
        elif clicked_button == save_as_button:
            self.log_result("カスタムボタン: 名前を付けて保存 が選択されました")
        elif clicked_button == cancel_button:
            self.log_result("カスタムボタン: キャンセル が選択されました")
            
    def show_detailed_message(self):
        """
        詳細メッセージダイアログの表示
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("処理完了")
        msg_box.setText("データベースの同期が完了しました")
        msg_box.setInformativeText("100件のレコードが正常に処理されました。")
        msg_box.setDetailedText("""
詳細ログ:
- 接続開始: 2024-01-01 10:00:00
- データ取得: 100件
- 処理時間: 2.5秒
- エラー: 0件
- 警告: 0件
- 接続終了: 2024-01-01 10:00:03
        """)
        msg_box.exec()
        self.log_result("詳細メッセージダイアログを表示しました")
        
    def show_multiple_choice_dialog(self):
        """
        複数選択ダイアログの表示
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("ファイル形式選択")
        msg_box.setText("エクスポート形式を選択してください")
        
        pdf_button = msg_box.addButton("PDF", QMessageBox.ButtonRole.AcceptRole)
        excel_button = msg_box.addButton("Excel", QMessageBox.ButtonRole.AcceptRole)
        csv_button = msg_box.addButton("CSV", QMessageBox.ButtonRole.AcceptRole)
        cancel_button = msg_box.addButton("キャンセル", QMessageBox.ButtonRole.RejectRole)
        
        msg_box.exec()
        
        clicked_button = msg_box.clickedButton()
        if clicked_button == pdf_button:
            self.log_result("ファイル形式: PDF が選択されました")
        elif clicked_button == excel_button:
            self.log_result("ファイル形式: Excel が選択されました")
        elif clicked_button == csv_button:
            self.log_result("ファイル形式: CSV が選択されました")
        elif clicked_button == cancel_button:
            self.log_result("ファイル形式選択: キャンセルされました")
            
    def save_file_simulation(self):
        """
        ファイル保存シミュレーション
        """
        filename = self.filename_edit.text().strip()
        
        if not filename:
            QMessageBox.warning(self, "入力エラー", "ファイル名を入力してください。")
            return
            
        # ファイル上書き確認
        reply = QMessageBox.question(
            self,
            "ファイル保存",
            f"ファイル '{filename}' を保存しますか？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # 成功メッセージ
            QMessageBox.information(
                self,
                "保存完了",
                f"ファイル '{filename}' が正常に保存されました。"
            )
            self.log_result(f"ファイル保存シミュレーション: '{filename}' を保存しました")
        else:
            self.log_result("ファイル保存シミュレーション: 保存がキャンセルされました")
            
    def exit_application_simulation(self):
        """
        アプリケーション終了シミュレーション
        """
        reply = QMessageBox.question(
            self,
            "アプリケーション終了",
            "アプリケーションを終了しますか？\n\n未保存の変更は失われます。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.log_result("アプリケーション終了: 終了が承認されました（実際には終了しません）")
        else:
            self.log_result("アプリケーション終了: 終了がキャンセルされました")
            
    def reset_settings_simulation(self):
        """
        設定リセットシミュレーション
        """
        reply = QMessageBox.warning(
            self,
            "設定リセット",
            "すべての設定をデフォルト値にリセットしますか？\n\nこの操作は元に戻せません。",
            QMessageBox.StandardButton.Reset | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )
        
        if reply == QMessageBox.StandardButton.Reset:
            QMessageBox.information(
                self,
                "リセット完了",
                "設定が正常にリセットされました。"
            )
            self.log_result("設定リセット: 設定がリセットされました")
        else:
            self.log_result("設定リセット: リセットがキャンセルされました")
            
    def clear_results(self):
        """
        結果表示のクリア
        """
        self.result_display.clear()


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QMessageBoxの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = MessageBoxDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 