"""Определить, является ли год, который ввел пользователь, високосным или не високосным. """

year = int(input('Type the number (year): '))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('Leap year')
else:
    print('Non - leap year')
