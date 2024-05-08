
def is_prime(a):
    if a<2:
        return False
    for i in range(2, a):
        if a%i==0:
            return False

    return True

num = int(input("Введите первое число: "))
num1 = int(input("Введите второе число: "))

for i in range(num, num1):
    i += 1
    if is_prime(i):
        print(i)

