numbers = []

while True:
    num = int(input('Введите целое число: '))
    if num % 7 == 0:
        numbers.append(num)
    else:
        res = numbers[::-1]
        for num in res:
            print(num, end = ' ')
        break
        
# Введите целое число: 7
# Введите целое число: 14
# Введите целое число: 21
# Введите целое число: 28
# Введите целое число: 12
# 28 21 14 7