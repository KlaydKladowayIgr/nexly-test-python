from abc import ABC


class BaseValidator(ABC):
    validation_name: str

    def __init__(self, value: str):
        self.value = value

    def validate(self, validate_value):
        if validate_value != self.value:
            print(f"{self.validation_name} validation failed: expected {validate_value}, found {self.value}")
        else:
            print(f"{self.validation_name} validation passed.")