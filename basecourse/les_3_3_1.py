import re

# with open(os.path.join(".", "files", "dataset_3363_2.txt")) as inf:
with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\dataset_3363_21.txt") as inf, open(
        "C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\out_3_3_1.txt", "w") as ouf:
    line = inf.readline()
    line = line.strip()
    print(line)
    one = re.split("\d+", line)
    two = re.split("[a-zA-z]", line)
    two.remove("")
    one.remove("")

    s = ""
    # print(len(one))
    # print(one)
    # print(len(two))
    for i in range(len(one)):
        s += one[i] * int(two[i])
    ouf.write(s)
