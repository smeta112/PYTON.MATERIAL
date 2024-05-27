class Student:
    def __init__(self, name, age, bal):
        self.name = name
        self.age = age
        self.bal = bal
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_bal(self):
        return self.bal

    def calculate_sum(students):
        sum_bal = 0
        for student in students:
        sum_bal += student.get_bal()

        return sum_bal
student1 = Student("lol", 5, 10)
student2 = Student("nani", 2, 7)
student3 = Student("miha", 4, 1)

print(student1.get_name())
print(student2.get_age())
print(student3.get_bal())

'''student1 = Student("Name1", 5, 10)
print(student1.name)'''

students = [student1, student2, student3]
total_bal = Student.calculate_sum(students)
print(total_bal)
