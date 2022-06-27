"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого). """

num_1, num_2, num_3 = map(int, input('Type three numbers via whitespace: ').split())

if num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
    middle = num_2
elif num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
    middle = num_1
else:
    middle = num_3
print(f'The middle number is {middle}')
