a = input()
li = []
plus_li = []

for c in a.split('-'):
    if '+' in c:
        plus_li = c.split('+')
        plus = 0
        for i in range(len(plus_li)):
            plus += int(plus_li[i])
        li.append(plus)
    else:
        li.append(int(c))

ans = li[0]
if len(li) == 1:
    print(ans)
else:
    for i in range(1,len(li)):
        ans -= li[i]
    print(ans)