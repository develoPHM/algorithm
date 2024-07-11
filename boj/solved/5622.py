S = input() # '0A'
num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
second = 0
for c in range(len(S)):
    if c == '1':
        second += 2
    elif c == '0':
        second += 11
    else:
        cnt = 3
        for d in range(len(num)):
            if S[c] in num[d]:
                second += cnt
            cnt += 1

print(second)