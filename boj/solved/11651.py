N = int(input())
li = []
for i in range(N):
    word = input()
    if word in li:
        continue
    li.append(word)

li.sort(key=lambda x: (len(x), x))
for c in li:
    print(c)
