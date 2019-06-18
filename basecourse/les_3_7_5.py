with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\dataset_3380_52.txt") as inf:
    dda, d = [x.strip().split("\t") for x in inf.readlines()], {str(i): [0, 0] for i in range(1, 12)}
    for da in dda:
        d[da[0]] = [d[da[0]][0] + int(da[2]), d[da[0]][1] + 1]
        # d[da[0]] = [da[2], 1]
        # print(da)
    for k, v in d.items():
        print(k, v[0]/v[1] if v[1] != 0 else "-")
