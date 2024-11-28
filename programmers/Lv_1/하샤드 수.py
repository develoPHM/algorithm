def solution(x):
    str_x = str(x)
    a = 0
    for c in str_x:
        a += int(c)
    if x % a == 0:
        return True
    else:
        return False