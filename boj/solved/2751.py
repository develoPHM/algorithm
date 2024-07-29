import sys
input = sys.stdin.readline

N = int(input())
li = [0] * 2000001
nums = []
for i in range(N):
    nums.append(int(input()))
for i in range(len(nums)):
    li[nums[i] + 1000000] += 1
for i in range(len(li)):
    if li[i] == 1:
        print(i - 1000000)
