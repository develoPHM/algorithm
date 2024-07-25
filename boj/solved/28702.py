def fb(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 != 0 and i % 5 != 0:
        return int(i)
    elif i % 3 == 0 and i % 5 != 0:
        return 'Fizz'
    elif i % 3 != 0 and i % 5 == 0:
        return 'Buzz'
    else:
        return 'FizzBuzz'

a = input()
b = input()
c = input()

if a.isdigit():
    print(fb(int(a) + 3))
    exit(0)
elif b.isdigit():
    print(fb(int(b) + 2))
    exit(0)
else:
    print(fb(int(c) + 1))
