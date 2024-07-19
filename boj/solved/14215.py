a, b, c = map(int, input().split())
total = a + b + c
m = max(a, b, c)

if a == b and b == c and a == c:
    print(total)
    exit(0)
if total - m <= m:
    new_m = total - m - 1
    print(total - m + new_m)
    exit(0)
if total - m > m:
    print(total)
    exit(0)