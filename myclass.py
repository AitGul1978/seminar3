class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return '{} {}'.format(self.name, self.surname)

    def change_name(self, new_name):
        self.name = new_name
