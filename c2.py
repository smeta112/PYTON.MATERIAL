a = int(input("Введите число: "))

sum=0
for i in range(1, a+1):
    if i%5==0:
        continue
    sum=sum+i
print(sum)