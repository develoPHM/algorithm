N = int(input())
def fibo(num):
    if num == 1:
        return 1
    if num == 0:
        return 0

    return fibo(num-1) + fibo(num-2)
print(fibo(N))