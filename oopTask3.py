class Counter:
    def __init__(self, start=None, stop=None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start and self.stop:
            if self.start < self.stop:
                self.start += 1
                return self.start
            elif self.start == self.stop:
                print("The maximal value is reached")
                return self.start
            return None
        elif self.start:
            self.start += 1
            return self.start
        else:
            self.start = 0
            self.start += 1
            return self.start

    def get(self):
        return self.start


c = Counter(42, 43)
if __name__ == "__main__":
    assert c.increment() == 43
    assert c.get() == 43