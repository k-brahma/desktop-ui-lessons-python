"""
QTableWidget基本サンプル - テーブル表示の基本機能

このモジュールは、PySide6のQTableWidgetクラスの基本的な使用方法を示します。
QTableWidgetは、表形式のデータを表示・編集するためのウィジェットです。

主要な学習ポイント:
- 基本的なテーブルの作成と設定
- セルへのデータ設定
- ヘッダーの設定
- 選択動作の制御
- 基本的なテーブル操作

Authors: PySide6 Learning Team
Date: 2024
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class BasicTableWindow(QWidget):
    """
    基本的なQTableWidgetの使用例を示すウィンドウクラス
    
    学生の成績表を模したテーブルを表示し、基本的な操作を実演します。
    """
    
    def __init__(self):
        """
        BasicTableWindowクラスのコンストラクタ
        
        ウィンドウの初期設定とテーブルの作成を行います。
        """
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """
        ユーザーインターフェースの初期化
        
        ウィンドウのレイアウトとテーブルの設定を行います。
        """
        self.setWindowTitle("QTableWidget基本サンプル - 学生成績表")
        self.setGeometry(200, 200, 700, 500)
        
        # メインレイアウト
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 説明ラベル
        info_label = QLabel("学生成績管理テーブル - セルをクリックして選択できます")
        info_label.setStyleSheet("""
            QLabel {
                background-color: #e3f2fd;
                padding: 10px;
                border: 1px solid #2196f3;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        layout.addWidget(info_label)
        
        # テーブルの作成
        self.create_table()
        layout.addWidget(self.table)
        
        # 操作ボタン
        self.create_control_buttons(layout)
        
        # ステータスラベル
        self.status_label = QLabel("準備完了")
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #f5f5f5;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 3px;
            }
        """)
        layout.addWidget(self.status_label)
        
    def create_table(self):
        """
        基本的なテーブルの作成と設定
        
        学生の成績データを含むテーブルを作成します。
        """
        # テーブルウィジェットの作成
        self.table = QTableWidget()
        
        # テーブルのサイズを設定（行数、列数）
        self.table.setRowCount(8)
        self.table.setColumnCount(5)
        
        # ヘッダーの設定
        headers = ["学生番号", "氏名", "数学", "英語", "平均点"]
        self.table.setHorizontalHeaderLabels(headers)
        
        # サンプルデータの追加
        sample_data = [
            ["001", "田中太郎", "85", "78", "81.5"],
            ["002", "佐藤花子", "92", "88", "90.0"],
            ["003", "山田次郎", "76", "82", "79.0"],
            ["004", "鈴木美咲", "89", "91", "90.0"],
            ["005", "高橋健太", "73", "75", "74.0"],
            ["006", "渡辺さくら", "95", "89", "92.0"],
            ["007", "伊藤大輔", "81", "79", "80.0"],
            ["008", "中村愛", "88", "93", "90.5"]
        ]
        
        # データをテーブルに設定
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                
                # 平均点列は編集不可に設定
                if col == 4:  # 平均点列
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    # 平均点に応じて背景色を設定
                    avg = float(value)
                    if avg >= 90:
                        item.setBackground(Qt.green)
                    elif avg >= 80:
                        item.setBackground(Qt.yellow)
                    elif avg < 75:
                        item.setBackground(Qt.red)
                
                self.table.setItem(row, col, item)
        
        # テーブルの表示設定
        self.setup_table_appearance()
        
        # シグナルの接続
        self.table.cellClicked.connect(self.on_cell_clicked)
        self.table.cellChanged.connect(self.on_cell_changed)
        
    def setup_table_appearance(self):
        """
        テーブルの外観設定
        
        テーブルのサイズ調整、選択動作、グリッド表示などを設定します。
        """
        # 列幅の自動調整
        self.table.resizeColumnsToContents()
        
        # 行の高さを統一
        self.table.verticalHeader().setDefaultSectionSize(30)
        
        # 選択動作の設定（行全体を選択）
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        
        # 選択モード（単一行選択）
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        
        # グリッドの表示
        self.table.setShowGrid(True)
        
        # 水平ヘッダーのストレッチ（最後の列を自動調整）
        self.table.horizontalHeader().setStretchLastSection(True)
        
        # テーブルのスタイル設定
        self.table.setStyleSheet("""
            QTableWidget {
                gridline-color: #d0d0d0;
                background-color: white;
                alternate-background-color: #f5f5f5;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 8px;
                font-weight: bold;
                border: 1px solid #2c3e50;
            }
        """)
        
        # 交互の行の色を有効化
        self.table.setAlternatingRowColors(True)
        
    def create_control_buttons(self, layout):
        """
        制御ボタンの作成
        
        Args:
            layout (QVBoxLayout): ボタンを追加するレイアウト
        """
        button_layout = QHBoxLayout()
        
        # 行追加ボタン
        add_row_button = QPushButton("行を追加")
        add_row_button.clicked.connect(self.add_row)
        add_row_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
        """)
        button_layout.addWidget(add_row_button)
        
        # 選択行削除ボタン
        delete_row_button = QPushButton("選択行を削除")
        delete_row_button.clicked.connect(self.delete_selected_row)
        delete_row_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        button_layout.addWidget(delete_row_button)
        
        # データクリアボタン
        clear_button = QPushButton("全データクリア")
        clear_button.clicked.connect(self.clear_all_data)
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        button_layout.addWidget(clear_button)
        
        layout.addLayout(button_layout)
        
    def on_cell_clicked(self, row, column):
        """
        セルクリック時の処理
        
        Args:
            row (int): クリックされた行
            column (int): クリックされた列
        """
        item = self.table.item(row, column)
        if item:
            value = item.text()
            header = self.table.horizontalHeaderItem(column).text()
            self.status_label.setText(f"選択: {header} = {value} (行{row+1}, 列{column+1})")
        
    def on_cell_changed(self, row, column):
        """
        セル値変更時の処理
        
        Args:
            row (int): 変更された行
            column (int): 変更された列
        """
        # 数学または英語の点数が変更された場合、平均点を再計算
        if column in [2, 3]:  # 数学または英語列
            self.recalculate_average(row)
            
        item = self.table.item(row, column)
        if item:
            self.status_label.setText(f"データ変更: 行{row+1} が更新されました")
            
    def recalculate_average(self, row):
        """
        指定行の平均点を再計算
        
        Args:
            row (int): 再計算する行
        """
        try:
            math_item = self.table.item(row, 2)
            english_item = self.table.item(row, 3)
            
            if math_item and english_item:
                math_score = float(math_item.text())
                english_score = float(english_item.text())
                average = (math_score + english_score) / 2
                
                # 平均点セルを更新
                avg_item = QTableWidgetItem(f"{average:.1f}")
                avg_item.setFlags(avg_item.flags() & ~Qt.ItemIsEditable)
                
                # 平均点に応じて背景色を設定
                if average >= 90:
                    avg_item.setBackground(Qt.green)
                elif average >= 80:
                    avg_item.setBackground(Qt.yellow)
                elif average < 75:
                    avg_item.setBackground(Qt.red)
                
                self.table.setItem(row, 4, avg_item)
                
        except (ValueError, AttributeError):
            # 数値でない場合は平均点をクリア
            self.table.setItem(row, 4, QTableWidgetItem("--"))
            
    def add_row(self):
        """
        新しい行の追加
        """
        current_row_count = self.table.rowCount()
        self.table.insertRow(current_row_count)
        
        # 新しい行にデフォルト値を設定
        default_data = [f"{current_row_count+1:03d}", "新しい学生", "0", "0", "0.0"]
        for col, value in enumerate(default_data):
            item = QTableWidgetItem(value)
            if col == 4:  # 平均点列は編集不可
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                item.setBackground(Qt.red)
            self.table.setItem(current_row_count, col, item)
            
        self.status_label.setText(f"新しい行を追加しました (行{current_row_count+1})")
        
    def delete_selected_row(self):
        """
        選択された行の削除
        """
        current_row = self.table.currentRow()
        if current_row >= 0:
            self.table.removeRow(current_row)
            self.status_label.setText(f"行{current_row+1}を削除しました")
        else:
            self.status_label.setText("削除する行を選択してください")
            
    def clear_all_data(self):
        """
        全データのクリア
        """
        self.table.setRowCount(0)
        self.status_label.setText("全データをクリアしました")


def main():
    """
    アプリケーションのメインエントリーポイント
    
    QTableWidgetの基本的な使用方法を実演します。
    """
    app = QApplication(sys.argv)
    
    # ウィンドウの作成と表示
    window = BasicTableWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 