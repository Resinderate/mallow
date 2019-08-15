import abc

from marshmallow import Schema, fields, post_load, ValidationError


class Member:
    def __init__(self, first_name):
        self.first_name = first_name

    def __repr__(self):
        return "<Member(first_name={name})>".format(name=self.first_name)


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


class MemberSchema(Schema):
    first_name = fields.Str(
        data_key="firstName", validate=[StartsWithR(), LongerThanSix()]
    )

    @post_load
    def make_member(self, data, **kwargs):
        return Member(**data)


if __name__ == '__main__':
    s = MemberSchema()
    tom = s.load({"firstName": "tom"})
    print(tom)  # => <Member(first_name=tom)
    blob = s.dump(tom)
    print(blob)  # => {'firstName': 'tom'}
