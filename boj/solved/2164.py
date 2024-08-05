from collections import deque
N = int(input())
card = deque(list(range(1, N + 1)))
if N == 1:
    print(card[0])
    exit(0)
if N == 2:
    print(card[1])
    exit(0)
while len(card) > 3:
    card.popleft()
    card.append(card.popleft())
print(card[1])