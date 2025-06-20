import sys
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


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
        self.result_label = QLabel("結果がここに表示されます")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        # ボタンの作成
        self.click_button = QPushButton("クリックしてください")
        self.click_button.clicked.connect(self.on_button_click)
        layout.addWidget(self.click_button)

    def on_button_click(self):
        """今の日付時刻を表示する"""
        current_datetime = datetime.now()
        result = current_datetime.strftime("%Y/%m/%d %H:%M:%S")
        self.result_label.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 