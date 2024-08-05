N = int(input())
for _ in range(N):
    GH = input()
    stack = []
    for c in GH:
        if stack and c == ')' and stack[-1] == '(':
            stack.pop()
            continue
        stack.append(c)

    if not stack:
        print('YES')
        continue
    print('NO')