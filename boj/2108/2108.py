import sys

input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
li.sort()
A = sum(li) / N
B = li[len(li) // 2]
print(round(A))  ## 산술평균
print(B)  ## 중앙값

# 최빈값
dict = {}
for c in li:
    if c not in dict:
        dict[c] = 1
    else:
        dict[c] += 1
max_cnt = max(dict.values())
max_arr = []
for key, values in dict.items():
    if values == max_cnt:
        max_arr.append(key)
max_arr.sort()
if len(max_arr) > 1:
    print(max_arr[1])
else:
    print(max_arr[0])

# 범위
print(li[-1] - li[0])
