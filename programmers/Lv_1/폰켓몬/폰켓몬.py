def solution(nums):
    dic = {}
    pick = len(nums) // 2
    max_num = 0
    for c in nums:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
        if max_num <= dic[c]:
            max_num = dic[c]
    cnt = 0
    arr = []
    while pick >= 1:
        for c in dic:
            if pick == 0:
                break
            if dic[c] >= 1 and c in arr:
                dic[c] -= 1
                pick -= 1
            elif dic[c] == 0:
                continue
            else:
                arr.append(c)
                dic[c] -= 1
                pick -= 1
    return len(arr)
