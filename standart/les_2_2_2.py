# print(sum([int(input()) for _ in range(int(input()))]))
import simplecrypt

with open("C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\encrypted.bin", "rb") as inf, open(
        "C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\out_s_2_2_2.txt", "w") as ouf, open(
        "C:\\Users\\sky\\PycharmProjects\\stepic_course_512\\files\\passwords.txt") as pas:

    encrypted, passwords = inf.read(), str(pas.read()).splitlines()
    # print(passwords)
    for password in passwords:
        try:
            print(simplecrypt.decrypt(password, encrypted))
        except:
            print("bad password", password)
