class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def print_name(self):
        print(self.first_name, self.last_name)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print('Welcome', self.first_name, self.last_name, 'to the class of', self.graduation_year)
