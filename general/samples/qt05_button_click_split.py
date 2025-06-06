import sys
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
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
        # メインウィジェットとレイアウトの設定
        self._setup_main_widget()

        # ラベルの作成
        self._setup_label()

        # ボタンの作成
        self._setup_button()

    def _setup_main_widget(self):
        """メインウィジェットの作成"""
        self.setWindowTitle("ボタンクリックデモ")
        self.setGeometry(100, 100, 400, 300)

        self._main_widget = QWidget()
        self.setCentralWidget(self._main_widget)        
        self._setup_layout()

    def _setup_layout(self):
        """レイアウトの作成"""
        self._layout = QVBoxLayout()
        self._main_widget.setLayout(self._layout)

    def _setup_label(self):
        """ラベルの作成"""
        self.result_label = QLabel("結果がここに表示されます")
        self.result_label.setAlignment(Qt.AlignCenter)
        self._layout.addWidget(self.result_label)

        self.result_label.setStyleSheet("background-color: #000000; color: #ffffff;")
        self.result_label.setFont(QFont("Arial", 20))

    def _setup_button(self):
        """ボタンの作成"""
        self.click_button = QPushButton("クリックしてください")
        self.click_button.clicked.connect(self.on_button_click)
        self._layout.addWidget(self.click_button)

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