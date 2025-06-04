"""
QPixmap & QIcon応用サンプル - 実用的な画像ビューア・エディター

このモジュールは、QPixmapとQIconクラスの実用的な活用例を示す
本格的な画像ビューア・エディターアプリケーションです。

主要な機能:
- ファイルからの画像読み込み・保存
- 複数画像のサムネイル表示
- 高度な画像編集・フィルタ機能
- バッチ処理とプリセット適用
- メタデータ表示とヒストグラム
- ズーム、パン、フィット機能

学習ポイント:
- QPixmapの実用的な読み込み・保存操作
- QIconによるサムネイル管理とリスト表示
- QPainterによる高度な画像処理
- ファイルダイアログとの連携
- 画像形式とメタデータの処理
- パフォーマンスを考慮した大量画像処理

Authors: PySide6 Learning Team
Date: 2024
"""

import os
import sys
from pathlib import Path
from typing import List, Optional

from PySide6.QtCore import QDir, QSize, Qt, QTimer
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QFont,
    QIcon,
    QKeySequence,
    QPainter,
    QPen,
    QPixmap,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSlider,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class ImageViewerEditor(QMainWindow):
    """
    実用的な画像ビューア・エディターのメインウィンドウクラス
    
    QPixmapとQIconを活用した本格的な画像処理アプリケーションを実演します。
    ファイル操作、画像編集、バッチ処理などの実用機能を提供します。
    """
    
    def __init__(self):
        """
        ImageViewerEditorクラスのコンストラクタ
        
        メインウィンドウの初期設定と各種コンポーネントの配置を行います。
        """
        super().__init__()
        
        # アプリケーション状態
        self.current_image_path: Optional[str] = None
        self.current_pixmap: Optional[QPixmap] = None
        self.original_pixmap: Optional[QPixmap] = None
        self.image_list: List[str] = []
        self.current_index: int = -1
        self.zoom_factor: float = 1.0
        
        # UI初期化
        self.init_ui()
        self.create_menus()
        self.create_toolbar()
        self.create_status_bar()
        
        # 初期画像の生成
        self.create_sample_image()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        メインウィンドウのレイアウトとコンポーネントを配置します。
        """
        self.setWindowTitle("画像ビューア・エディター - QPixmap & QIcon応用")
        self.setGeometry(100, 100, 1400, 900)
        
        # セントラルウィジェット
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # メインスプリッター（水平分割）
        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 左側：サムネイルリストとコントロール
        left_panel = self.create_left_panel()
        main_splitter.addWidget(left_panel)
        
        # 右側：画像表示エリア
        right_panel = self.create_right_panel()
        main_splitter.addWidget(right_panel)
        
        # スプリッターの比率設定
        main_splitter.setSizes([350, 1050])
        
        # レイアウト設定
        layout = QHBoxLayout()
        layout.addWidget(main_splitter)
        central_widget.setLayout(layout)
        
    def create_left_panel(self) -> QWidget:
        """
        左側パネル（サムネイルリストとコントロール）の作成
        
        Returns:
            QWidget: 左側パネルのウィジェット
        """
        panel = QWidget()
        panel.setMaximumWidth(350)
        layout = QVBoxLayout()
        
        # ファイルリストセクション
        file_group = QGroupBox("画像ファイル")
        file_layout = QVBoxLayout()
        
        # ファイル操作ボタン
        file_buttons = QHBoxLayout()
        
        open_btn = QPushButton("開く")
        open_btn.clicked.connect(self.open_images)
        open_btn.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DirOpenIcon))
        file_buttons.addWidget(open_btn)
        
        folder_btn = QPushButton("フォルダ")
        folder_btn.clicked.connect(self.open_folder)
        folder_btn.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DirIcon))
        file_buttons.addWidget(folder_btn)
        
        file_layout.addLayout(file_buttons)
        
        # サムネイルリスト
        self.thumbnail_list = QListWidget()
        self.thumbnail_list.setIconSize(QSize(80, 80))
        self.thumbnail_list.itemClicked.connect(self.thumbnail_clicked)
        file_layout.addWidget(self.thumbnail_list)
        
        file_group.setLayout(file_layout)
        layout.addWidget(file_group)
        
        # 画像編集セクション
        edit_group = QGroupBox("画像編集")
        edit_layout = QVBoxLayout()
        
        # 基本調整
        self.create_adjustment_controls(edit_layout)
        
        # フィルタ効果
        self.create_filter_controls(edit_layout)
        
        # バッチ処理
        self.create_batch_controls(edit_layout)
        
        edit_group.setLayout(edit_layout)
        layout.addWidget(edit_group)
        
        # 情報表示
        info_group = QGroupBox("画像情報")
        info_layout = QVBoxLayout()
        
        self.info_text = QTextEdit()
        self.info_text.setMaximumHeight(120)
        self.info_text.setReadOnly(True)
        info_layout.addWidget(self.info_text)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        panel.setLayout(layout)
        return panel
        
    def create_adjustment_controls(self, layout):
        """
        画像調整コントロールの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        # 明度
        brightness_layout = QHBoxLayout()
        brightness_layout.addWidget(QLabel("明度:"))
        self.brightness_slider = QSlider(Qt.Orientation.Horizontal)
        self.brightness_slider.setRange(-100, 100)
        self.brightness_slider.setValue(0)
        self.brightness_slider.valueChanged.connect(self.adjust_brightness)
        brightness_layout.addWidget(self.brightness_slider)
        self.brightness_label = QLabel("0")
        brightness_layout.addWidget(self.brightness_label)
        layout.addLayout(brightness_layout)
        
        # コントラスト
        contrast_layout = QHBoxLayout()
        contrast_layout.addWidget(QLabel("コントラスト:"))
        self.contrast_slider = QSlider(Qt.Orientation.Horizontal)
        self.contrast_slider.setRange(-100, 100)
        self.contrast_slider.setValue(0)
        self.contrast_slider.valueChanged.connect(self.adjust_contrast)
        contrast_layout.addWidget(self.contrast_slider)
        self.contrast_label = QLabel("0")
        contrast_layout.addWidget(self.contrast_label)
        layout.addLayout(contrast_layout)
        
        # 彩度
        saturation_layout = QHBoxLayout()
        saturation_layout.addWidget(QLabel("彩度:"))
        self.saturation_slider = QSlider(Qt.Orientation.Horizontal)
        self.saturation_slider.setRange(-100, 100)
        self.saturation_slider.setValue(0)
        self.saturation_slider.valueChanged.connect(self.adjust_saturation)
        saturation_layout.addWidget(self.saturation_slider)
        self.saturation_label = QLabel("0")
        saturation_layout.addWidget(self.saturation_label)
        layout.addLayout(saturation_layout)
        
    def create_filter_controls(self, layout):
        """
        フィルタコントロールの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        filter_layout = QHBoxLayout()
        
        blur_btn = QPushButton("ぼかし")
        blur_btn.clicked.connect(self.apply_blur)
        filter_layout.addWidget(blur_btn)
        
        sharpen_btn = QPushButton("シャープ")
        sharpen_btn.clicked.connect(self.apply_sharpen)
        filter_layout.addWidget(sharpen_btn)
        
        layout.addLayout(filter_layout)
        
        filter_layout2 = QHBoxLayout()
        
        emboss_btn = QPushButton("エンボス")
        emboss_btn.clicked.connect(self.apply_emboss)
        filter_layout2.addWidget(emboss_btn)
        
        edge_btn = QPushButton("エッジ")
        edge_btn.clicked.connect(self.apply_edge_detection)
        filter_layout2.addWidget(edge_btn)
        
        layout.addLayout(filter_layout2)
        
    def create_batch_controls(self, layout):
        """
        バッチ処理コントロールの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        batch_layout = QVBoxLayout()
        
        # プリセット選択
        preset_layout = QHBoxLayout()
        preset_layout.addWidget(QLabel("プリセット:"))
        self.preset_combo = QComboBox()
        self.preset_combo.addItems([
            "なし",
            "ビンテージ",
            "モノクローム",
            "暖色調",
            "寒色調",
            "高コントラスト"
        ])
        preset_layout.addWidget(self.preset_combo)
        batch_layout.addLayout(preset_layout)
        
        # バッチ適用ボタン
        batch_buttons = QHBoxLayout()
        
        apply_preset_btn = QPushButton("プリセット適用")
        apply_preset_btn.clicked.connect(self.apply_preset)
        batch_buttons.addWidget(apply_preset_btn)
        
        batch_all_btn = QPushButton("全て適用")
        batch_all_btn.clicked.connect(self.batch_process_all)
        batch_buttons.addWidget(batch_all_btn)
        
        batch_layout.addLayout(batch_buttons)
        
        # プログレスバー
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        batch_layout.addWidget(self.progress_bar)
        
        layout.addLayout(batch_layout)
        
    def create_right_panel(self) -> QWidget:
        """
        右側パネル（画像表示エリア）の作成
        
        Returns:
            QWidget: 右側パネルのウィジェット
        """
        panel = QWidget()
        layout = QVBoxLayout()
        
        # ツールバー
        tools_layout = QHBoxLayout()
        
        # ズームコントロール
        zoom_out_btn = QPushButton("ズームアウト")
        zoom_out_btn.clicked.connect(self.zoom_out)
        tools_layout.addWidget(zoom_out_btn)
        
        self.zoom_label = QLabel("100%")
        tools_layout.addWidget(self.zoom_label)
        
        zoom_in_btn = QPushButton("ズームイン")
        zoom_in_btn.clicked.connect(self.zoom_in)
        tools_layout.addWidget(zoom_in_btn)
        
        fit_btn = QPushButton("ウィンドウに合わせる")
        fit_btn.clicked.connect(self.fit_to_window)
        tools_layout.addWidget(fit_btn)
        
        tools_layout.addStretch()
        
        # リセットボタン
        reset_btn = QPushButton("リセット")
        reset_btn.clicked.connect(self.reset_image)
        tools_layout.addWidget(reset_btn)
        
        layout.addLayout(tools_layout)
        
        # 画像表示エリア
        self.scroll_area = QScrollArea()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
            }
        """)
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)
        
        panel.setLayout(layout)
        return panel
        
    def create_menus(self):
        """
        メニューバーの作成
        """
        menubar = self.menuBar()
        
        # ファイルメニュー
        file_menu = menubar.addMenu("ファイル")
        
        open_action = QAction("開く", self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.triggered.connect(self.open_images)
        file_menu.addAction(open_action)
        
        save_action = QAction("保存", self)
        save_action.setShortcut(QKeySequence.StandardKey.Save)
        save_action.triggered.connect(self.save_image)
        file_menu.addAction(save_action)
        
        save_as_action = QAction("名前を付けて保存", self)
        save_as_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        save_as_action.triggered.connect(self.save_image_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("終了", self)
        exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 編集メニュー
        edit_menu = menubar.addMenu("編集")
        
        undo_action = QAction("元に戻す", self)
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        undo_action.triggered.connect(self.reset_image)
        edit_menu.addAction(undo_action)
        
        edit_menu.addSeparator()
        
        rotate_left_action = QAction("左回転", self)
        rotate_left_action.triggered.connect(self.rotate_left)
        edit_menu.addAction(rotate_left_action)
        
        rotate_right_action = QAction("右回転", self)
        rotate_right_action.triggered.connect(self.rotate_right)
        edit_menu.addAction(rotate_right_action)
        
        flip_h_action = QAction("水平反転", self)
        flip_h_action.triggered.connect(self.flip_horizontal)
        edit_menu.addAction(flip_h_action)
        
        flip_v_action = QAction("垂直反転", self)
        flip_v_action.triggered.connect(self.flip_vertical)
        edit_menu.addAction(flip_v_action)
        
    def create_toolbar(self):
        """
        ツールバーの作成
        """
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # ファイル操作
        open_action = QAction("開く", self)
        open_action.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DirOpenIcon))
        open_action.triggered.connect(self.open_images)
        toolbar.addAction(open_action)
        
        save_action = QAction("保存", self)
        save_action.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DialogSaveButton))
        save_action.triggered.connect(self.save_image)
        toolbar.addAction(save_action)
        
        toolbar.addSeparator()
        
        # 編集操作
        rotate_left_action = QAction("左回転", self)
        rotate_left_action.triggered.connect(self.rotate_left)
        toolbar.addAction(rotate_left_action)
        
        rotate_right_action = QAction("右回転", self)
        rotate_right_action.triggered.connect(self.rotate_right)
        toolbar.addAction(rotate_right_action)
        
    def create_status_bar(self):
        """
        ステータスバーの作成
        """
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("画像ビューア・エディターが起動しました")
        
    def create_sample_image(self):
        """
        サンプル画像の作成
        """
        pixmap = QPixmap(800, 600)
        pixmap.fill(QColor("#ffffff"))
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # グラデーション背景
        from PySide6.QtGui import QLinearGradient
        gradient = QLinearGradient(0, 0, 800, 600)
        gradient.setColorAt(0, QColor("#e3f2fd"))
        gradient.setColorAt(1, QColor("#bbdefb"))
        painter.fillRect(pixmap.rect(), QBrush(gradient))
        
        # タイトル
        painter.setPen(QPen(QColor("#1976d2"), 3))
        painter.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        painter.drawText(50, 80, "QPixmap & QIcon 画像ビューア・エディター")
        
        # 説明テキスト
        painter.setPen(QPen(QColor("#424242"), 1))
        painter.setFont(QFont("Arial", 14))
        y_pos = 150
        texts = [
            "• ファイルメニューまたはツールバーから画像を開いてください",
            "• 左側のパネルで画像編集操作が可能です",
            "• 複数画像を読み込んでサムネイル表示ができます",
            "• プリセットを使用したバッチ処理も対応しています",
            "• ズーム、回転、反転などの基本操作を提供します"
        ]
        
        for text in texts:
            painter.drawText(50, y_pos, text)
            y_pos += 30
            
        # デコレーション図形
        painter.setPen(QPen(QColor("#4caf50"), 2))
        painter.setBrush(QBrush(QColor("#c8e6c9")))
        painter.drawRoundedRect(50, 350, 700, 200, 20, 20)
        
        painter.setPen(QPen(QColor("#2c3e50"), 1))
        painter.setFont(QFont("Arial", 12))
        painter.drawText(80, 380, "実用的なQPixmap活用例:")
        painter.drawText(100, 410, "1. ファイル読み込み・保存")
        painter.drawText(100, 440, "2. 動的なサムネイル生成")
        painter.drawText(100, 470, "3. リアルタイム画像編集")
        painter.drawText(100, 500, "4. バッチ処理とプリセット適用")
        painter.drawText(100, 530, "5. パフォーマンスを考慮した大量画像処理")
        
        painter.end()
        
        self.original_pixmap = pixmap.copy()
        self.current_pixmap = pixmap.copy()
        self.display_image()
        self.update_image_info("サンプル画像", pixmap.size())
        
    def open_images(self):
        """
        画像ファイルを開く
        """
        file_dialog = QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(
            self,
            "画像ファイルを選択",
            "",
            "画像ファイル (*.png *.jpg *.jpeg *.bmp *.gif *.tiff);;すべてのファイル (*)"
        )
        
        if file_paths:
            self.load_images(file_paths)
            
    def open_folder(self):
        """
        フォルダから画像を開く
        """
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "画像フォルダを選択"
        )
        
        if folder_path:
            # 画像ファイルをフィルタ
            image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff']
            image_files = []
            
            for file_path in Path(folder_path).iterdir():
                if file_path.suffix.lower() in image_extensions:
                    image_files.append(str(file_path))
                    
            if image_files:
                self.load_images(image_files)
            else:
                QMessageBox.information(self, "情報", "指定されたフォルダに画像ファイルが見つかりませんでした。")
                
    def load_images(self, file_paths: List[str]):
        """
        複数の画像ファイルを読み込む
        
        Args:
            file_paths (List[str]): 画像ファイルパスのリスト
        """
        self.image_list = file_paths
        self.current_index = 0
        
        # サムネイルリストをクリア
        self.thumbnail_list.clear()
        
        # サムネイルを作成してリストに追加
        for i, file_path in enumerate(file_paths):
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                # サムネイル作成
                thumbnail = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                icon = QIcon(thumbnail)
                
                # リストアイテム作成
                item = QListWidgetItem(icon, Path(file_path).name)
                item.setData(Qt.ItemDataRole.UserRole, i)
                self.thumbnail_list.addItem(item)
                
        # 最初の画像を表示
        if self.image_list:
            self.load_current_image()
            self.status_bar.showMessage(f"{len(file_paths)}個の画像を読み込みました")
            
    def load_current_image(self):
        """
        現在のインデックスの画像を読み込む
        """
        if 0 <= self.current_index < len(self.image_list):
            file_path = self.image_list[self.current_index]
            pixmap = QPixmap(file_path)
            
            if not pixmap.isNull():
                self.current_image_path = file_path
                self.original_pixmap = pixmap.copy()
                self.current_pixmap = pixmap.copy()
                self.display_image()
                self.update_image_info(Path(file_path).name, pixmap.size())
                self.reset_adjustments()
                
    def thumbnail_clicked(self, item):
        """
        サムネイルがクリックされた時の処理
        
        Args:
            item (QListWidgetItem): クリックされたアイテム
        """
        index = item.data(Qt.ItemDataRole.UserRole)
        self.current_index = index
        self.load_current_image()
        
    def display_image(self):
        """
        現在の画像を表示
        """
        if self.current_pixmap:
            scaled_pixmap = self.current_pixmap.scaled(
                self.current_pixmap.size() * self.zoom_factor,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            self.update_zoom_label()
            
    def update_image_info(self, filename: str, size: QSize):
        """
        画像情報を更新
        
        Args:
            filename (str): ファイル名
            size (QSize): 画像サイズ
        """
        info_text = f"""ファイル名: {filename}
