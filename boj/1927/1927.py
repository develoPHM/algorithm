import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))  # 최소값 출력 후 삭제
        else:
            print(0)
    else:
        heapq.heappush(heap, x)  # 힙에 값 추가