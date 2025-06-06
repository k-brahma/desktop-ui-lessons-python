import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 アーキテクチャ例 - QMainWindow")
        self.resize(400, 200)
        
        # 中央ウィジェットとメインレイアウト
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #FFE0B3;")  # 薄いオレンジ
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # 1つ目：LabelとInputの横並び
        top_layout = QHBoxLayout()
        self.label = QLabel("QLabel ラベル")
        self.label.setStyleSheet("background-color: #D3D3D3; color: black;")  # 灰色背景、黒文字
        self.line_edit = QLineEdit("QLineEdit テキストを入力")
        self.line_edit.setStyleSheet("background-color: white; color: black;")  # 白背景、黒文字
        top_layout.addWidget(self.label)
        top_layout.addWidget(self.line_edit)
        
        # 2つ目：ボタンを右寄せ
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()  # 左側にスペーサー
        self.button = QPushButton("QPushButton クリック")
        self.button.setStyleSheet("background-color: #4CAF50; color: white;")  # 緑色背景、白文字
        bottom_layout.addWidget(self.button)
        
        # メインレイアウトに追加
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        
        # シグナルと関数を接続
        self.button.clicked.connect(self.my_function)
    
    def my_function(self):
        print("ボタンがクリックされました") 


if __name__ == "__main__":
    # 1. QApplication を作成（最下層の青い土台）
    app = QApplication(sys.argv)
    
    # 2. QMainWindow を作成（オレンジの層）
    window = MainWindow()
    
    # 3. ウィンドウを表示してイベントループ開始
    window.show()
    sys.exit(app.exec())