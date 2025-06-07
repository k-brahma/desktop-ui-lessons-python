# QLabel

QLabelは、テキストや画像を表示するためのウィジェットです。静的なコンテンツの表示に使用されます。

## インポート
```python
from PySide6.QtWidgets import QLabel
```

## 基本的な使用方法

```python
from PySide6.QtWidgets import QLabel

label = QLabel("Hello, World!")
```

## 主要なメソッド

### テキスト設定

#### setText(text)
```python
label.setText("新しいテキスト")
```
ラベルに表示するテキストを設定します。

**パラメータ**:
- `text` (str): 表示するテキスト

#### text()
```python
current_text = label.text()
```
現在のテキストを取得します。

**戻り値**: str - 現在表示されているテキスト

### テキスト配置

#### setAlignment(alignment)
```python
from PySide6.QtCore import Qt
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
```
テキストの配置を設定します。

**パラメータ**:
- `alignment` (Qt.AlignmentFlag): 配置方法
  - `Qt.AlignmentFlag.AlignLeft` - 左揃え
  - `Qt.AlignmentFlag.AlignRight` - 右揃え
  - `Qt.AlignmentFlag.AlignCenter` - 中央揃え
  - `Qt.AlignmentFlag.AlignTop` - 上揃え
  - `Qt.AlignmentFlag.AlignBottom` - 下揃え

### スタイル設定

#### setStyleSheet(styleSheet)
```python
label.setStyleSheet("background-color: #ff0000; color: #ffffff;")
```
CSSライクなスタイルシートを設定します。

**パラメータ**:
- `styleSheet` (str): スタイルシート文字列

#### setFont(font)
```python
from PySide6.QtGui import QFont
font = QFont("Arial", 14)
label.setFont(font)
```
フォントを設定します。

**パラメータ**:
- `font` (QFont): 設定するフォント

### 画像表示

#### setPixmap(pixmap)
```python
from PySide6.QtGui import QPixmap
pixmap = QPixmap("image.png")
label.setPixmap(pixmap)
```
ラベルに画像を表示します。

**パラメータ**:
- `pixmap` (QPixmap): 表示する画像

### その他の設定

#### setWordWrap(on)
```python
label.setWordWrap(True)
```
長いテキストの自動改行を有効/無効にします。

**パラメータ**:
- `on` (bool): True で自動改行を有効

## 使用例

### 基本的なラベル
```python
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 基本的なラベル
        label1 = QLabel("こんにちは！")
        layout.addWidget(label1)
        
        # 中央揃えのラベル
        label2 = QLabel("中央揃えテキスト")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

### スタイル付きラベル
```python
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

label = QLabel("スタイル付きラベル")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setStyleSheet("""
    background-color: #2c3e50;
    color: #ecf0f1;
    border: 2px solid #3498db;
    border-radius: 10px;
    padding: 10px;
""")
label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
```

### 動的テキスト更新
```python
from datetime import datetime
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

class TimeDisplay(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.time_label = QLabel("時刻が表示されます")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        update_button = QPushButton("時刻更新")
        update_button.clicked.connect(self.update_time)
        
        layout.addWidget(self.time_label)
        layout.addWidget(update_button)
    
    def update_time(self):
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.time_label.setText(current_time)
```

## よく使用されるスタイルシートプロパティ

```css
/* 背景色 */
background-color: #3498db;

/* 文字色 */
color: #ffffff;

/* ボーダー */
border: 2px solid #2c3e50;
border-radius: 5px;

/* パディング */
padding: 10px;

/* マージン */
margin: 5px;

/* フォントサイズ */
font-size: 16px;
font-weight: bold;
```

## 注意事項
- テキストと画像の両方を同時に表示することはできません
- 長いテキストを表示する場合は `setWordWrap(True)` を使用してください
- アライメントは複数の値を組み合わせることができます（例: `Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop`） 