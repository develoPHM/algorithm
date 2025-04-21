def find(a, b, c, park):
    for i in range(a, a + c):
        for j in range(b, b + c):
            if park[i][j] != "-1":
                return False
    return True

def solution(mats, park):
    row = len(park)
    col = len(park[0])

    for c in mats:
        for i in range(row):
            for j in range(col):
                if i + c <= row and j + c <= col:
                    if find(i, j, c, park):
                        return c
    return -1
mats = [1,2,3]
mats.sort(reverse=True)
print(mats)