a = 2
b = 1
n = 20
plus = 0
cnt = 0
while n >= a:
    plus = n % a
    n = (n // a) * b
    cnt += n
    n = n + plus
print(cnt)