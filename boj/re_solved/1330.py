A, B = map(int,input().split())
if A == B:
    print('==')
    exit(0)
if A > B:
    print('>')
    exit(0)
if A < B:
    print('<')
    exit(0)

# O(1)