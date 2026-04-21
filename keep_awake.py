import tkinter as tk
import pyautogui
import sys

pyautogui.FAILSAFE = False

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("自动防锁屏(鼠标版)")
        self.root.geometry("300x150")
        
        self.label = tk.Label(root, text="🖱️ 鼠标模拟已启用", font=("Arial", 12, "bold"), fg="#D2691E")
        self.label.pack(pady=20)
        
        self.exit_button = tk.Button(root, text="停止并退出", command=self.on_closing)
        self.exit_button.pack(pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.jiggle_mouse()

    def jiggle_mouse(self):
        try:
            pyautogui.moveRel(1, 0)
            pyautogui.moveRel(-1, 0)
        except Exception:
            pass
        self.jiggle_job = self.root.after(60000, self.jiggle_mouse)

    def on_closing(self):
        if hasattr(self, 'jiggle_job'):
            self.root.after_cancel(self.jiggle_job)
        self.root.destroy()
        sys.exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-topmost", True)
    app = App(root)
    root.mainloop()
