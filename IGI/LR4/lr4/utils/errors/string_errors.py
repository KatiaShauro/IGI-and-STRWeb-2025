class InvalidNameError(ValueError):
    """Is called when the name does not match the expected format."""
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Invalid name: {name}")
