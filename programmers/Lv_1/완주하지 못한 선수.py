def solution(participant, completion):
    dic = {}
    for c in participant:
        if c not in dic:
            dic[c] = 0
        dic[c] += 1
    for c in completion:
        dic[c] -= 1
    for key, value in dic.items():
        if value == 1:
            return key