import sys
input = sys.stdin.readline
word = input()
N = int(input())
alpha = [[0] * 26 for i in range(len(word))]

for i in range(len(word)):
    for j in range(26):
        if ord(word[i]) - 97 == j:
            alpha[i][j] = alpha[i - 1][j] + 1  # 한번 나왔으니 누적합 +
        else:
            alpha[i][j] = alpha[i - 1][j]  # 안 나왔으니 누적합

for _ in range(N):
    s, start, end = input().split()
    if int(start) == 0:
        print(alpha[int(end)][ord(s) - 97])
    else:
        print(alpha[int(end)][ord(s) - 97] - alpha[int(start) - 1][ord(s) - 97])
