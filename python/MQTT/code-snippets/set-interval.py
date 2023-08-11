from threading import Timer

class Repeat(Timer):
    def __init__(self, interval, function, args=None, kwargs=None):
        super(Repeat, self).__init__(interval, self._function_wrapper, args=args, kwargs=kwargs)
        self.function = function

    def _function_wrapper(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self._function_wrapper(*self.args, **self.kwargs)

def action(name, greeting):
    print(f"{greeting}, {name}!")

t = Repeat(1.0, action, args=("World", "Hello"))
t.start()
