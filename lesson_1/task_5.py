"""Пользователь вводит номер буквы в алфавите. Определить, какая это буква. """

num = int(input('Type the number (1-26): '))
print(f'The letter {chr(num + ord("a") - 1)} is in {num} place')
