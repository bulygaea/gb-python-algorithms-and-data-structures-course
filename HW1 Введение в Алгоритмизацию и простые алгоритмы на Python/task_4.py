"""Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится
букв. """

letter_1, letter_2 = input('Type two letters via whitespace in lowercase (second bigger than first): ').split()
print(f'The letter {letter_1} is in {ord(letter_1) - ord("a") + 1} place')
print(f'The letter {letter_2} is in {ord(letter_2) - ord("a") + 1} place')
print(f'There are {ord(letter_2) - ord(letter_1) - 1} letter{"s" if ord(letter_2) - ord(letter_1) - 1 != 1 else ""} '
      f'between {letter_1} and {letter_2}')
