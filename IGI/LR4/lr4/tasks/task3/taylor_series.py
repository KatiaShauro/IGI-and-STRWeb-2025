import math
from collections import Counter

from utils import InvalidXError, InvalidEpsilonError


class TaylorSeries:
    def __init__(self, x: float, eps: float):
        try:
            self.x = x
            self.eps = eps
            self.series = []
            self.sum = 0
            self.n = -1
        except (InvalidXError, InvalidEpsilonError) as e:
            print(f"ERROR: {e}")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_value: float):
        if new_value < 1:
            raise InvalidXError
        self.__x = new_value

    @property
    def eps(self):
        return self.__epsilon

    @eps.setter
    def eps(self, new_value: float):
        if not 0 < new_value < 1:
            raise InvalidEpsilonError
        self.__epsilon = new_value


    def get_series(self):
        return self.series


    def get_sys_solution(self):
        return math.log((self.x+1) / (self.x-1), math.exp(1))


    def taylor_series(self):
        """
        Decomposes the logarithm ln((x+1)/(x-1)) into a Taylor series
        :return: dictionary from x, n, resulting sum, system sum, accuracy
        """
        cur_eps = 1
        system_solution = math.log(  # Counting using built-in functions.
            (self.x+1) / (self.x-1),
            math.exp(1)
        )
        try:
            while cur_eps > self.eps and self.n < 500:
                self.n += 1
                member = 2 / ((2*self.n + 1) * self.x**(2*self.n + 1))
                self.series.append(member)
                self.sum += member  # Taylor series expansion.
                cur_eps = abs(self.sum - system_solution)   # Error calculation.

        except OverflowError:
            print("Oh-oh, your chosen precision and base led to overflow :(")

        return (  # Writing the result into columns.
            f"x\t\t\tn\t\tF(x)\t\tMath F(x)\tepsilon\n"
            f"{self.x}\t\t\t{self.n}\t\t{round(self.sum, 5)}\t\t{round(system_solution, 5)}\t\t{self.eps}"
        )


    def evolve_average(self):
        return self.sum / self.n


    def evolve_median(self):
        if self.n + 1 % 2 == 1:
            return sorted(self.series)[self.n // 2]
        else:
            return (sorted(self.series)[self.n // 2 - 1] +
                    sorted(self.series)[self.n // 2]) / 2


    def evolve_mode(self):
        counts = Counter(self.series)
        max_count = max(counts.values())
        if max_count == 1:
            return None
        else:
            return [k for k, v in counts.items() if v == max_count][0]


    def evolve_variance(self):
        m = self.evolve_average()
        return sum((x - m) ** 2 for x in self.series) / self.n


    def evolve_sko(self):
        return math.sqrt(self.evolve_variance())
