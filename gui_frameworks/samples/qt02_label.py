import sys
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ボタンクリックデモ")
        self.setGeometry(100, 100, 400, 300)

        # メインウィジェットとレイアウトの設定
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # ラベルの作成
        self.result_label = QLabel("こんにちはようこそ！")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        # ラベルの背景色を変更
        self.result_label.setStyleSheet("background-color: #000000; color: #ffffff;")

        # ラベルのフォントを変更
        self.result_label.setFont(QFont("Arial", 20))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 