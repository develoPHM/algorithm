N = int(input())
for i in reversed(range(N)):
    print(' ' * i + '*' * (N - i))