"""По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти
точки. """

x1, y1 = map(float, input('Type two numbers via whitespace (coordinates): ').split())
x2, y2 = map(float, input('Type two numbers via whitespace (coordinates): ').split())

k = (y1 - y2) / (x1 - x2)
print(
    f'y = {k}x {"+" if y1 - k * x1 > 0 else "-" if y1 - k * x1 < 0 else ""} {abs(y1 - k * x1) if y1 - k * x1 != 0 else ""}')
