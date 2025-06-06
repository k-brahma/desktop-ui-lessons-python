import tkinter as tk


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("シンプルウィンドウ")
        self.root.geometry("400x300+100+100")  # width x height + x + y


if __name__ == "__main__":
    window = MainWindow()
    window.root.mainloop() 