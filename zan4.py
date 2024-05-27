import math
class Treug:
    def __init__(self, st1, st2, st3):
        self.st1 = st1
        self.st2= st2
        self.st3 = st3

    def p(self, st1, st2, st3):
            self.result = (st1 + st2 + st3)/2

    def sqier(self, st1, st2, st3):
            self.result = math.sqrt(p*(p-st1)*(p-st2)*(p-st3))
a = int(input("Enter 1st stor: "))
b = int(input("Enter 2nd stor: "))
c = int(input("Enter 3rd stor: "))
st1 = a
st2 = b
st3 = c

