class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 5
        return self.value

    def decrement(self):
        if self.value >= 5:
            self.value -= 5
        return self.value

    def reset(self):
        self.value = 0
        return self.value