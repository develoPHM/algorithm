s = "aukks"
skip = "wbqd"
index = 5
alpha = 'abcdefghijklmnopqrstuvwxyz'
answer = ''
for c in skip:
    if c in alpha:
        alpha = alpha.replace(c, '')
for i in s:
    change = alpha[(alpha.index(i) + index) % len(alpha)]
    answer += change

print(answer)