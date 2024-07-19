a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())
ans = 1
for n in range(n0,101):
    fn = a1 * n + a0
    gn = c * n
    if not fn <= gn:
        ans = 0
        break
print(ans)
