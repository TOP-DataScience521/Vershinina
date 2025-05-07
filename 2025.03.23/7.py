num = int(input("Введите число: "))
a, b = 1, 1
print (a , b, end=" ")

for n in range(num - 2):
    a, b = b, a+b
    print (b, end=" ")
    
C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.23> python 7.py
Введите число: 5
1 1 2 3 5
C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.23> python 7.py
Введите число: 15
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
