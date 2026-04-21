import tkinter as tk
import pyautogui
import time
import sys

# 禁用防故障
pyautogui.FAILSAFE = False

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("自动防锁屏(强效版)")
        self.root.geometry("300x150")
        
        self.label = tk.Label(root, text="🚀 强效防锁屏已启用", font=("Arial", 12, "bold"), fg="#FF0000")
        self.label.pack(pady=20)
        
        self.exit_button = tk.Button(root, text="停止并退出", command=self.on_closing)
        self.exit_button.pack(pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.jiggle_mouse()

    def jiggle_mouse(self):
        try:
            # 绝招1：按下无害的 F15 键，向系统发送真实的键盘活动信号
            pyautogui.press('f15')
            
            # 绝招2：模拟人类移动鼠标（移动幅度稍微大一点，且不要瞬间完成）
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 5, y + 5)
            
            # 短暂亦可接受的停顿，骗过系统的判定
            self.root.update()
            time.sleep(0.1) 
            
            pyautogui.moveTo(x, y)
        except Exception:
            pass
        
        # 依然是每 60 秒触发一次
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
