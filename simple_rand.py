class NotSoRandom(object):
    def seed(self, a=3):
        """Самый загадочный генератор случайных чисел в мире."""
        self.seedval = a
    def random(self):
        """Смотрите, случайные числа!"""
        self.seedval = (self.seedval * 3) % 19
        return self.seedval
 
_inst = NotSoRandom()
seed = _inst.seed
random = _inst.random


seed(42)
print([ random() for _ in range(100)])