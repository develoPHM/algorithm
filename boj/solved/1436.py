N = int(input())
cnt = 0
ans = 0
for i in range(1,100000000):
    if '666' in str(i):
        cnt += 1
        ans = i
    if  N == cnt:
        print(ans)
        break