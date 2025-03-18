num1 = int(input('введите первое число: ')) 
num2 = int(input('введите второе число: '))
num3 = int(input('введите третье число: '))

if num1>0 and num2>0 and num3>0:
    print(num1+num2+num3)
    
if num1>0 and num2>0 and num3<0:
    print(num1+num2)
    
if num1<0 and num2>0 and num3>0:
    print(num2+num3)
    
if num1>0 and num2<0 and num3>0:
    print(num1+num3)
    
# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.17> python 1.py
# введите первое число: 5
# введите второе число: -6
# введите третье число: 7
# 12

# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.17> python 1.py
# введите первое число: -9
# введите второе число: 5
# введите третье число: 3
# 8

# C:\Users\DTO\Desktop\Курс Data Science\Vershinina\2025.03.17> python 1.py
# введите первое число: 5
# введите второе число: 5
# введите третье число: -5
# 10