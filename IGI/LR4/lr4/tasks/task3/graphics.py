import matplotlib.pyplot as plt
import numpy as np

from tasks.task3 import TaylorSeries


class Graphics(TaylorSeries):
    sys_color = 'r'
    plot_color = 'b'

    def __init__(self, x: float, eps: float):
        super().__init__(x, eps)

    def plot(self, x_range: tuple = (1.1, 5.0), step: float = 0.1):
        xs = np.arange(*x_range, step) # Generates an array of values
        taylor_vals = []
        math_vals = []

        for val in xs:
            self.__init__(val, self.eps)
            self.taylor_series()
            taylor_vals.append(self.sum)
            math_vals.append(self.get_sys_solution())

        plt.figure(figsize=(10, 6))
        plt.plot(xs, taylor_vals, label='Taylor Series', color=self.plot_color)
        plt.plot(xs, math_vals, label='Math log((x+1)/(x-1))', color=self.sys_color, linestyle='--')

        plt.title('Taylor Series vs Math Function')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.annotate("Начало",
                     xy=(xs[0], taylor_vals[0]),
                     xytext=(10, 0),
                     textcoords='offset points')

        plt.savefig("graphics.png")
        plt.show()
