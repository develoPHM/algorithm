N = int(input())
find = 0
count = 0
while find < N:
    # 시작하는 숫자
    count += 1
    find += count
# print(cnt)
# 몇칸 이동해야하는지
move = N - find + count - 1
if count % 2 == 0:
    print(1 + move, '/', count - move, sep='')
else:
    print(count - move, '/', 1 + move, sep='')
# 시간 복잡도 O(1)

