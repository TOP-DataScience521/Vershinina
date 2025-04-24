num = int(input('введите число: '))

sum = 0

for i in range(1,num+1):
    if num % i == 0:
        sum = sum + i 
print(sum)


# введите число: 30
# 72

# введите число: 99
# 156