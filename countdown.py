class Counter:
    def __init__(self):
        self.value = 0

    def incr(self):
        self.value += 1
        print("ANSWER:", self.value, "incremented by 1")

    def decr(self):
        self.value -= 1
        print("ANSWER:", self.value, "decremented by 1")

    def incrby(self, n):
        self.value += n
        print("ANSWER:", self.value, "incremented by", n)

    def decrby(self, n):
        self.value -= n
        print("ANSWER:", self.value, "decremented by", n)


counter = Counter()
counter.incr()
counter.incr()
counter.decr()
counter.incrby(5)
counter.decrby(5)
