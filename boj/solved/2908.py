A,B = input().split()

def reverse(num):
    re_num = ''
    for i in range(len(num)):
        idx = len(num) - i - 1
        re_num += num[idx]
    return re_num

print(max(int(reverse(A)),int(reverse(B))))
