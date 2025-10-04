# Зчитування трьох чисел
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

# Вивід вхідних даних
print("\nВхідні дані:")
print(a)
print(b)
print(c)

# Визначення максимуму, мінімуму та середнього числа
max_num = max(a, b, c)
min_num = min(a, b, c)
mid_num = a + b + c - max_num - min_num  # середнє число через суму

# Вивід вихідних даних
print("\nВихідні дані:")
print(max_num)
print(min_num)
print(mid_num)