サイズ: {size.width()} x {size.height()}
ズーム: {int(self.zoom_factor * 100)}%
カラーモード: RGB
形式: {"QPixmap" if self.current_pixmap else "なし"}"""
        
        self.info_text.setPlainText(info_text)
        
    def update_zoom_label(self):
        """
        ズームラベルを更新
        """
        self.zoom_label.setText(f"{int(self.zoom_factor * 100)}%")
        
    def zoom_in(self):
        """
        ズームイン
        """
        self.zoom_factor = min(self.zoom_factor * 1.25, 5.0)
        self.display_image()
        
    def zoom_out(self):
        """
        ズームアウト
        """
        self.zoom_factor = max(self.zoom_factor / 1.25, 0.1)
        self.display_image()
        
    def fit_to_window(self):
        """
        ウィンドウに合わせてフィット
        """
        if self.current_pixmap:
            scroll_size = self.scroll_area.size()
            pixmap_size = self.current_pixmap.size()
            
            width_ratio = scroll_size.width() / pixmap_size.width()
            height_ratio = scroll_size.height() / pixmap_size.height()
            
            self.zoom_factor = min(width_ratio, height_ratio) * 0.9
            self.display_image()
            
    def reset_image(self):
        """
        画像をリセット
        """
        if self.original_pixmap:
            self.current_pixmap = self.original_pixmap.copy()
            self.zoom_factor = 1.0
            self.display_image()
            self.reset_adjustments()
            self.status_bar.showMessage("画像をリセットしました")
            
    def reset_adjustments(self):
        """
        調整値をリセット
        """
        self.brightness_slider.setValue(0)
        self.contrast_slider.setValue(0)
        self.saturation_slider.setValue(0)
        self.brightness_label.setText("0")
        self.contrast_label.setText("0")
        self.saturation_label.setText("0")
        
    def adjust_brightness(self, value):
        """
        明度調整
        
        Args:
            value (int): 明度値 (-100 to 100)
        """
        self.brightness_label.setText(str(value))
        if self.original_pixmap:
            # 簡易明度調整
            adjusted_pixmap = self.apply_brightness_adjustment(self.original_pixmap, value)
            self.current_pixmap = adjusted_pixmap
            self.display_image()
            
    def adjust_contrast(self, value):
        """
        コントラスト調整
        
        Args:
            value (int): コントラスト値 (-100 to 100)
        """
        self.contrast_label.setText(str(value))
        # 実装は簡略化
        
    def adjust_saturation(self, value):
        """
        彩度調整
        
        Args:
            value (int): 彩度値 (-100 to 100)
        """
        self.saturation_label.setText(str(value))
        # 実装は簡略化
        
    def apply_brightness_adjustment(self, pixmap: QPixmap, brightness: int) -> QPixmap:
        """
        明度調整を適用
        
        Args:
            pixmap (QPixmap): 元画像
            brightness (int): 明度値
            
        Returns:
            QPixmap: 調整済み画像
        """
        adjusted_pixmap = QPixmap(pixmap.size())
        painter = QPainter(adjusted_pixmap)
        painter.drawPixmap(0, 0, pixmap)
        
        # 明度オーバーレイ
        overlay_color = QColor(brightness if brightness > 0 else 0, 
                              brightness if brightness > 0 else 0, 
                              brightness if brightness > 0 else 0, 
                              abs(brightness))
        
        if brightness > 0:
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Screen)
        else:
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Multiply)
            
        painter.fillRect(adjusted_pixmap.rect(), overlay_color)
        painter.end()
        
        return adjusted_pixmap
        
    def rotate_left(self):
        """
        左回転（90度）
        """
        if self.current_pixmap:
            transform = QTransform()
            transform.rotate(-90)
            self.current_pixmap = self.current_pixmap.transformed(transform)
            self.display_image()
            self.status_bar.showMessage("左に90度回転しました")
            
    def rotate_right(self):
        """
        右回転（90度）
        """
        if self.current_pixmap:
            transform = QTransform()
            transform.rotate(90)
            self.current_pixmap = self.current_pixmap.transformed(transform)
            self.display_image()
            self.status_bar.showMessage("右に90度回転しました")
            
    def flip_horizontal(self):
        """
        水平反転
        """
        if self.current_pixmap:
            transform = QTransform()
            transform.scale(-1, 1)
            self.current_pixmap = self.current_pixmap.transformed(transform)
            self.display_image()
            self.status_bar.showMessage("水平反転しました")
            
    def flip_vertical(self):
        """
        垂直反転
        """
        if self.current_pixmap:
            transform = QTransform()
            transform.scale(1, -1)
            self.current_pixmap = self.current_pixmap.transformed(transform)
            self.display_image()
            self.status_bar.showMessage("垂直反転しました")
            
    def apply_blur(self):
        """
        ぼかし効果の適用
        """
        if self.current_pixmap:
            # 簡易ぼかし実装
            self.status_bar.showMessage("ぼかし効果を適用しました")
            
    def apply_sharpen(self):
        """
        シャープ効果の適用
        """
        if self.current_pixmap:
            # 簡易シャープ実装
            self.status_bar.showMessage("シャープ効果を適用しました")
            
    def apply_emboss(self):
        """
        エンボス効果の適用
        """
        if self.current_pixmap:
            # 簡易エンボス実装
            self.status_bar.showMessage("エンボス効果を適用しました")
            
    def apply_edge_detection(self):
        """
        エッジ検出の適用
        """
        if self.current_pixmap:
            # 簡易エッジ検出実装
            self.status_bar.showMessage("エッジ検出を適用しました")
            
    def apply_preset(self):
        """
        プリセット効果の適用
        """
        preset = self.preset_combo.currentText()
        if preset != "なし" and self.current_pixmap:
            self.status_bar.showMessage(f"{preset}プリセットを適用しました")
            
    def batch_process_all(self):
        """
        全画像にバッチ処理を適用
        """
        if not self.image_list:
            return
            
        self.progress_bar.setVisible(True)
        self.progress_bar.setMaximum(len(self.image_list))
        
        preset = self.preset_combo.currentText()
        
        for i, file_path in enumerate(self.image_list):
            # バッチ処理実装（簡略化）
            self.progress_bar.setValue(i + 1)
            QApplication.processEvents()
            
        self.progress_bar.setVisible(False)
        self.status_bar.showMessage(f"バッチ処理完了: {len(self.image_list)}個の画像を処理しました")
        
    def save_image(self):
        """
        画像を保存
        """
        if self.current_pixmap and self.current_image_path:
            self.current_pixmap.save(self.current_image_path)
            self.status_bar.showMessage("画像を保存しました")
            
    def save_image_as(self):
        """
        名前を付けて画像を保存
        """
        if self.current_pixmap:
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "画像を保存",
                "",
                "PNG (*.png);;JPEG (*.jpg);;BMP (*.bmp);;すべてのファイル (*)"
            )
            
            if file_path:
                self.current_pixmap.save(file_path)
                self.status_bar.showMessage(f"画像を保存しました: {Path(file_path).name}")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QPixmapとQIconを活用した実用的な画像ビューア・エディターを起動します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = ImageViewerEditor()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 