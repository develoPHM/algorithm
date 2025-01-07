s = 'cdcd'
arr = []
for c in s:
    if len(arr) == 0:
        arr.append(c)
        continue
    if arr[-1] == c:
        arr.pop()
        continue
    arr.append(c)
