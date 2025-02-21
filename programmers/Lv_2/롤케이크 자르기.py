def solution(topping):
    answer = 0
    A = {}
    B = {}
    for c in topping:
        if c in A:
            A[c] += 1
        else:
            A[c] = 1
    for c in topping:
        if len(A) == len(B):
            answer += 1
        if c not in B:
            B[c] = 1
        A[c] -= 1
        if A[c] == 0:
            del A[c]

    return answer
