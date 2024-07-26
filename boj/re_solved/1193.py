N = int(input())
find = 0
cnt = 0
while find < N:
    # 시작하는 숫자
    cnt += 1
    find += cnt
# print(cnt)
# 몇칸 이동해야하는지
move = N - find + cnt - 1
if cnt % 2 == 0:
    print(1 + move, '/', cnt - move, sep='')
else:
    print(cnt - move, '/', 1 + move, sep='')
# 시간 복잡도 O(1)

