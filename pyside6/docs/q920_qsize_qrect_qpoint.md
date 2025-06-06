# QSize, QRect, QPoint リファレンス

PySide6における基本図形クラス（座標、サイズ、矩形）についてのリファレンス資料です。

## 概要

これらのクラスは、GUI要素の位置、サイズ、領域を表現するための基本的な図形クラスです。

## QPoint - 座標点

### 基本的な使用方法

```python
from PySide6.QtCore import QPoint

# 座標点の作成
point1 = QPoint(10, 20)
point2 = QPoint(50, 100)

# 座標値の取得
x = point1.x()
y = point1.y()

# 座標値の設定
point1.setX(30)
point1.setY(40)
```

### 座標計算

```python
p1 = QPoint(10, 20)
p2 = QPoint(30, 40)

# 座標の加算・減算
p3 = p1 + p2  # QPoint(40, 60)
p4 = p2 - p1  # QPoint(20, 20)

# 座標の判定
is_null = p1.isNull()  # 座標が(0, 0)かどうか
```

## QSize - サイズ

### 基本的な使用方法

```python
from PySide6.QtCore import QSize

# サイズの作成
size1 = QSize(100, 50)
size2 = QSize(200, 150)

# サイズの取得
width = size1.width()
height = size1.height()

# サイズの設定
size1.setWidth(120)
size1.setHeight(80)
```

### サイズ計算

```python
size1 = QSize(100, 50)
size2 = QSize(200, 150)

# サイズの拡張・縮小
expanded = size1.expandedTo(size2)  # より大きいサイズを取得
bounded = size1.boundedTo(size2)   # より小さいサイズを取得

# 有効性チェック
is_valid = size1.isValid()  # 幅・高さが正の値かどうか
```

## QRect - 矩形

### 基本的な使用方法

```python
from PySide6.QtCore import QRect, QPoint, QSize

# 矩形の作成方法
rect1 = QRect(10, 20, 100, 50)  # x, y, width, height
rect2 = QRect(QPoint(10, 20), QSize(100, 50))  # 位置とサイズから

# 矩形の取得
x = rect1.x()
y = rect1.y()
width = rect1.width()
height = rect1.height()

# 角の座標取得
top_left = rect1.topLeft()
top_right = rect1.topRight()
bottom_left = rect1.bottomLeft()
bottom_right = rect1.bottomRight()
```

### 矩形の操作

```python
rect = QRect(10, 20, 100, 50)

# 位置の移動
rect.moveTo(50, 100)          # 絶対位置に移動
rect.moveTopLeft(QPoint(0, 0)) # 左上角を指定位置に移動

# サイズの変更
rect.setSize(QSize(150, 75))
rect.setWidth(200)
rect.setHeight(100)

# 矩形の拡張・縮小
rect.adjust(-5, -5, 10, 10)   # 左上を(-5, -5)、右下を(10, 10)移動
```

### 矩形の判定

```python
rect1 = QRect(10, 20, 100, 50)
rect2 = QRect(50, 40, 100, 50)
point = QPoint(60, 45)

# 点が矩形内にあるかチェック
contains_point = rect1.contains(point)

# 矩形同士の重なりチェック
intersects = rect1.intersects(rect2)
intersection = rect1.intersected(rect2)  # 重なり部分の矩形

# 矩形の結合
united = rect1.united(rect2)  # 両方を含む最小矩形
```

## ウィジェットでの使用例

### ウィジェットの位置・サイズ設定

```python
from PySide6.QtWidgets import QWidget, QPushButton

widget = QWidget()
button = QPushButton("Click me", widget)

# ジオメトリ設定
widget.setGeometry(QRect(100, 100, 300, 200))
button.setGeometry(10, 10, 100, 30)

# 位置とサイズを個別に設定
widget.move(QPoint(150, 150))
widget.resize(QSize(400, 300))

# 現在の値を取得
current_pos = widget.pos()
current_size = widget.size()
current_rect = widget.geometry()
```

### カスタム描画での使用

```python
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget

class CustomWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # 矩形の描画
        rect = QRect(10, 10, 100, 50)
        painter.drawRect(rect)
        
        # 円の描画（矩形に内接）
        circle_rect = QRect(150, 10, 50, 50)
        painter.drawEllipse(circle_rect)
```

## よく使用されるサイズ定数

```python
from PySide6.QtCore import QSize

# 標準的なサイズ
ICON_SIZE_SMALL = QSize(16, 16)
ICON_SIZE_MEDIUM = QSize(32, 32)
ICON_SIZE_LARGE = QSize(48, 48)

BUTTON_SIZE_SMALL = QSize(80, 25)
BUTTON_SIZE_MEDIUM = QSize(100, 30)
BUTTON_SIZE_LARGE = QSize(120, 35)

WINDOW_SIZE_SMALL = QSize(400, 300)
WINDOW_SIZE_MEDIUM = QSize(800, 600)
WINDOW_SIZE_LARGE = QSize(1200, 900)
```

## 参考リンク

- [Qt Documentation - QPoint](https://doc.qt.io/qt-6/qpoint.html)
- [Qt Documentation - QSize](https://doc.qt.io/qt-6/qsize.html)
- [Qt Documentation - QRect](https://doc.qt.io/qt-6/qrect.html) 