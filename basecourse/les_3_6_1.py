import requests

with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\dataset_3378_2.txt") as inf:
    strip = inf.readline().strip()
    get = requests.get(strip)
    print(len(get.text.splitlines()))
