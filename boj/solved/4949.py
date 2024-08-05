def check_if_valid(s):
    stack = []
    for c in s:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
            continue
        if stack and stack[-1] == '[' and c == ']':
            stack.pop()
            continue
        stack.append(c)

    if len(stack) == 0:
        return True
    return False

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        exit(0)
    arr = []
    for c in s:
        if c in "()[]":
            arr.append(c)

    if check_if_valid(arr):
        print('yes')
    else:
        print('no')


