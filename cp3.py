
def unique_elements(list1, list2):
    result = []
    for num in list1:
        if num not in list2:
            result.append(num)

    for num in list2:
        if num not in list1:
            result.append(num)
    return result

list_1 = input("Введите первый список чисел через пробел: ").split() #оттделять запятыми
new_list1 = []
for el in list_1:
    new_list1.append(int(el))
list_1=new_list1

list_2 = input("Введите второй список чисел через пробел: ").split()
new_list2 = []
for el in list_2:
    new_list2.append(int(el))
list_2=new_list2

unique_list = unique_elements(list_1, list_2)
print(unique_list)

