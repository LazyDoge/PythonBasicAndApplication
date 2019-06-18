import requests


def step_output_text():
    print()
    print()
    print()


path = "https://stepic.org/media/attachments/course67/3.6.3/"

with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\dataset_3378_3.txt") as inf:
    strip = inf.readline().strip()
    path_strip = path + strip
    print(path_strip)
    get = requests.get(strip).text

    step_output_text()
    counter = 1
    while not get.startswith("We"):
        print(counter)
        counter += 1
        get = requests.get(path + get.strip()).text
    step_output_text()
    step_output_text()
    step_output_text()
    print("#####")
    print(get)
    print("#####")
