year = int(input('введите год: '))

if year % 4 == 0 and year // 100 > 0 or year % 400 == 0:
    print('yes')
else:
    print('no')


# введите год: 2024
# yes


# введите год: 2023
# no

