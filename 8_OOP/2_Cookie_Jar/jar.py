class Jar:
    def __init__(self, capacity=12):

        self._capacity = capacity
        self._size = 0

        if self._capacity < 0:
            raise ValueError()

    def __str__(self):
        return "🍪" * self._size


    def deposit(self, n):
        self._size = self._size + n
        if self._size < 0 or self._size > self._capacity:
            raise ValueError()
        return self.size


    def withdraw(self, n):
        self._size = self._size - n
        if 0 > self._size:
            raise ValueError()
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


"""jar = Jar()
jar.deposit(5)
jar.withdraw(1)
print(jar)
"""
