
ALL_Price = 0
N_Ticket = int(input('Введите цифрами кол-во билетов: '))
Price = [0, 990, 1390]
Age = []
for x in range(1, N_Ticket + 1):
    Age = int(input(f"Введите возраст {x} посетителя: "))
    if Age < 18:
        ALL_Price += Price[0]
    if 18 <= Age < 25:
        ALL_Price += Price[1]
    if Age > 25:
        ALL_Price += Price[2]
if N_Ticket > 3:
    ALL_Price = ALL_Price * 0.9
    print("С учетом скидки 10% сумма заказа равна - ", ALL_Price, "руб.")
else:
    print("Сумма заказа равна - ", ALL_Price, "руб.")





