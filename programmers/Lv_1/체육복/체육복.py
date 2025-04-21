def solution(n, lost, reserve):
    save = 0
    lost.sort()
    reserve.sort()
    lost_copy = lost[::]

    for c in lost:
        if c in reserve:
            save += 1
            reserve.remove(c)
            lost_copy.remove(c)

    for c in lost_copy:
        if c - 1 in reserve:
            reserve.remove(c - 1)
            save += 1
        elif c + 1 in reserve:
            reserve.remove(c + 1)
            save += 1
    return n - len(lost) + save