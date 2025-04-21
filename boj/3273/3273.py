n = int(input())
li = list(map(int,input().split()))
x = int(input())
li.sort()
ans = 0

l = 0
r = len(li) - 1

while l < r:
    if li[l] + li[r] == x:
        ans += 1
        l += 1
        r -= 1
    if li[l] + li[r] > x:
        r -= 1
        continue
    if li[l] + li[r] < x:
        l += 1
        continue
print(ans)