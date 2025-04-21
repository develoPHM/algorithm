from itertools import combinations
N = int(input())
com = list(range(1,N + 1))
count = 0
for i in combinations(com,2):
    count += 1
print(2 * count)