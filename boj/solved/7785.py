N = int(input())
dict = {}
for _ in range(N):
    name, check = input().split()
    if name not in dict:
        dict[name] = 0
    if check == 'enter':
        dict[name] += 1
    else:
        dict[name] -= 1
people = []
for key,value in dict.items():
    if value == 1:
        people.append(key)
people.sort(reverse=True)
for c in people:
    print(c)