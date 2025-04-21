from itertools import permutations

def solution(k, stage):
    li = []
    for c in permutations(range(len(stage)), len(stage)):
        temp_k = k
        cnt = 0
        for i in c:
            need_hp, use_hp = stage[i]
            if temp_k >= need_hp:
                cnt += 1
                temp_k -= use_hp
        li.append(cnt)
    return max(li)
