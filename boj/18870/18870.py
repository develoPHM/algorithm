N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
nums_dict = {}
point = 0
for c in sorted_nums:
    if c in nums_dict:
        continue
    nums_dict[c] = point
    point += 1
for c in nums:
    print(nums_dict[c], end=' ')