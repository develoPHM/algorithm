import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}
for _ in range(N):
    word = input().strip()
    if word in dic:
        dic[word] += 1
        continue
    if len(word) >= M:
        dic[word] = 1
li = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# -x[1] 빈도 x[0] 단어 len 단어길이
for c in li:
    print(c[0])