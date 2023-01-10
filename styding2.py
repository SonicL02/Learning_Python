import numpy as np
num = int(input("введите число"))
if num % 2 ==0:
    print("четное число", num)
else:
    print("нечетное число")
letter = input("напишите букву")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("гласная")
elif letter == "y":
    print("гласная и согласная")
else:
    print("согласная")

mas = [23, 'Hello', True]
print(mas[0])

num = int(input('введите число'))
data = []
while num != 0:
    data.append(num)
    num = int(input())
data.sort()
print(data)


first_name = input("Введите ваше имя:")
last_name = input("Введите вашу фамилию:")
age = input("Введите ваш возраст:")
city = input("Введите город проживания:")

# # Выводим пустую строку
print("")

# # Выводим приветствие, подставляя имя и фамилию пользователя,
# # которые он ввел с клавиатуры
print("Привет,", first_name, last_name, "!")
#
# # Выводим пустую строку
print("")
#
# # Выводим фиксированный текст для удобства просмотра
print("Ваш профиль:")
#
# # Выводим возраст и город, которые указал пользователь
print("Возраст:", age, "лет")
print("Город:", city)

a = -13
b = 7
a = a - b
b = a + b
print(b)

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел

print(sum(list_of_numbers[::3]))

# Напишите программу, которая на вход получает последовательность чисел, а выводит модифицированный список:
#
# Первое и последнее числа последовательности должны поменяться местами.
# В конец списка нужно добавить сумму всех чисел.

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел
list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]
print(list_of_numbers)

print(sum(list_of_numbers))


per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
L = list(per_cent.values())
S = float(input("Введите сумму"))
D = []
for i in L:
    D.append(int((i * S)/100))
print("deposit =", D)
print("Максимальная сумма, которую вы можете заработать -", max(D))


def is_leap_year(x):
    return (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))

# Дано n-значное целое число N. Определите, входят ли в него цифры 3 и 7

N = (input("Введите число"))
print("3" and "7" in str(N))

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'}

def check_user(username, password):
    if username in user_database:
        return True
    if password in user_database:
        return True
    else:
        return False
print(check_user(username='user', password='password'))
#
# Запишите условие, которое является истинным, /t
# когда только одно из чисел А, В и С меньше 45.
A = int(input("a: "))
B = int(input("b: "))
C = int(input("c: "))
if A < 45 and B >= 45 and C >= 45:
    print(True)
elif A >= 45 and B < 45 and C >= 45:
    print(True)
elif A >= 45 and B >= 45 and C < 45:
    print(True)
else:
    print(False)

# Проверка деления на 5
A = int(input("a: "))
if A % 5 == 0:
    print("Делиться на 5")
else:
    print("Не делиться на 5")

S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

P = 1
N = 5
for i in range(1, N + 1):
    P = P*i
print(P)

n = 10
for lesenka in range(1, n +1):
    print("*" * lesenka)


random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берем каждую сроку
    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
    max_index = 0
    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
    max_value = row[max_index]  # для максимального значения тоже самое
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)

list_ = [-5, 2, 4, 8, 12, -7, 5]
for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
    print("Индекс элемента: ", i)
    print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")


list_ = [-5, 2, 4, 8, 12, -7, 5]
for i, value in enumerate(list_):
    print("Индекс элемента: ", i)
    print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")


# если число четное, то разделить его пополам,
# если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
n = int(input("Введите число\n"))
def check_h(n):
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3 + 1) // 2

        if n == 1:
            return True
            break


# Проверка числа по заданным условиям
a = int(input("Введите число: "))
if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
    print("Число удовлетворяет условиям")
else:
    print('Error')


# Таблица умножения 10 * 10
M = [[i*j for j in range(1, 11)] for i in range(1, 11)]
for i in M:
    print (i)














