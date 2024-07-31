N, M = map(int,input().split())
li = []
d = {}
ans = []
cnt = 0
for _ in range(N):
    li.append(input())
for _ in range(M):
    d[input()] = 1
for c in li:
    if c in d:
        ans.append(c)
        cnt += 1
print(cnt)
for c in sorted(ans):
    print(c)