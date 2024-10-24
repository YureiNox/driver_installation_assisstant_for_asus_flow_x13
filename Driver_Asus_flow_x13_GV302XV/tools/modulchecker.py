import os
import sys
import time
import platform

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
PURPLE = "\033[35m"
RESET = "\033[0m"

modul = ["requests"]

def modulchecker():
    try:
        for i in modul:
            __import__(i)
            print(f"Module {i} found")
            return True
    except ImportError:
        print(f"Module {i} not found")
        print("Installing module")
        if platform.system() == "Windows":
            os.system(f"pip install {i}")
        else:
            os.system(f"pip3 install {i}")
        print("Module installed")
        time.sleep(5)
        sys.exit()
        return False

if __name__ == "__main__":
    modulchecker()