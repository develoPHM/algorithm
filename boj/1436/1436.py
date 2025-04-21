N = int(input())
count = 0
ans = 0
for i in range(1,100000000):
    if '666' in str(i):
        count += 1
        ans = i
    if  N == count:
        print(ans)
        break