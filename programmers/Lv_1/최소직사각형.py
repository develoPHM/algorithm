def solution(sizes):
    max_r = 0
    max_c = 0
    for c in sizes:
        if c[1] > c[0]:
            c[1], c[0] = c[0], c[1]
        if max_r < c[0]:
            max_r = c[0]
        if max_c < c[1]:
            max_c = c[1]
    return max_r * max_c