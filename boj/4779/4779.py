import sys

input = sys.stdin.readline


def cut(line):
    if len(line) == 1:
        return line
    a = cut(line[0:len(line) // 3])
    return a + ' ' * (len(line) // 3) + a


while True:
    try:
        N = int(input())
        start = '-' * (3 ** N)
        print(cut(start))
    except:
        break
