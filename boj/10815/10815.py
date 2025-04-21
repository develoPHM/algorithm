N = int(input())
N_nums = list(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))
dict = {}
for c in N_nums:
    dict[c] = 1
for c in M_nums:
    if c in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
# O(N)