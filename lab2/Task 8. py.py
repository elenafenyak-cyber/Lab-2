# зчитування всіх чисел (для двох пар у прикладі)
numbers = [float(input()) for _ in range(8)]  # 8 чисел → 2 пари

# обробка пар по 4 числа
for i in range(0, len(numbers), 4):
    x1, y1, x2, y2 = numbers[i:i+4]
    distance_A2 = x1**2 + y1**2
    distance_B2 = x2**2 + y2**2

    if distance_A2 > distance_B2:
        print("A → точка A далі від початку координат")
    elif distance_B2 > distance_A2:
        print("B → точка B далі від початку координат")
    else:
        print("The distance is the same → точки на однаковій відстані від початку координат")