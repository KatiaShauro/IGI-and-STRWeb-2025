import math

import numpy as np
from matplotlib import pyplot as plt

from tasks.task4 import Color, Shape
from utils.errors.digit_errors import InvalidAngleError


class Rhombus(Shape):
    def __init__(self, side: float = 5, angle: int = 60, color: str = 'blue', name: str = "Rhombus"):
        super().__init__(side)
        self.angle = angle
        self.shape_color = Color(color)
        self.name = name


    @property
    def angle(self):
        return self.__angle


    @angle.setter
    def angle(self, new_value: int):
        if new_value <= 0 or new_value > 90:
            raise InvalidAngleError
        self.__angle = new_value


    def __str__(self):
        return ("{} info:\na = {}\nS = {}\n{}"
                .format(self.name, self.side, self.calc_square(), self.shape_color))


    def calc_square(self):
        return self.side * self.side * math.sin(math.radians(self.angle))


    def get_name(self):
        return self.name


    def plot(self):
        label = input(f"Enter label for {self.name}: ")
        radians = np.deg2rad(self.angle) / 2
        x = np.array([
            0,
           - self.side * np.cos(radians),
            0,
            self.side * np.cos(radians)
        ])

        y = np.array([
            self.side * np.sin(radians),
            0,
            - self.side * np.sin(radians),
            0
        ])

        fig, ax = plt.subplots() # Fig - холст, ax - область с графиком (оси)
        ax.fill(x, y, color=self.shape_color.color, label=label)
        ax.set_aspect('equal') # The same scale is set on the X and Y axes.
        ax.grid(True)
        plt.title(f"{self.name} plot".upper())
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.savefig(f"{self.get_name()}.png")
        plt.show()

