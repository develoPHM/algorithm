x, y, w, h = map(int,input().split())
a = min(abs(x - w), x)
b = min(abs(y - h), y)
print(min(a,b))