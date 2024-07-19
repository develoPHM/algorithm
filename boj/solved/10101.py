a = []
for _ in range(3):
    a.append(int(input()))
cnt = 0
total = 0
total += a[0]
for i in range(1, 3): # 1 ~ 2
    total += a[i]
    if a[i] == a[i - 1]:
        cnt += 1
if total == 180 and cnt == 2:
    print('Equilateral')
elif total == 180 and cnt == 1:
    print('Isosceles')
elif total == 180 and cnt == 0:
    print('Scalene')
else:
    print('Error')

a = int(input())
b = int(input())
c = int(input())

total = a + b + c
if total != 180:
    print("Error")
    exit(0)

# 세 각의 합이 무조건 180
if a == b and b == c and a == c:
    print("Equilateral")
    exit(0)

# 세 각의 합이 전부 다 같지는 않다
if a == b or b == c or a == c:
    print("Isosceles")
    exit(0)

print("Scalene")