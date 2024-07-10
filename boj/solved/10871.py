N, X = map(int,input().split())
nums = list(map(int,input().split()))
ans = []
for i in nums:
    if i < X:
        ans.append(i)
print(*ans)