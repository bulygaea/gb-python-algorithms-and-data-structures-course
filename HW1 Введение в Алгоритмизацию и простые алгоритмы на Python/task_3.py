"""Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на
экран любой символ алфавита от 'a' до 'f' включительно. """

from random import randint, random

num_1, num_2 = map(int, input('Type two numbers via whitespace (second bigger than first): ').split())
print(f'Random integer from {num_1} to {num_2} is {randint(num_1, num_2)}')

num_1, num_2 = map(int, input('Type two numbers via whitespace (second bigger than first): ').split())
print(f'Random real number from {num_1} to {num_2} is {random() * (num_2 - num_1) + num_1}')

letter_1, letter_2 = input('Type two letters via whitespace in lowercase (second bigger than first): ').split()
print(f'Random letter from {letter_1} to {letter_2} is {chr(randint(ord(letter_1), ord(letter_2) + 1))}')
