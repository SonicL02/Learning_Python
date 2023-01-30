# n = int(input())
# counter = []
# for i in range(n):
#     num = int(input())
#     counter.append(num)
#
# print(max(counter))
# l = counter.pop(counter.index(max(counter)))
# print(max(counter)
# a = [2, 2, 3, -15, 2, -7, -12, 2, 3]
# print(a.pop(a.index(max(a))), a.pop(a.index(max(a))))


# Последовательность Фибоначчи
# n = int(input())
# f = 0 # пред пред
# f2 = 1 # пред
# aa = [1]
# for i in range(n -1):
#     x = f + f2
#     f = f2
#     f2 = x
#     aa.append(x)
# print(*aa)

# a = int(input())
# counter = 0
# if a >= 25:
#     while a >= 25:
#         counter +=  1
#         a = a - 25
# if a < 25:
#     while a >=10 :
#         a = a -10
#         counter +=1
# if a < 10:
#     while a >=5:
#         a = a -5
#         counter += 1
# if a < 5:
#     while a != 0:
#         a = a - 1
#         counter += 1
# print(counter)

# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа

# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# num = int(input())
# summ = 0
# counter = 0
# proiz = 1
# sr = 0
# first = 0
# end = num%10
#
# while num != 0:
#     last = int(num%10)
#     counter += 1
#     summ += last
#     proiz *= last
#     sr += last
#     num = num // 10
#     if last <= 9:
#         first = last
# print(summ, counter, proiz, sr/counter, first, first + end, sep="\n")

# n = int(input())
# nl = n//10
# c = 0
# while n != 0:
#     if n%10 == nl%10:
#         n = n//10
#         c += 0
#     else:
#         print("NO")
#         break
# if c == 0:
#     print("YES")

# n = int(input())
# s = 0
# while n > 9:
#     if n%10 < n//10%10:
#         s = 0
#         n = n //10
#     else:
#         s = s + 1
#         print("NO")
#         break
# if s == 0:
#     print("YES")

# n = int(input())
# for i in range(1, n + 1):
#     if 5 < i <= 9 or 17 < i <= 37 or 78 < i <= 87:
#         continue
#     print(i)