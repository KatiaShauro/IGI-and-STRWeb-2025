from abc import ABC, abstractmethod

from utils.errors.digit_errors import InvalidSideError


class Shape(ABC):
    def __init__(self, side: float):
        self.side = side


    @property
    def side(self):
        return self.__side


    @side.setter
    def side(self, new_value: float):
        if new_value <= 0:
            raise InvalidSideError
        self.__side = new_value


    @abstractmethod
    def calc_square(self):
        return self.side * self.side


    @abstractmethod
    def plot(self):
        pass