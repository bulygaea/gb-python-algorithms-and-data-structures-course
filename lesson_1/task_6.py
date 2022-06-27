"""По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
равносторонним. """

side_1, side_2, side_3 = map(int, input('Type three numbers (triangle\'s sides): ').split())
if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2:
    if side_1 == side_2 == side_3:
        print('The triangle is equilateral')
    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
        print('The triangle is isosceles')
    else:
        print('The triangle is versatile')
else:
    print('There is no triangle with such sides')
