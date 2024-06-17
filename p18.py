a = int(input("Введите первое число:" ))
b = int(input("Введите второе число:" ))
c = int(input("Введите третье число:" ))

biggest_number = max(a, b, c)
smallest_number = min(a, b, c)

if a<biggest_number and a>smallest_number:
    aver_number=a
elif b<biggest_number and b>smallest_number:
    aver_number=b
else:
    aver_number=c

print(biggest_number, aver_number, smallest_number)