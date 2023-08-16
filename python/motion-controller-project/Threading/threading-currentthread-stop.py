import threading
import time

def task():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print("Working...")
        time.sleep(1)
    print("Stopping...")

t = threading.Thread(target=task)
t.start()
time.sleep(5)
t.do_run = False
