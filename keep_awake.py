import ctypes
import time
import sys

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def prevent_lock():
    state = ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    ctypes.windll.kernel32.SetThreadExecutionState(state)

def allow_lock():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

if __name__ == "__main__":
    try:
        prevent_lock()
        print("防锁屏已启动，按 Ctrl+C 退出...")
        while True:
            time.sleep(3600) 
    except KeyboardInterrupt:
        allow_lock()
        sys.exit(0)
