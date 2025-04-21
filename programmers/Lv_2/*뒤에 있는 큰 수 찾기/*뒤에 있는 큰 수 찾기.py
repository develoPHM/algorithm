numbers = [9, 1, 5, 3, 6, 2]
ans = [-1] * len(numbers)
stack = []

for i in range(len(numbers)):
    while stack and numbers[stack[-1]]  < numbers[i]:
        idx = stack.pop()
        ans[idx] = numbers[i]
    stack.append(i)
