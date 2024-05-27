import math
class Calc:
    def __init__(self):
        self.result = 0

    def sum(self, num1, num2):
        self.result = num1 + num2

    def razn(self, num1, num2):
        self.result = num1 - num2

    def um(self, num1, num2):
        self.result = num1 * num2

    def dil(self, num1, num2):
        self.result = num1 / num2

calc_1 = Calc()
num1 = 0
num2 = 0
op = ""
a = num1
b = num2
n = True
while n:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    op = input("Enter operation(+ - % *): ")
    if op == "+":
        calc_1.sum(a, b)
    elif op == "-":
        calc_1.razn(a, b)
    elif op == "*":
        calc_1.um(a, b)
    elif op == "/":
        if b != 0:
            calc_1.dil(a, b)
        else:
            print('error')
3
    else:
        print("Command Not Found")
    print(a, op, b, "=", calc_1.result)

    qu = int(input("If u wanna exit, print 0:"))
    if qu == 0:
        n = False
    else:
        n = True




