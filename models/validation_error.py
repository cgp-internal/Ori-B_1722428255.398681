from enum import Enum

class ValidationLevel(Enum):
    ERROR = 'error'
    WARNING = 'warning'

class ValidationError:
    def __init__(self, message, level=ValidationLevel.ERROR):
        if not isinstance(level, ValidationLevel):
            raise ValueError("Invalid validation level")
        self.message = message
        self.level = level

    def __str__(self):
        return f'[{self.level.value.upper()}] {self.message}'

    def __repr__(self):
        return f'ValidationError(message={self.message!r}, level={self.level.value!r})'