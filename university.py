class Department:
    def __init__(self, name="Development"):
        self.name = name
        self.students = []

    def register(self, student):
        self.students.append(student)


class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.lst_name = last_name
        self.age = age

    def say_hello(self):
        print(f"Hello, My name is {self.name}")


# def register_student(name, lst_name, career):
#     student = Person(name, lst_name, career)
#     if student in students:
#         print("Student is on the class")
#     students.append(student)
#     print(students)
#     print(students[0].say_hello())
#     return "Success", 200

run = True

while run:
    name = input("Student Name: ")
    last_name = input("Student Last Name: ")
    age = input("Ages of the student: ")
    career = input("Student Career: ")
    department = Department()
    student = Person(name, last_name, age)
    status = department.register(name, last_name, age)
    print(status)







