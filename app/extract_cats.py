import io
import sys

# --- 临时屏蔽 app.py 的 print 输出 ---
sys.stdout = io.StringIO()
from app import CATEGORIES
sys.stdout = sys.__stdout__

# --- 只打印 category keys（小写） ---
if __name__ == "__main__":
    for key in CATEGORIES.keys():
        print(key.lower())