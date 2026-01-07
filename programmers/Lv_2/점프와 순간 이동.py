# k칸 점프 건전지 - k, 온 거리 x2 순간이동
# 반대로 6번째 칸에서 0으로 간다고 생각하면 쉬움
n = 6
ans = 0
while n > 0:
    if n % 2 != 0:
       ans += 1
       n -= 1
    n = n // 2
print(ans)