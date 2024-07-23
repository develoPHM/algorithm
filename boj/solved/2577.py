a = int(input())
b = int(input())
c = int(input())
num = str(a * b * c)
num_0 = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0
num_9 = 0

for i in num:
    if i == '0':
        num_0 += 1
    elif i == '1':
        num_1 += 1
    elif i == '2':
        num_2 += 1
    elif i == '3':
        num_3 += 1
    elif i == '4':
        num_4 += 1
    elif i == '5':
        num_5 += 1
    elif i == '6':
        num_6 += 1
    elif i == '7':
        num_7 += 1
    elif i == '8':
        num_8 += 1
    elif i == '9':
        num_9 += 1
print(num_0)
print(num_1)
print(num_2)
print(num_3)
print(num_4)
print(num_5)
print(num_6)
print(num_7)
print(num_8)
print(num_9)

