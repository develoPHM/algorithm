N, M = map(int,input().split())
li = []
d = {}
ans = []
count = 0
for _ in range(N):
    li.append(input())
for _ in range(M):
    d[input()] = 1
for c in li:
    if c in d:
        ans.append(c)
        count += 1
print(count)
for c in sorted(ans):
    print(c)