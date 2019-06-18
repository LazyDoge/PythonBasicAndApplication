with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\dataset_3363_31.txt") as inf:
    split = inf.read().split()
    print(split)
    d = {}
    for word in split:
        lower = word.lower()
        d[lower] = 1 if lower not in d else d[lower] + 1
    print(d)
    maxKey = max(d, key=d.get)
    maxValue = max(d.values())
    print(maxKey, maxValue)
    res = sorted([x for x in split if x.lower() == maxKey])
    print(res)