import sys
input = sys.stdin.readline
N, C = map(int, input().split())
li = list(int(input()) for _ in range(N))
li.sort()
start, end = 1, li[-1] - li[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1  # 공유기 설치 수 (첫 번째 집에는 무조건 설치)
    cur = li[0]  # 첫 번째 집에 공유기 설치

    for i in range(1, len(li)):
        if li[i] >= cur + mid:
            cnt += 1
            cur = li[i]

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)