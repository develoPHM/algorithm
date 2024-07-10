N, M = map(int,input().split())
bucket = list(range(1,N + 1))
for _ in range(0,M):
    i, j = map(int,input().split())
    re = reversed(bucket[i-1:j]) # 뒤집어 줄 리스트의 요소를 슬라이싱 해서 새로운 변수 re에 초기화 시킨다.
    bucket[i - 1:j] = re # 뒤집어질 리스트의 요소를 슬라이싱해서 초기화 해놓은 re로 값을 변경
print(*bucket)
