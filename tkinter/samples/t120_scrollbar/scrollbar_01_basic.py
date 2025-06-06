"""
tkinter TextウィジェットとScrollbarの組み合わせ
"""
import tkinter as tk


class BasicScrollbarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Scrollbarの例")
        self.geometry("450x450")
        
        self.create_widgets()
    
    def create_widgets(self):
        # メインフレームを作成し、gridで配置と伸縮の設定
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # Text ウィジェットとScrollbarを作成
        text_widget = tk.Text(main_frame, wrap=tk.NONE) # wrap=tk.NONEで横スクロールも有効に
        v_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=text_widget.yview)
        h_scrollbar = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=text_widget.xview)
        
        # スクロールバーとText ウィジェットを接続
        text_widget.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # gridでウィジェットを配置
        text_widget.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # サンプルテキストを追加
        sample_text = ""
        for i in range(1, 101):
            sample_text += f"行 {i}: これは非常に長いサンプルテキストです。ウィンドウの幅を超えることで、水平スクロールバーの必要性を示します。\n"
        text_widget.insert(1.0, sample_text)

if __name__ == "__main__":
    app = BasicScrollbarApp()
    app.mainloop() 