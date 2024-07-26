M = int(input())
N = int(input())
li = []
for i in range(M, N + 1):
    # 1은 패스
    if i == 1:
        continue
    # 반복문에서 체킹하는 불리언 추가
    check = True
    for j in range(2, i):
        if i % j == 0:
            # 2부터 자기자신 - 1 까지 돌면서 나눠지는 수 있으면 반복문 종료
            check = False
            break
    if check:
        li.append(i)
# print(li)
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])
