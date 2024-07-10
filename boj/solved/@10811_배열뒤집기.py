# N, M = map(int,input().split())
# bucket = list(range(1,N + 1))
# for _ in range(0,M):
#     i, j = map(int,input().split())
#     re = reversed(bucket[i-1:j]) # 뒤집어 줄 리스트의 요소를 슬라이싱 해서 새로운 변수 re에 초기화 시킨다.
#     bucket[i - 1:j] = re # 뒤집어질 리스트의 요소를 슬라이싱해서 초기화 해놓은 re로 값을 변경
# print(*bucket)
#
def custom_reverse(sub_list: list[int]):
    li = []
    for i in range(len(sub_list)):
        idx = len(sub_list) - i - 1
        li.append(sub_list[idx])
    return li


N, M = map(int, input().split())
# N, M = 5, 4

bucket = list(range(1, N + 1))


for _ in range(M):
    a, b = map(int,input().split())
    # 뒤집힌 리스트.
    rev = custom_reverse(bucket[a - 1 : b])
    # 얘를 써서 기존 버킷의 원소들을 변경해야함
    for i in range(len(rev)):
        bucket[a - 1 + i] = rev[i]

for b in bucket:
    print(b, end=' ')



# # print(bucket)
# li = [0,1,2,3,4,5]
# li2 = []
# i, j = 1, 4
# for i in range(len(li)):
#     li2.append(li[len(li)-1-i])
# print(li2)
