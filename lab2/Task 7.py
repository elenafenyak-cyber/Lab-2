# Введення температури
t = float(input("Введіть температуру (°C): "))

# Визначення стану води
if t < 0:
    print("ice")
elif t <= 100:
    print("water")
else:
    print("water vapor")