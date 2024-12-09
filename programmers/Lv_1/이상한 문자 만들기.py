def solution(s):
    arr = []
    for c in s.split(' '):
        word = ''
        for i in range(len(c)):
            if i % 2 == 0:
                word += c[i].upper()
            else:
                word += c[i].lower()
        arr.append(word)
    return ' '.join(arr)