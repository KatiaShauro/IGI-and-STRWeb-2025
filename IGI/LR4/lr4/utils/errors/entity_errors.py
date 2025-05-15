from utils.data import SUPPORTED_COLORS

class InvalidTreeError(Exception):
    """Is called when input params for tree are not valid."""
    def __init__(self, message: str):
        super().__init__(f"Invalid tree format because of {message}")


class InvalidColorError(Exception):
    """Is called when input color is not valid."""
    def __init__(self, color_name: str):
        super().__init__(f"Unsupported color '{color_name}'. Supported: {', '.join(SUPPORTED_COLORS)}")


class InvalidCArrayError(Exception):
    """Is called when array C is empty."""
    def __init__(self):
        super().__init__(f"Invalid action, cause C-array is empty!\n"
                         f"Please, perform 'all_elements_grater_than_b()' firstly!")