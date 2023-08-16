import threading
import time

class ControlledThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()

                # thread should do the thing here
                print('Running...')
                time.sleep(1)

    def pause(self):
        self.paused = True
        # If in sleep, we acquire immediately, otherwise we wait for thread
        # to release condition. In race, worker will still see self.paused
        # and begin waiting until it's set back to False
        self.pause_cond.acquire()

    def resume(self):
        self.paused = False
        # Notify the thread to continue
        self.pause_cond.notify()
        # Now release the lock
        self.pause_cond.release()

t = ControlledThread()
t.start()
time.sleep(3)
t.pause()
print('Pausing...')
time.sleep(3)
t.resume()
print('Resuming...')
