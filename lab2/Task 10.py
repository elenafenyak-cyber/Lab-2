# Порожній список для чисел
inputs = []

# Зчитування трьох чисел від користувача
for i in range(3):
    num = input()
    inputs.append(num)

# Вивід вхідних даних
print("Вхідні дані:")
for num in inputs:
    print(num)

# Вивід вихідних даних
print("Вихідні дані:")
for num in inputs:
    result = "".join("*" if int(d) % 2 == 0 else d for d in num)
    print(result)