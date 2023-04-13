print("Покупка билетов на Онлайн конференцию")
print("_____________\n")
value = int(input("Введите количество приобретаемых билетов: "))
print(f"Количество покупаемых биллетов {value}")
print("_____________\n")
print("Укажите возраст посетителя для каждого билета:")
ticket_age = {}
for i in range(1, value + 1):
    age = int(input(f"Билет №{i} "))
    ticket_age[f"Билет №{i} "] = age
ticket_price = []
for i in list(ticket_age.values()):
    if i < 18:
        ticket_price.append(0)
    elif 18 <= i < 25:
        ticket_price.append(990)
    else:
        ticket_price.append(1390)
print("_____________\n")
print("Стоимость билетов:")
for a, b in zip(list(ticket_age.keys()), ticket_price):
    print(f"{a}- {b}₽")
total_price = sum(ticket_price)
discount = total_price-(total_price/10)
print("_____________\n")
if value <= 3:
    print(f"Общая стоимость билетов {total_price}₽")
    if total_price > 0:
        print("Вы можете получить скиду 10% \nесли регистрируете более 3 билетов.")
else:
    print(f"Общая стоимость билетов {total_price}₽")
    print(f"Стоимость с учетом скидки {discount}₽")
