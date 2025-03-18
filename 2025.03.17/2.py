num1 = int(input('введите число: '))
num2 = int(input('введите второе число: '))

if num1%num2 ==0:
    print(f'{num1} делится на {num2}\nчастное {num1//num2}')
if num1%num2 >0:
    print(f'{num1} не делится на {num2} нацело\nнеполное частное {num1//num2}\nостаток деления {num1%num2}')
    
# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.17> python 2.py
# введите число: 15
# введите второе число: 5
# 15 делится на 5
# частное 3

# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.17> python 2.py
# введите число: 10
# введите второе число: 3
# 10 не делится на 3 нацело
# неполное частное 3
# остаток деления 1