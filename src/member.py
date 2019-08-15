class Member:
    def __init__(self, first_name):
        self.first_name = first_name

    def __repr__(self):
        return "<Member(first_name={name})>".format(name=self.first_name)
