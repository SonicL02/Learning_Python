# число дней в месяце в невисокосном году

x = int(input())
if x in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif x == 2:
    print(28)
else:
    print(30)

#  вес боксера

weight = int(input())

if weight < 60:
    print("Легкий вес")
elif 60 <= weight < 64:
    print("Первый полусредний вес")
elif 64 <= weight < 69:
    print("Полусредний вес")

# Самописный калькулятор

a = int(input())
b = int(input())
operation = input()
x: int = 0
if operation == "+":
    x = a + b
    print(x)
elif operation == "-":
    x = a - b
    print(x)
elif operation == "/":
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        x = a / b
        print(x)
elif operation == "*":
    x = a*b
    print(x)
else:
    print("Неверная операция")

# Цветовой микшер

color1 = input()
color2 = input()

if color1 in ("красный", "синий", "желтый") and color2 in ("красный", "синий", "желтый"):
    if color1 == color2:
        print(color1)
    elif color1 == "красный" and color2 == "синий" or  color2 == "красный" and color1 == "синий":
        print("фиолетовый")
    elif color1 == "красный" and color2 == "желтый" or color2 == "красный" and color1 == "желтый":
        print("оранжевый")
    elif color1 == "синий" and color2 == "желтый" or color2 == "синий" and color1 == "желтый":
        print("зеленый")
else:
    print("ошибка цвета")

# Цвета колеса рулетки

a = int(input())

if 0 <= a <= 36:
    if a == 0:
        print("зеленый")
    elif 1 <= a <= 10:
        if a%2 == 0:
            print("черный")
        else:
            print("красный")
    elif 11 <= a <= 18:
        if a%2 == 0:
            print("красный")
        else:
            print("черный")
    elif 19 <= a <= 28:
        if a%2 ==0:
            print("черный")
        else:
            print("красный")
    elif 29 <= a <= 36:
        if a%2 == 0:
            print("красный")
        else:
            print("черный")
else:
    print("ошибка ввода")


# Пересечение отрезков

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# пустые множества
if b1 < a2 or b2 < a1:
    print("Пустое множество")
# частичное или полное пересечение
elif (a1 == a2 and b1 == b2) or (a1 > a2 and b1 < b2):
    print(a1, b1)
elif (a1 == a2 and b1 > b2) or (a2 < a1 < b2 and b1 > b2):
    print(a1, b2)
elif (b1 == b2 and a1 < a2) or (a1 < a2 < b1 and b1 < b2):
    print(a2, b1)
elif a2 < a1 and b2 > b1:
    print(a1, b1)
elif  a2 > a1 and b2 < b1:
    print(a2, b2)
# точки
elif a1 == b2:
    print(a1)
elif b1 == a2:
    print(b1)



