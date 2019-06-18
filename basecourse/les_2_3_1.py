a, b, c, d = (int(input()) for _ in range(4))
for i in range(a, b):
    print(i, end="\t")
    for j in range(c, d):
        print(j, end="\t")
