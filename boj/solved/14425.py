N, M = map(int,input().split())
S = set()
count = 0
for _ in range(N):
    S.add(input())
for _ in range(M):
    word = input()
    if word in S:
        count += 1
print(count)