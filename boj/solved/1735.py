import math

a, b = map(int, input().split())
aa, bb = map(int, input().split())
down = math.lcm(b, bb)
up1, up2 = a * down // b, aa * down // bb
up = up1 + up2
g = math.gcd(up,down)
up, down = up//g, down//g
print(up, down)