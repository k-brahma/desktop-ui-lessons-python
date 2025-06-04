# QColor リファレンス

PySide6における色の定義と操作についてのリファレンス資料です。

## 概要

`QColor`クラスは、色を表現し操作するためのクラスです。RGB、HSV、CMYK、HSLなど様々な色空間をサポートします。

## 基本的な使用方法

### 色の作成

```python
from PySide6.QtGui import QColor

# RGB値から作成
color1 = QColor(255, 0, 0)  # 赤
color2 = QColor(0, 255, 0)  # 緑
color3 = QColor(0, 0, 255)  # 青

# 16進数から作成
color4 = QColor("#FF0000")  # 赤
color5 = QColor("#00FF00")  # 緑

# 色名から作成
color6 = QColor("red")
color7 = QColor("blue")
```

## 標準色名

| 色名 | RGB値 | 16進数 |
|------|-------|--------|
| red | (255, 0, 0) | #FF0000 |
| green | (0, 128, 0) | #008000 |
| blue | (0, 0, 255) | #0000FF |
| yellow | (255, 255, 0) | #FFFF00 |
| cyan | (0, 255, 255) | #00FFFF |
| magenta | (255, 0, 255) | #FF00FF |
| black | (0, 0, 0) | #000000 |
| white | (255, 255, 255) | #FFFFFF |
| gray | (128, 128, 128) | #808080 |

## 色空間の変換

### RGB値の取得・設定

```python
color = QColor(255, 128, 64)

# RGB値の取得
r = color.red()
g = color.green()
b = color.blue()
a = color.alpha()  # アルファ値（透明度）

# RGB値の設定
color.setRed(200)
color.setGreen(100)
color.setBlue(50)
color.setAlpha(200)  # 透明度設定
```

### HSV値の操作

```python
color = QColor()

# HSV値から設定
color.setHsv(120, 255, 255)  # 色相, 彩度, 明度

# HSV値の取得
h = color.hue()
s = color.saturation()
v = color.value()
```

## スタイルシートでの使用

```python
# ウィジェットのスタイル設定
widget.setStyleSheet("""
    QPushButton {
        background-color: #3498db;
        color: white;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
""")
```

## よく使用される色パレット

### Material Design Colors

```python
# Primary Colors
BLUE_500 = QColor("#2196F3")
RED_500 = QColor("#F44336")
GREEN_500 = QColor("#4CAF50")

# Gray Scale
GRAY_50 = QColor("#FAFAFA")
GRAY_100 = QColor("#F5F5F5")
GRAY_200 = QColor("#EEEEEE")
GRAY_300 = QColor("#E0E0E0")
```

## 参考リンク

- [Qt Documentation - QColor](https://doc.qt.io/qt-6/qcolor.html)
- [PySide6 QColor](https://doc.qt.io/qtforpython/PySide6/QtGui/QColor.html) 