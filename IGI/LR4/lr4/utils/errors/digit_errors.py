class InvalidCountError(ValueError):
    """Is called when the count does not match the expected format."""
    def __init__(self, count: int):
        self.count = count
        super().__init__(f"Invalid count: {count}")


class InvalidHealthyCountError(ValueError):
    """Is called when the healthy count does not match the expected format or it's bigger than total."""
    def __init__(self, count: int):
        self.count = count
        super().__init__(f"Invalid healthy count: {count}")


class InvalidEpsilonError(ValueError):
    """Is called when entered epsilon |eps| > 1."""
    def __init__(self):
        super().__init__(f"Epsilon must be less than 1 and bigger than 0")


class InvalidXError(ValueError):
    """Is called when entered x less than 1."""
    def __init__(self):
        super().__init__(f"The absolute value of x must be greater than 1")


class InvalidSideError(ValueError):
    """Is called when entered side less than 0."""
    def __init__(self):
        super().__init__(f"The value of shape side must be greater than 0")


class InvalidAngleError(ValueError):
    """Is called when entered angle is not acute."""
    def __init__(self):
        super().__init__(f"The value of angle must be in range from 1 to 90")