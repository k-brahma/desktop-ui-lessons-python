"""
QApplication高度サンプル - アプリケーション属性とイベント処理

このモジュールは、QApplicationクラスの高度な機能を示します。
アプリケーション全体の設定、イベント処理、終了処理などを学習できます。

主要な学習ポイント:
- アプリケーション情報の設定
- 終了時のクリーンアップ処理
- シグナルとスロットの基本的な使用
- アプリケーション全体での状態管理
"""

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class AdvancedWindow(QWidget):
    """
    高度な機能を持つウィンドウクラス
    
    タイマー、ボタンクリック、アプリケーション終了処理などの
    機能を含むウィンドウを作成します。
    """
    
    def __init__(self):
        """
        AdvancedWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とUIコンポーネントの配置を行います。
        """
        super().__init__()
        self.init_ui()
        self.init_timer()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        レイアウト、ラベル、ボタンを設定します。
        """
        self.setWindowTitle("QApplication高度サンプル")
        self.setGeometry(300, 300, 400, 200)
        
        # レイアウトの作成
        layout = QVBoxLayout()
        
        # ステータスラベル
        self.status_label = QLabel("アプリケーション起動中...")
        layout.addWidget(self.status_label)
        
        # カウンターラベル
        self.counter_label = QLabel("経過時間: 0秒")
        layout.addWidget(self.counter_label)
        
        # 終了ボタン
        quit_button = QPushButton("アプリケーション終了")
        quit_button.clicked.connect(self.graceful_quit)
        layout.addWidget(quit_button)
        
        self.setLayout(layout)
        
        # カウンター初期化
        self.counter = 0
        
    def init_timer(self):
        """
        タイマーの初期化
        
        1秒間隔で実行されるタイマーを設定します。
        """
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_counter)
        self.timer.start(1000)  # 1000ms = 1秒
        
        # ステータス更新
        self.status_label.setText("アプリケーション実行中...")
        
    def update_counter(self):
        """
        カウンターの更新
        
        タイマーから呼び出され、経過時間を更新します。
        """
        self.counter += 1
        self.counter_label.setText(f"経過時間: {self.counter}秒")
        
    def graceful_quit(self):
        """
        優雅なアプリケーション終了
        
        クリーンアップ処理を行ってからアプリケーションを終了します。
        """
        self.status_label.setText("アプリケーション終了処理中...")
        self.timer.stop()
        
        # QApplicationのquit()メソッドを呼び出してイベントループを終了
        QApplication.instance().quit()
        
    def closeEvent(self, event):
        """
        ウィンドウクローズイベントのオーバーライド
        
        ウィンドウが閉じられる際の処理を定義します。
        
        Args:
            event: クローズイベント
        """
        self.timer.stop()
        print("ウィンドウが閉じられました - クリーンアップ完了")
        event.accept()


def setup_application():
    """
    アプリケーションの詳細設定
    
    Returns:
        QApplication: 設定済みのアプリケーションインスタンス
    """
    app = QApplication(sys.argv)
    
    # アプリケーション情報の設定
    app.setApplicationName("PySide6 学習アプリ")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("PySide6 Learning Team")
    app.setOrganizationDomain("example.com")
    
    # アプリケーション終了時のクリーンアップ処理を設定
    app.aboutToQuit.connect(cleanup_on_exit)
    
    return app


def cleanup_on_exit():
    """
    アプリケーション終了時のクリーンアップ処理
    
    アプリケーションが終了する直前に実行される処理です。
    """
    print("アプリケーションを終了しています...")
    print("クリーンアップ処理完了")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    高度なQApplicationの使用方法を示します。
    """
    # アプリケーションの設定
    app = setup_application()
    
    # ウィンドウの作成と表示
    window = AdvancedWindow()
    window.show()
    
    print("アプリケーションが開始されました")
    
    # イベントループの開始
    exit_code = app.exec()
    
    print(f"アプリケーションが終了しました (終了コード: {exit_code})")
    sys.exit(exit_code)


if __name__ == "__main__":
    main() 