import abc

from marshmallow import ValidationError


class Validator(abc.ABC):
    def __call__(self, value):
        self.validate(value)

    @abc.abstractmethod
    def validate(self):
        pass


class StartsWithR(Validator):
    def validate(self, value):
        if value.lower().startswith("r"):
            raise ValidationError("Cannot start with R")


class LongerThanSix(Validator):
    def validate(self, value):
        if len(value) > 6:
            raise ValidationError("Cannot be longer than Six")
