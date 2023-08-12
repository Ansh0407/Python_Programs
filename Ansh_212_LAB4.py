class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")


class Staff(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")


class Professor(Staff):
    def __init__(self, name, age, employee_id, specialization):
        super().__init__(name, age, employee_id)
        self.specialization = specialization

    def display(self):
        super().display()
        print(f"Specialization: {self.specialization}")


class Administrator(Staff):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


print("**************************************************************************")
name = input("Enter name: ")
fname=input("Enter Faculty Name :")
aname=input("Enter Administrator Name :")
age = int(input("Enter age: "))
fage = int(input("Enter faculty age: "))
aage = int(input("Enter administrator age: "))
student_id = input("Enter student ID: ")
employee_id = input("Enter employee ID: ")
administrator_id = input("Enter administrator ID: ")
specialization = input("Enter specialization: ")
department = input("Enter department: ")
print("**************************************************************************")


student = Student(name, age, student_id)
professor = Professor(fname, fage, employee_id, specialization)
administrator = Administrator(aname, aage,administrator_id, department)


print("\nStudent Information:")
student.display()

print("\nProfessor Information:")
professor.display()

print("\nAdministrator Information:")
administrator.display()
