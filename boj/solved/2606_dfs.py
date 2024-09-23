V = int(input())
E = int(input())

li = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    li[start].append(end)
    li[end].append(start)

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in li[current]:
        if destination not in visited:
            stack.append(destination)

print(len(visited) - 1)
