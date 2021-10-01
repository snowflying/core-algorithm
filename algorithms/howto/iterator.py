class Event():
    def __init__(self, size):
        self.n = 2
        self._max = size

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self._max:
            value = self.n
            self.n = self.n + 2
            return value
        else:
            raise StopIteration


eve = Event(25)
print(dir(eve))
print(next(eve))
print(next(eve))
print(next(eve))