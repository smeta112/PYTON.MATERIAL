
def is_power_of_two(number):
    while number%2==0 and number>1:
        number=number/2
    return number ==1

def power_of_two(numbers):
    list_1 = []
    for num in numbers:
        if is_power_of_two(num):
            list_1.append(num)
    return list_1

numbers=[1, 2, 4, 56, 67, 35, 34, 24, 26, 28, 89, 9 , 32]
list_1 = power_of_two(numbers)
print(list_1)





