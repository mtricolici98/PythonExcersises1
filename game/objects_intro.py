class Student:

    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade


student_1 = Student("Marius", "Tricolici", 20)

print(student_1.last_name)
print(student_1.first_name)
print(student_1.grade)

student_2 = Student("Iva", "Shighidze", 9)
print(student_2.last_name)
print(student_2.first_name)
print(student_2.grade)
