from marshmallow import Schema, fields, post_load

from validators import StartsWithR, LongerThanSix
from member import Member


class MemberSchema(Schema):
    first_name = fields.Str(
        data_key="firstName", validate=[StartsWithR(), LongerThanSix()]
    )

    @post_load
    def make_member(self, data, **kwargs):
        return Member(**data)
