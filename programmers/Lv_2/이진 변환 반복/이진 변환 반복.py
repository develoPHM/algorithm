def solution(s):
    i, c = 0, 0
    while len(s) != 1 :
        s_len = sum([1 for i in s if i == "1"])
        c += len(s) - s_len
        s = str(bin(s_len)[2:])
        i += 1
    return [i, c]
