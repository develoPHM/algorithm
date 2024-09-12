import sys
sys.setrecursionlimit(10**6)

def cal(A, B, C):
    if B == 0:
        return 1
    half = cal(A, B // 2, C)
    half = (half * half) % C
    if B % 2 == 1:
        half = (half * A) % C
    return half

A, B, C = map(int, input().split())
result = cal(A, B, C)
print(result)
