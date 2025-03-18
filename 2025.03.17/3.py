year = int(input('введите год: '))

if year%4==0 and year//100>0 or year%400==0:
    print('yes')
else:
    print('no')
    
# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.17> python 3.py
# введите год: 2024
# yes

# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.17> python 3.py
# введите год: 2023
# no