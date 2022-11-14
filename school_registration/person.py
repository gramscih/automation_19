class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.lst_name = last_name
        self.age = age

    def say_hello(self):
        print(f"Hello, My name is {self.name}")


class Student(Person):
    def __init__(self, name, last_name, age, std_id, degree):
        super().__init__(name, last_name, age)
        self.std_id = std_id
        self.degree = degree

    def __str__(self):
        return f"Name: {self.name}, Last Name: {self.lst_name}, Age: {self.age}, Student ID: {self.std_id}, Degree: {self.degree}"


class Teacher(Person):
    def __init__(self, name, last_name, age, subject):
        super().__init__(name, last_name, age)
        self.subject = subject