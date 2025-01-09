n, s = map(int, input().strip().split())
li = list(map(int, input().strip().split()))
l, r = 0, 0
length = 1e9
check = li[0]

while l <= r:
    if check >= s:
        length = min(length, r - l + 1)
        check -= li[l]
        l += 1
    else:
        r += 1
        if r < n:
            check += li[r]
        else:
            break

if length == 1e9:
    print(0)
else:
    print(length)