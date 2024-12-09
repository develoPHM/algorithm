def solution(a, b):
    def gcd(a, b):
        if a % b == 0:
            return b
        elif b == 0:
            return a
        else:
            return gcd(b, a % b)

    def lcm(a, b):
        return a * b // gcd(a, b)

    return [gcd(a, b), lcm(a, b)]
