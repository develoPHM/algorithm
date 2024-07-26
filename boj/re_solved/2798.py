N, M = map(int,input().split())
li = list(map(int,input().split()))
sum = 0
# 전체를 돌며 m이하 + 이전 sum보다 큰 값으로 최대값 찾음
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        for k in range(j + 1, len(li)):
            if sum < li[i] + li[j] + li[k] <= M:
                sum = li[i] + li[j] + li[k]
print(sum)
# 시간 복잡도 앤삼승