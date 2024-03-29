from schemas import MemberSchema


if __name__ == '__main__':
    s = MemberSchema()
    tom = s.load({"firstName": "tom"})
    print(tom)  # => <Member(first_name=tom)
    blob = s.dump(tom)
    print(blob)  # => {'firstName': 'tom'}

    ronan = s.load({"firstName": "ronan"})  # => marshmallow.exceptions.ValidationError: {'firstName': ['Cannot start with R']}
