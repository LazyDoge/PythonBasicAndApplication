with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\dataset_24465_4.txt") as inf, open(
        "C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\out_s_2_4_1.txt", "w") as ouf:
    ouf.write("\n".join([x.strip() for x in inf.readlines()][::-1]))
