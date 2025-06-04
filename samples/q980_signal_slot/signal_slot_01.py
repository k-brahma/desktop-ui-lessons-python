"""
Signal & Slot基本サンプル - シグナルとスロットによる通信

このモジュールは、PySide6のシグナル・スロット機能の基本的な使用方法を示します。
シグナル・スロットは、Qtのコア機能の一つで、オブジェクト間の安全で柔軟な通信を提供します。

主要な学習ポイント:
- カスタムシグナルの定義と送出
- シグナルとスロットの接続・切断
- 引数付きシグナルの使用
- シグナルチェーンとデータバインディング
- 実用的なアプリケーション例

Authors: PySide6 Learning Team
Date: 2024
"""

import random
import sys
from typing import Optional

from PySide6.QtCore import QObject, Qt, QTimer, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QSlider,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class DataModel(QObject):
    """
    データモデルクラス - シグナルを使用してデータ変更を通知
    """
    
    # シグナルの定義
    nameChanged = Signal(str)
    ageChanged = Signal(int)
    scoreChanged = Signal(int)
    dataReset = Signal()
    
    def __init__(self):
        super().__init__()
        self._name = ""
        self._age = 0
        self._score = 0
    
    def get_name(self):
        """名前の取得"""
        return self._name
    
    def set_name(self, value):
        """名前の設定"""
        if self._name != value:
            self._name = value
            self.nameChanged.emit(value)
    
    def get_age(self):
        """年齢の取得"""
        return self._age
    
    def set_age(self, value):
        """年齢の設定"""
        if self._age != value:
            self._age = value
            self.ageChanged.emit(value)
    
    def get_score(self):
        """スコアの取得"""
        return self._score
    
    def set_score(self, value):
        """スコアの設定"""
        if self._score != value:
            self._score = value
            self.scoreChanged.emit(value)
    
    def reset_data(self):
        """データをリセット"""
        self._name = ""
        self._age = 0
        self._score = 0
        self.dataReset.emit()


class TaskProcessor(QObject):
    """
    タスク処理クラス - 非同期処理をシミュレート
    """
    
    # シグナルの定義
    taskStarted = Signal(str)  # タスク名
    progressUpdated = Signal(int)  # 進行率 (0-100)
    taskCompleted = Signal(str, bool)  # タスク名, 成功/失敗
    statusChanged = Signal(str)  # ステータスメッセージ
    
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.current_task = ""
        self.progress = 0
        self.is_running = False
    
    def start_task(self, task_name: str):
        """タスクの開始"""
        if self.is_running:
            self.statusChanged.emit("既にタスクが実行中です")
            return
            
        self.current_task = task_name
        self.progress = 0
        self.is_running = True
        
        self.taskStarted.emit(task_name)
        self.statusChanged.emit(f"タスク '{task_name}' を開始しました")
        
        # ランダムな間隔でタイマーを開始
        interval = random.randint(50, 200)
        self.timer.start(interval)
    
    def update_progress(self):
        """進行状況の更新"""
        self.progress += random.randint(1, 10)
        
        if self.progress >= 100:
            self.progress = 100
            self.timer.stop()
            self.is_running = False
            
            # ランダムで成功/失敗を決定
            success = random.random() > 0.2  # 80%の確率で成功
            self.taskCompleted.emit(self.current_task, success)
            
            if success:
                self.statusChanged.emit(f"タスク '{self.current_task}' が正常に完了しました")
            else:
                self.statusChanged.emit(f"タスク '{self.current_task}' でエラーが発生しました")
        else:
            self.progressUpdated.emit(self.progress)


class Counter(QObject):
    """
    カウンタークラス - シンプルなカウンター機能
    """
    
    # シグナルの定義
    valueChanged = Signal(int)
    limitReached = Signal(int)  # 制限値に達した時
    resetRequested = Signal()
    
    def __init__(self, limit: int = 100):
        super().__init__()
        self._value = 0
        self._limit = limit
    
    def increment(self):
        """値を増加"""
        if self._value < self._limit:
            self._value += 1
            self.valueChanged.emit(self._value)
            
            if self._value >= self._limit:
                self.limitReached.emit(self._limit)
    
    def decrement(self):
        """値を減少"""
        if self._value > 0:
            self._value -= 1
            self.valueChanged.emit(self._value)
    
    def reset(self):
        """値をリセット"""
        self._value = 0
        self.valueChanged.emit(self._value)
        self.resetRequested.emit()
    
    def set_value(self, value: int):
        """値を直接設定"""
        if 0 <= value <= self._limit and value != self._value:
            self._value = value
            self.valueChanged.emit(self._value)


