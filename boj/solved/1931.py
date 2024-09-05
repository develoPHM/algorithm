import sys
input = sys.stdin.readline
N = int(input())
cnt = 1
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[1], x[0]))

start = time[0][1]
for i in range(1, len(time)):
    if start <= time[i][0]:
        cnt += 1
        start = time[i][1]
print(cnt)