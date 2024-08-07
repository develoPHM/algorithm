from itertools import combinations
N = int(input())
com = list(range(1,N + 1))
cnt = 0
for i in combinations(com,2):
    cnt += 1
print(2 * cnt)