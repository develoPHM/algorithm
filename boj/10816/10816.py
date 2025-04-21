N = int(input())
li = list(map(int, input().split()))
card = {}
for c in li:
    if c in card:
        card[c] += 1
    else:
        card[c] = 1
M = int(input())
li2 = list(map(int, input().split()))

for c in li2:
    if c in card:
        print(card[c], end=' ')
    else:
        print(0,end=' ')