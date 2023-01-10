import numpy as np
# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка

list1 = [1, 1, 2, 3, 2, 5]
print(list1)
list1.append(str("Hey"))
print(list1)
list1[2] = 4
print(list1)
list1.append([1, 3, 7])
print(list1)
list1[-1] = (1, 5)
print(list1)
print(list1[1])
list1.remove(5)
print(list1)
print(list1.count(1))

strq = 'Python - это Питон!'
# strq2 = list(strq)
# print(strq2)
# print(len(strq2))
c = 0
for i in strq:
    c = c + 1
print(c)


n = 0
str_1 = 'Python - это Питон!'
while str_1:
    # Сокращаем строку на один символ.
    str_1 = str_1[1:]
    #увеличиваем счетчик на единицу.
    n += 1
print('В строке', n, 'символов.')

l = [1, '2', 3, 4, '5']
l2 = 0
for i in l:
    if type(i) is int:
        l2 += i
    else:
        l2 += int(i)
print(l2)

k = {12, 33, 24, 7, 19}
for i in k:
    if i%2 == 0:
        print(i)

s1 = 'abcde123f'
s2 = 'bad_cat_23'
for i in s1:
    if i in s2:
        print(f'Символ {i} есть в "bad_cat_23"')
    else:
        print(f'Символа {i} нет в "bad_cat_23"')
#
# сумму кубов натуральных чисел от 1 до n включительно
e = int(input("Введите число "))
c = 0
for i in range(1, e + 1):
     c += i**3
print(c)
# факториал числа до 30 вкл
g = int(input("Введите число до 30 включительно: "))
f = 1
for i in range(1, g + 1):
     if g <= 30:
          f *= i
print(f)

