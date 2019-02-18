from myclass import Person

class Student(Person, object):
    def __init__(self, name, surname, id):
        self.id = id
        super(Student, self).__init__(name, surname)
    
    def __repr__(self):
        return '{} {} | id: {}'.format(self.name, self.surname, self.id)
    
    def change_name(self, new_name):
        self.name = new_name