def f(x):
    return x * 2


n = int(input())
nums = [int(input()) for _ in range(n)]
d = {}
for num in nums:
    if num not in d:
        d[num] = f(num)
    print(d[num])



'''
a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])

'''



