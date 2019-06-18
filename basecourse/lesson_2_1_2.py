a, b = int(input()), int(input())
res = a * b
minimum = a
if b < a:
    minimum = b
d = 2
while d <= minimum:
    if a % d == 0 and b % d == 0:
        res /= d
        a /= d
        b /= d
    else:
        d += 1
print(int(res))



a = int(input())
b = int(input())
d = a
while d%b:
    d += a
print(d)