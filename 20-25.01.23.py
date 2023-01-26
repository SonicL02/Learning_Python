# def print_2_add_2():
#     d = 2 + 2
#     print(d)
# print_2_add_2()

# def hello_world():
#     print("Hello world!")
# hello_world()

# def cheking(n, a):
#     if n % a == 0:
#         print(f"Число {a} является делителем {n}")
#     else:
#         print(f"Число {a} не является делителем {n}")
# cheking(10, 3)

# def lesenka(n):
#     for i in range(n, 0, -1):
#             print("*" * i)
# lesenka(3)

# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))

# def number_divisors(a):
#     cont = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             cont += 1
#     return cont
# number_divisors(4)


# def check_palindrome(str_):
#     str_ = str_.lower()
#     str_ = str_.replace(" ", "")
#
#     if str_ == str_[::-1]:
#         print("Yes")
#         # return True
#     else:
#         print("No")
#         # return False
# check_palindrome("Кит на море не романтик")
#


# x = 3
#
#
# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# func()
# print(x)

# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()

# def mult(*nums):
#     sum = 1
#     for i in nums:
#         sum *= i
#     return sum
# print(mult(1, 2, 3, 4))

# def rec_sum(n):
#    if n == 1:  # терминальный случай
#        return 1
#    return n + rec_sum(n - 1)
# print(rec_sum(6))


# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# print(rec_fibb(7))

# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# print(reverse_str('gfhdj'))
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# print(sum_digit(510))
# print(333%10)

# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)


# Вот универсальный шаблон для декоратора:
#
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrappe

# def counter(func):
#    count = 0
#    def wrapper(*args, **kwargs):
#        nonlocal count
#        func(*args, **kwargs)
#        count += 1
#        print(f"Функция {func} была вызвана {count} раз")
#    return wrapper
#
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")


# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper


# def linear_solve(a, b):
#     return b/a
# print(linear_solve(0,1))

# def disk(a, b, c):
#     D = b**2 - 4*a*c
#     x1 = (-b - D ** 0.5) / (2 * a)
#     x2 = (-b + D ** 0.5) / (2 * a)
#     if D == 0:
#         print(f"уравнение имеет один корень - x = {-b}/(2*{a})")
#     elif D < 0:
#         print(f"уравнение не имеет вещественных корней")
#     else:
#         print(f"равнение имеет два корня: \n x1 = {x1} \n x2 = {x2}")
# disk(3, 55, 34)

# def D(a, b, c):
#     return b ** 2 - 4 * a * c
#
#     def quadratic_solve(a, b, c):
#         if D(a, b, c) < 0:
#             return "Нет вещественных корней"
#         elif D(a, b, c) == 0:
#             return -b/(2*a)
#         else:
#             return (-b - D(a, b, c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
#
# D(4, 3, 2)

# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res * 10 + a % 10)
#
# print(mirror(1234))
#
# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)

# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение

# L = ['THIS', 'IS', 'LOWER', 'STRING']
#
# print(list(map(str.lower, L)))

# l = [-2, -1, 0, 1, -3, 2, -3]
# def fi(x):
#     return x % 2 == 0
#
# r = filter(fi, l)
# print(list(r))

# (вес, рост)
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# print(min(sorted(data, key = lambda x: x[0] / (x[1]/100) ** 2)))

# a = ["asd", "bbd", "ddfa", "mcsa"]
# print(list(map(len, a)))
# print(list(map(str.upper, a)))

# Номер купе

# x = int(input())
# if x%4 == 0:
#     print(int(x/4))
# elif x%4 != 0:
#     print(int(x//4 + 1))

# расчет кол-ва часов и минут

# t = int(input("Введите кол-во минут"))
# a = t//60
# b = t%60
# print(f"{t}  мин - это {a}  час {b}  минут.")


# расчет суммы и произведения цифр 3хзначного числа

# a = int(input())
# x1 = a%10
# x2 = (a//10)%10
# x3 = a//100
# print("Сумма цифр =", x1 + x2 + x3)
# print("Произведение цифр =", x1*x2*x3)

# Переставнока цифр

# x = int(input())
# a = x//100
# b = x//10%10
# c = x%10
#
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# x = int(input())
# a = x//1000
# b = x//100%10
# c = x//10%10
# d = x%10
# print(f"Цифра в позиции тысяч равна {a}")
# print(f"Цифра в позиции сотен равна {b}")
# print(f"Цифра в позиции десятков равна {c}")
# print(f"Цифра в позиции единиц равна {d}")


# сумма a + aa + aaa

# a = input()
# x = a + a
# x1 = a*3
# ai = int(a)
# xi = int(x)
# x1i = int(x1)
# print(ai + xi + x1i)

# проверка совпадения пароля

# password1 = input("Введите пароль: ")
# password2 = input("Повторите пароль: ")
# if password1 == password2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# сумма первой и последней цифр равна разности второй и третьей цифр

# x =  int(input()) #1234
# a = x//1000
# b = x//100%10
# c = x//10%10
# d = x%10
# if a + d == b - c:
#     print("ДА")
# else:
#     print("НЕТ")

# Арифметическая прогрессия

# a, b, c = int(input()), int(input()), int(input())
# if b - a == c - b:
#     print("YES")
# else:
#     print("NO")

# Наименьшее из четырёх чисел

# list_data = [int(value) for value in input().split()]
# print(list_data)
# count = 1000000000000
# for i in list_data:
#     if i <= count:
#         count = i
#
# print(count)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# x = 100000000000
# for i in (a, b, c, d):
#     if i < x:
#         x = i
#
# print(x)

# Возрастная группа

# age = int(input())
# if age <= 13:
#     print("детство")
# elif 14 < age <= 24:
#     print("молодость")
# elif 25 <= age <= 59:
#     print("зрелость")
# else:
#     print("старость")

# сумма положительных цисел

# a, b, c = int(input()), int(input()), int(input())
# count = 0
# for i in (a, b, c):
#     if i >= 0:
#         count += i
#
# print(count)