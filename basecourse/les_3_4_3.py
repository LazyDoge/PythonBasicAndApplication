with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\dataset_3363_4 (1).txt") as inf:
    split = [x.strip() for x in inf.readlines()]
    summM, summF, summL, quan = 0, 0, 0, 0
    for line in split:
        line_split = line.split(";")
        print((float(line_split[1]) + float(line_split[2]) + float(line_split[3]))/3)
        quan += 1
        summM += float(line_split[1])
        summF += float(line_split[2])
        summL += float(line_split[3])
    print(summM/quan, summF/quan, summL/quan)
    # d = {}
    # for word in split:
    #     lower = word.lower()
    #     d[lower] = 1 if lower not in d else d[lower] + 1
    # print(d)
    # maxKey = max(d, key=d.get)
    # maxValue = max(d.values())
    # print(maxKey, maxValue)
    # res = sorted([x for x in split if x.lower() == maxKey])
    # print(res)