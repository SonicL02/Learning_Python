
nn =int(input()[1:])
kod = []
for i in range(nn):
    k = input()
    if '#' in k:
        position = k.index("#")
        k = k[:position].rstrip()
        kod.append(k)
    else:
        kod.append(k.rstrip())
print(*kod, sep="\n")

n = list(map(int, input().split()))
print(*[i**2 for i in list(map(int, input().split())) if i%10 != 4 and i%2 ==0], sep=' ', end="")

a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)
c = 0
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            c +=1

print(a)
print(c)

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)
for i in range(n - 1):
    m = a.index(max(a[0:n - i]))
    a[n - 1- i], a[m] = a[m], a[n - 1 - i]

print(a)

L = list(map(int, input().split()))
s = sum(L)
print(*L, sep="+", end="=")
print(s)


 номер телефона 1

number = list(input())
f = True
if len(number) == 12:
    for i in range(len(number)):
        if number[i] in "0987654321":
            f = True
        elif (i == 3 and number[3] in "-") or (i == 7 and  number[7] in "-"):
            f = True
        else:
            f = False
            break
elif len(number ) == 14 and number[0] in "7":
    for i in range(len(number)):
        if number[i] in "0987654321":
            f = True
        elif (i == 5 and number[5] in "-") or (i == 9 and  number[9] in "-") or (i == 1 and number[1] in "-"):
            f = True
        else:
            f = False
            break
else:
    f = False
if f == True:
    print("YES")
else:
    print("NO")

 номер телефона 2

number = input()
f = True
if len(number) == 12 and number[:3].isdigit() and number[4:7].isdigit() and number[8:].isdigit() and number[3] in "-" and number[7] in "-":
    f = True
elif len(number) == 14 and number[0] in "7" and number[1:10:4] in "---" and number[2:5].isdigit() and number[6:9].isdigit() and number[10::].isdigit():
    f = True
else:
    f = False
print("YES" if f == True else "NO")

самое длинное слово
s = input().split()
lenght = 0
for i in range(len(s)):
    if len(s[i]) > lenght:
        lenght = len(s[i])
print(lenght)

s = list(input().split())
for w in range(len(s)):
    s[w] = s[w][1:] + s[w][0] + "ки"
print(*s)


def draw_triangle(fill, base):
    for i in range(1, base//2 + 1):
        print(fill * i)
    for j in range(base//2 + 1, 0, -1):
        print(fill * j)

fill = input()
base = int(input())
draw_triangle(fill, base)


