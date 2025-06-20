# QMainWindow

QMainWindowは、アプリケーションのメインウィンドウを作成するためのクラスです。ツールバー、メニューバー、ステータスバー、中央ウィジェットなどの標準的なウィンドウ要素を提供します。

## インポート
```python
from PySide6.QtWidgets import QMainWindow
```

## 基本的な使用方法

```python
from PySide6.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("マイアプリ")
        self.setGeometry(100, 100, 800, 600)
```

## 主要なメソッド

### ウィンドウ設定

#### setWindowTitle(title)
```python
self.setWindowTitle("ウィンドウタイトル")
```
ウィンドウのタイトルを設定します。

**パラメータ**:
- `title` (str): ウィンドウのタイトル

#### setGeometry(x, y, width, height)
```python
self.setGeometry(100, 100, 800, 600)
```
ウィンドウの位置とサイズを設定します。

**パラメータ**:
- `x` (int): ウィンドウの左上角のX座標
- `y` (int): ウィンドウの左上角のY座標
- `width` (int): ウィンドウの幅
- `height` (int): ウィンドウの高さ

### 中央ウィジェット

#### setCentralWidget(widget)
```python
central_widget = QWidget()
self.setCentralWidget(central_widget)
```
メインウィンドウの中央領域にウィジェットを設定します。

**パラメータ**:
- `widget` (QWidget): 中央に配置するウィジェット

#### centralWidget()
```python
widget = self.centralWidget()
```
現在の中央ウィジェットを取得します。

**戻り値**: QWidget - 中央ウィジェット

### 表示制御

#### show()
```python
self.show()
```
ウィンドウを表示します。

#### hide()
```python
self.hide()
```
ウィンドウを非表示にします。

#### close()
```python
self.close()
```
ウィンドウを閉じます。

## 使用例

### 基本的なメインウィンドウ
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("サンプルアプリケーション")
        self.setGeometry(100, 100, 400, 300)
        
        # 中央ウィジェットの設定
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # レイアウトの設定
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # ラベルの追加
        label = QLabel("Hello, PySide6!")
        layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

## 注意事項
- QMainWindowには必ず中央ウィジェットを設定してください
- レイアウトは中央ウィジェットに対して設定します
- QMainWindow自体には直接レイアウトを設定できません 