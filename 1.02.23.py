# n = int(input())
# max_digit = 0
# flag = False
# while n != 0:
#     digit = n % 10
#     if digit == 0:
#         flag = True
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if flag == True:
#     print(0)
# elif max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)


# n = int(input())
# max_digit = -1
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# while n != 0:
#     for i in range(1, n + 1):
#         print(i, i, i, i, i)
#     break

# n=int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         c = i + j
#         print(f'{i} + {j} = {c}')
#     print()

#  программ, которая печатает равнобедренный звездный треугольник с основанием, равным n
# n = int(input())
# for i in range(1, n + 1):
#     if i < n//2 + 1:
#         print("*" * i)
#     if i == n//2 + 1:
#         print("*" * i)
#     if i > (n//2 +1):
#         while i != n + 1:
#             print("*" * (n + 1 - i))
#             break
# n = int(input())
# for i in range(1, n + 1):
#     print('*' * min(i, n - i + 1))

# a = int(input())
# for i in range(1, a + 1):
#     for f in range(1, i + 1):
#         print(i, end="")
#     print()

# n = int(input())
# s = 0
# t = 0
# for i in range(1, n + 1):
#     s += 1
#     for j in range(1, s + 1):
#         t +=1
#         print(t, end=" ")
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for f in range(1, i + 1):
#         print(f, sep="", end="")
#     for j in range(i - 1, 0, -1):
#         print(j, sep="", end="")
#     print()

# a, b = int(input()), int(input())
# counter = 0
# s = 0
# for i in range(a, b + 1):
#     co = 0
#     for j in range(1, i + 1):
#         if i%j == 0:
#             co += j
#             if co >= counter:
#                 s = i
#                 counter = co
#
# print(s, counter)

# n = int(input())
# for i in range(1, n + 1):
#     x = 0
#     for j in range(1, i + 1):
#         if i%j == 0:
#             x += 1
#     print(i, "+"*x, sep="")

# n = int(input())
#
# sum = 0
# for i in range(1, n + 1):
#     s = 1
#     for j in range(1, i + 1):
#         s *=j
#     sum += s
# print(sum)

a, b = int(input()), int(input())
s = 0
for i in range(a, b + 1):
    s = 0
    for f in range(2, i + 1):
        if i%f == 0:
            s += 1
    if s == 1:
        print(i)











