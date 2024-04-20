class Student:
    def __init__(self, grades):
        self.name = 'Doca'
        self.grades = grades

    def __str__(self):
        return f'Hello, Wold'

    def __repr__(self):
        return f'Ola, Mundo!'

student = Student((100, 100, 93, 78, 90))
print(student.grades)
