per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = (input("Введите сумму вклада: "))
money = round(float(money), 2)
x = ("Сумма вклада округляется до %.2f $" % money)
print(x)
line_1 = int(len(x))
print(line_1*"#", "\n")# Это тут для красоты, просто выводи "#"
bank = list(per_cent.keys())
rate = list(per_cent.values())
for i in rate:
    deposit.append(i*float(money)/100)
deposit = [round(i, 2) for i in deposit] #Функцию округления нашел на просторах интернета
print("Выплаты по вкладу в разных банках:")
for f, o in zip(bank, deposit):
    print(f, o, "$") #Метод zip так же был найден на просторах интернета, без эстетики никуда
print()
print("Максимальная сумма, которую вы можете заработать — ", max(deposit), "$")
