N = int(input())
nums = list(map(int,input().split()))
m = max(nums)
average = 0
for c in nums:
    average += (c/m * 100)
print(average / N)