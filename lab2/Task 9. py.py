# Зчитування координат вершин трикутника
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

# Обчислення квадратів довжин сторін
AB2 = (x2 - x1)**2 + (y2 - y1)**2
BC2 = (x3 - x2)**2 + (y3 - y2)**2
AC2 = (x3 - x1)**2 + (y3 - y1)**2

# Перевірка теореми Піфагора
if AB2 + BC2 == AC2 or AB2 + AC2 == BC2 or AC2 + BC2 == AB2:
    print("Yes")
else:
    print("No")