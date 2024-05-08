


def is_prime(a):
    if a<2:
        return False
    for i in range(2, a):
        if a%i==0:
            return False

    return True

num = int(input("Введите число: "))

if is_prime(num):
    print(f'{num} простое')
else:
    print(f'{num} не простое')



