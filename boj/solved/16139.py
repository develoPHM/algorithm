import sys
input = sys.stdin.readline
word = input()
N = int(input())
alpha = [[0]*26 for _ in range(len(word))]
for _ in range(N):
    s, start, end = input().split()

    for i in range(int(start), int(end) + 1):
        alpha[ord(word[i]) - 97] += 1
    print(alpha[ord(s) - 97])