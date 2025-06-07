import sys
from datetime import datetime

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    
    # UIファイルを読み込む
    ui_file_name = "button_click.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    
    # UIをロード
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    
    # ボタンクリックイベントの処理を定義
    def on_button_click():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        window.result_label.setText(f"現在の日時: {current_time}")
        print(f"ボタンがクリックされました: {current_time}")
    
    # ボタンクリックイベントを接続
    window.click_button.clicked.connect(on_button_click)
    
    # ウィンドウを表示
    window.show()
    
    # アプリケーションの実行
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 