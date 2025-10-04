# Ввід номера квитка
ticket = input("Enter ticket number: ")

# Перевірка коректності вводу
if len(ticket) != 6 or not ticket.isdigit():
    print("Invalid ticket number")

# Обчислення сум перших і останніх трьох цифр
else:
    first_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    last_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    # Перевірка рівності сум
    if first_sum == last_sum:
        print("Happy")
    elif first_sum != last_sum:
        print("Ordinary")
