# QApplication

QApplicationは、PySide6アプリケーション全体を管理するクラスです。すべてのGUIアプリケーションで1つだけ作成する必要があります。

## インポート
```python
from PySide6.QtWidgets import QApplication
```

## 基本的な使用方法

```python
import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.show()
sys.exit(app.exec())
```

## 主要なメソッド

### コンストラクタ
```python
QApplication(argv)
```
- **パラメータ**:
  - `argv` (list): コマンドライン引数のリスト（通常は`sys.argv`）

### exec()
```python
app.exec()
```
アプリケーションのメインイベントループを開始します。

**戻り値**: int - アプリケーションの終了コード

### quit()
```python
app.quit()
```
アプリケーションを終了します。

## 使用例

### 基本的なアプリケーション
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

## 注意事項
- 1つのアプリケーションにつき、QApplicationのインスタンスは1つだけ作成してください
- `sys.exit(app.exec())`でアプリケーションを適切に終了させることが重要です 