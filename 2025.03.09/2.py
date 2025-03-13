num1 = input()
num2 = int(num1) + 1
num3 = int(num1) - 1

print('Следующее число за числом', num1, 'число:', num2, '\n', 'Для числа', num1, 'предыдущее число:', num3) 


# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.09> python 2.py
# 60
# Следующее число за числом 60 число: 61
 # Для числа 60 предыдущее число: 59
 
 
 # не смогла убрать пробел перед второй строкой вывода, выходила ошибка синтаксиса
    # print('Следующее число за числом', num1, 'число:', num2, '\n', end='', 'Для числа', num1, 'предыдущее число:', num3)
                                                                                                                       # ^
# SyntaxError: positional argument follows keyword argument
