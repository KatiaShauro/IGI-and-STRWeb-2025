import statistics
from copy import copy
import numpy as np

from utils.errors import InvalidCArrayError


class NumPyClass:
    def __init__(self, n: int = 2, m: int = 3, N : int = 100):
        self.arr = np.random.randint(1, N + 1, size=(n, m))
        self.c = []
        self.c_len = 0


    def print_arrays(self):
        print(f"\tMAIN ARRAY:\n{self.arr}")
        print(f"\tC-ARRAY:\n{self.c}")


    def all_elements_greater_than_b(self, b: int):
        indexes = np.where(np.abs(self.arr) > np.abs(b))
        self.c = copy(self.arr[indexes])
        self.c_len = len(self.c)
        return self.c


    def calc_median(self):
        if self.c_len:
            return statistics.median(self.c)
        else:
            raise InvalidCArrayError


    def my_median(self):
        if self.c_len:
            if self.c_len + 1 % 2 == 1:
                return sorted(self.c)[self.c_len // 2]
            else:
                return (sorted(self.c)[self.c_len // 2 - 1] +
                        sorted(self.c)[self.c_len // 2]) / 2
        else:
            raise InvalidCArrayError

