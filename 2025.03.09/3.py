x = input('введите любое время в минутах:')
hour = int(x) // 60
min = int(x) % 60

print(f'{x} минут - это {hour} часов {min} минут')

C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.09> python 3.py
введите любое время в минутах:856
856 минут - это 14 часов 16 минут