class SignalSlotDemoWindow(QWidget):
    """
    Signal & Slotの使用例を示すウィンドウクラス
    
    様々なシグナル・スロット機能を実演します。
    """
    
    def __init__(self):
        """
        SignalSlotDemoWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とシグナル・スロットサンプルの作成を行います。
        """
        super().__init__()
        
        # モデルとコンポーネントの初期化
        self.data_model = DataModel()
        self.task_processor = TaskProcessor()
        self.counter = Counter(50)
        
        self.init_ui()
        self.setup_connections()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        様々なシグナル・スロットの機能を示すサンプルを配置します。
        """
        self.setWindowTitle("Signal & Slot基本サンプル - シグナルとスロット通信")
        self.setGeometry(200, 200, 1000, 800)
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # タイトル
        self.create_title_section(main_layout)
        
        # 水平レイアウトで左右に分割
        horizontal_layout = QHBoxLayout()
        
        # 左側のカラム
        left_column = QVBoxLayout()
        self.create_data_binding_section(left_column)
        self.create_counter_section(left_column)
        
        # 右側のカラム
        right_column = QVBoxLayout()
        self.create_task_processor_section(right_column)
        self.create_signal_chain_section(right_column)
        
        horizontal_layout.addLayout(left_column)
        horizontal_layout.addLayout(right_column)
        main_layout.addLayout(horizontal_layout)
        
        # ログ表示エリア
        self.create_log_section(main_layout)
        
    def create_title_section(self, layout):
        """
        タイトルセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        title_label = QLabel("Signal & Slot デモンストレーション")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                background-color: #ecf0f1;
                padding: 15px;
                border-radius: 8px;
                border: 2px solid #bdc3c7;
                margin-bottom: 15px;
            }
        """)
        layout.addWidget(title_label)
        
    def create_data_binding_section(self, layout):
        """
        データバインディングセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        data_group = QGroupBox("データバインディング")
        data_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        data_layout = QVBoxLayout()
        
        # 名前入力
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("名前:"))
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("名前を入力...")
        name_layout.addWidget(self.name_edit)
        data_layout.addLayout(name_layout)
        
        # 年齢入力
        age_layout = QHBoxLayout()
        age_layout.addWidget(QLabel("年齢:"))
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setRange(0, 120)
        age_layout.addWidget(self.age_spinbox)
        data_layout.addLayout(age_layout)
        
        # スコア入力
        score_layout = QHBoxLayout()
        score_layout.addWidget(QLabel("スコア:"))
        self.score_slider = QSlider(Qt.Orientation.Horizontal)
        self.score_slider.setRange(0, 100)
        score_layout.addWidget(self.score_slider)
        self.score_label = QLabel("0")
        self.score_label.setMinimumWidth(30)
        score_layout.addWidget(self.score_label)
        data_layout.addLayout(score_layout)
        
        # 表示エリア
        self.data_display = QLabel("データ待ち...")
        self.data_display.setStyleSheet("""
            QLabel {
                background-color: #e8f5e8;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #27ae60;
                margin: 5px 0;
            }
        """)
        data_layout.addWidget(self.data_display)
        
        # リセットボタン
        reset_btn = QPushButton("データをリセット")
        reset_btn.clicked.connect(self.data_model.reset_data)
        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        data_layout.addWidget(reset_btn)
        
        data_group.setLayout(data_layout)
        layout.addWidget(data_group)
        
    def create_counter_section(self, layout):
        """
        カウンターセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        counter_group = QGroupBox("カウンター（シグナルチェーン）")
        counter_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #e74c3c;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        counter_layout = QVBoxLayout()
        
        # カウンター表示
        self.counter_display = QLabel("0")
        self.counter_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.counter_display.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #e74c3c;
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                padding: 20px;
                margin: 10px 0;
            }
        """)
        counter_layout.addWidget(self.counter_display)
        
        # ボタン群
        button_layout = QHBoxLayout()
        
        increment_btn = QPushButton("＋")
        increment_btn.clicked.connect(self.counter.increment)
        increment_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        button_layout.addWidget(increment_btn)
        
        decrement_btn = QPushButton("−")
        decrement_btn.clicked.connect(self.counter.decrement)
        decrement_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        button_layout.addWidget(decrement_btn)
        
        reset_counter_btn = QPushButton("リセット")
        reset_counter_btn.clicked.connect(self.counter.reset)
        reset_counter_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        button_layout.addWidget(reset_counter_btn)
        
        counter_layout.addLayout(button_layout)
        
        counter_group.setLayout(counter_layout)
        layout.addWidget(counter_group)
        
    def create_task_processor_section(self, layout):
        """
        タスク処理セクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        task_group = QGroupBox("非同期タスク処理")
        task_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #9b59b6;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        task_layout = QVBoxLayout()
        
        # タスク選択ボタン
        task_button_layout = QHBoxLayout()
        
        task1_btn = QPushButton("データダウンロード")
        task1_btn.clicked.connect(lambda: self.task_processor.start_task("データダウンロード"))
        task1_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        task_button_layout.addWidget(task1_btn)
        
        task2_btn = QPushButton("ファイル処理")
        task2_btn.clicked.connect(lambda: self.task_processor.start_task("ファイル処理"))
        task2_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d68910;
            }
        """)
        task_button_layout.addWidget(task2_btn)
        
        task3_btn = QPushButton("データベース同期")
        task3_btn.clicked.connect(lambda: self.task_processor.start_task("データベース同期"))
        task3_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        task_button_layout.addWidget(task3_btn)
        
        task_layout.addLayout(task_button_layout)
        
        # 進行状況表示
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                text-align: center;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #9b59b6;
                border-radius: 3px;
            }
        """)
        task_layout.addWidget(self.progress_bar)
        
        # ステータス表示
        self.status_label = QLabel("待機中...")
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                padding: 8px;
                border-radius: 4px;
                border: 1px solid #dee2e6;
                margin: 5px 0;
            }
        """)
        task_layout.addWidget(self.status_label)
        
        task_group.setLayout(task_layout)
        layout.addWidget(task_group)
        
    def create_signal_chain_section(self, layout):
        """
        シグナルチェーンセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        chain_group = QGroupBox("シグナルチェーンのデモ")
        chain_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #f39c12;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        chain_layout = QVBoxLayout()
        
        # 説明
        info_label = QLabel("カウンターが制限値に達すると、自動的にデータがリセットされます")
        info_label.setWordWrap(True)
        info_label.setStyleSheet("color: #5d6d7e; padding: 5px; font-style: italic;")
        chain_layout.addWidget(info_label)
        
        # カウンタースライダー
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(QLabel("カウンター値:"))
        self.counter_slider = QSlider(Qt.Orientation.Horizontal)
        self.counter_slider.setRange(0, 50)
        self.counter_slider.setValue(0)
        slider_layout.addWidget(self.counter_slider)
        self.counter_value_label = QLabel("0")
        self.counter_value_label.setMinimumWidth(30)
        slider_layout.addWidget(self.counter_value_label)
        
        chain_layout.addLayout(slider_layout)
        
        # 連鎖アクションボタン
        chain_btn = QPushButton("連鎖アクション実行")
        chain_btn.clicked.connect(self.trigger_signal_chain)
        chain_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d68910;
            }
        """)
        chain_layout.addWidget(chain_btn)
        
        chain_group.setLayout(chain_layout)
        layout.addWidget(chain_group)
        
    def create_log_section(self, layout):
        """
        ログセクションの作成
        
        Args:
            layout (QVBoxLayout): 追加先のレイアウト
        """
        log_group = QGroupBox("シグナル・スロット通信ログ")
        log_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #2c3e50;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                background-color: white;
            }
        """)
        
        log_layout = QVBoxLayout()
        
        self.log_display = QTextEdit()
        self.log_display.setMaximumHeight(150)
        self.log_display.setPlaceholderText("シグナル・スロットの通信ログがここに表示されます...")
        self.log_display.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Courier New', monospace;
                font-size: 11px;
            }
        """)
        log_layout.addWidget(self.log_display)
        
        # クリアボタン
        clear_log_btn = QPushButton("ログをクリア")
        clear_log_btn.clicked.connect(self.log_display.clear)
        clear_log_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        log_layout.addWidget(clear_log_btn)
        
        log_group.setLayout(log_layout)
        layout.addWidget(log_group)
        
    def setup_connections(self):
        """
        シグナル・スロット接続の設定
        """
        # データバインディング
        self.name_edit.textChanged.connect(self.data_model.set_name)
        self.age_spinbox.valueChanged.connect(self.data_model.set_age)
        self.score_slider.valueChanged.connect(self.data_model.set_score)
        
        # モデルからの通知
        self.data_model.nameChanged.connect(self.on_name_changed)
        self.data_model.ageChanged.connect(self.on_age_changed)
        self.data_model.scoreChanged.connect(self.on_score_changed)
        self.data_model.dataReset.connect(self.on_data_reset)
        
        # カウンター
        self.counter.valueChanged.connect(self.on_counter_value_changed)
        self.counter.limitReached.connect(self.on_counter_limit_reached)
        self.counter.resetRequested.connect(self.on_counter_reset)
        
        # カウンタースライダー
        self.counter_slider.valueChanged.connect(self.counter.set_value)
        self.counter_slider.valueChanged.connect(self.counter_value_label.setNum)
        
        # タスク処理
        self.task_processor.taskStarted.connect(self.on_task_started)
        self.task_processor.progressUpdated.connect(self.on_progress_updated)
        self.task_processor.taskCompleted.connect(self.on_task_completed)
        self.task_processor.statusChanged.connect(self.on_status_changed)
        
        # シグナルチェーン: カウンターが制限値に達したらデータリセット
        self.counter.limitReached.connect(self.data_model.reset_data)
        
    def log_signal(self, message: str):
        """
        シグナル通信をログに記録
        
        Args:
            message (str): ログメッセージ
        """
        self.log_display.append(f"[SIGNAL] {message}")
        
    def update_data_display(self):
        """
        データ表示の更新
        """
        name = self.data_model.get_name() or "未設定"
        age = self.data_model.get_age()
        score = self.data_model.get_score()
        
        self.data_display.setText(f"名前: {name} | 年齢: {age}歳 | スコア: {score}点")
        
    def on_name_changed(self, name: str):
        """名前変更のスロット"""
        self.log_signal(f"名前が変更されました: '{name}'")
        self.update_data_display()
        
    def on_age_changed(self, age: int):
        """年齢変更のスロット"""
        self.log_signal(f"年齢が変更されました: {age}歳")
        self.update_data_display()
        
    def on_score_changed(self, score: int):
        """スコア変更のスロット"""
        self.score_label.setText(str(score))
        self.log_signal(f"スコアが変更されました: {score}点")
        self.update_data_display()
        
    def on_data_reset(self):
        """データリセットのスロット"""
        self.name_edit.clear()
        self.age_spinbox.setValue(0)
        self.score_slider.setValue(0)
        self.log_signal("データがリセットされました")
        self.update_data_display()
        
    def on_counter_value_changed(self, value: int):
        """カウンター値変更のスロット"""
        self.counter_display.setText(str(value))
        self.counter_slider.setValue(value)
        self.log_signal(f"カウンターが変更されました: {value}")
        
    def on_counter_limit_reached(self, limit: int):
        """カウンター制限値到達のスロット"""
        self.log_signal(f"カウンターが制限値 {limit} に達しました！自動リセットを実行...")
        
    def on_counter_reset(self):
        """カウンターリセットのスロット"""
        self.log_signal("カウンターがリセットされました")
        
    def on_task_started(self, task_name: str):
        """タスク開始のスロット"""
        self.progress_bar.setValue(0)
        self.log_signal(f"タスク開始: '{task_name}'")
        
    def on_progress_updated(self, progress: int):
        """進行状況更新のスロット"""
        self.progress_bar.setValue(progress)
        
    def on_task_completed(self, task_name: str, success: bool):
        """タスク完了のスロット"""
        status = "成功" if success else "失敗"
        self.log_signal(f"タスク完了: '{task_name}' - {status}")
        
        if success:
            self.progress_bar.setStyleSheet("""
                QProgressBar::chunk {
                    background-color: #27ae60;
                }
            """)
        else:
            self.progress_bar.setStyleSheet("""
                QProgressBar::chunk {
                    background-color: #e74c3c;
                }
            """)
            
    def on_status_changed(self, status: str):
        """ステータス変更のスロット"""
        self.status_label.setText(status)
        
    def trigger_signal_chain(self):
        """シグナルチェーンのトリガー"""
        self.log_signal("連鎖アクション開始: カウンターを50に設定します")
        self.counter.set_value(50)  # これにより制限値到達 → データリセットの連鎖が発生


def main():
    """
    アプリケーションのメインエントリーポイント
    
    Signal & Slotの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = SignalSlotDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 