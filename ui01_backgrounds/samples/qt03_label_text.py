import sys
from datetime import datetime

from PySide6.QtCore import Qt
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
        current_datetime = datetime.now()
        self.result_label = QLabel(current_datetime.strftime("%Y/%m/%d %H:%M:%S"))
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 