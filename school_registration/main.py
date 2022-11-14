from registrator import Registrator
from person import Student
from txt_handler import TxtHandler
from csv_handler import CsvHandler

run = True

while run:
    name = input("Student Name: ")
    last_name = input("Student Last Name: ")
    age = input("Ages of the student: ")
    std_id = input("Student id: ")
    degree = input('Student degree: ')

    txt = TxtHandler()
    csv = CsvHandler()
    department = Registrator(csv)
    student = Student(name, last_name, age, std_id, degree)
    status = department.register(student)
    print(status)