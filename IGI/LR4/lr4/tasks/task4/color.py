from utils import SUPPORTED_COLORS, ANSI_COLORS
from utils.errors.entity_errors import InvalidColorError


class Color:
    def __init__(self, color_name: str):
        self.color = color_name


    def get_color(self):
        return self._color


    def set_color(self, value):
        if value not in SUPPORTED_COLORS:
            raise InvalidColorError(value)
        self._color = value

    color = property(get_color, set_color)

    def __str__(self):
        return f"{ANSI_COLORS[self.color]}{self.color}{ANSI_COLORS["reset"]}"
