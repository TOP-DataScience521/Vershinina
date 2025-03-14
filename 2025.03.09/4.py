num = int(input('введите любое трехзначное число:'))

num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10

print(f'сумма цифр = {num1+num2+num3}\nпроизведение цифр = {num1*num2*num3}')

C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.09> python 4.py
введите любое трехзначное число:758
сумма цифр = 20
произведение цифр = 280