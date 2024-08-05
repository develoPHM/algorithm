import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    if num == 0:
        nums.pop()
        continue
    nums.append(num)
print(sum(nums))