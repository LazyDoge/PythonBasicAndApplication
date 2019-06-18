number1 = int(input())

inheritance = {}

# print(number)

for x in range(number1):
    inputted = input().split(":")
    cn_left = inputted[0]
    if len(inputted) == 1:
        cn_right = []
        inheritance[cn_left.strip()] = cn_right
    else:
        cn_right = inputted[1]
        inheritance[cn_left.strip()] = cn_right.split()
    # print(cn_left)
    # print(cn_right)

number2 = int(input())


def check(a, b):
    if a in inheritance[b]:
        return "Yes"
    else:
        temp = "No"
        for element in inheritance[b]:
            if check(a, element) == "Yes":
                temp = "Yes"
        return temp


for y in range(number2):
    cn_out_left, cn_out_right = input().split()
    if cn_out_right in inheritance:
        if cn_out_right == cn_out_left:
            print("Yes")
        else:
            print(check(cn_out_left, cn_out_right))
    else:
        print("No")


# print(inheritance)


# 15
# G : F
# A
# B : A
# C : A
# D : B C
# E : D
# F : D
# X
# Y : X A
# Z : X
# V : Z Y
# W : V
# Q : P
# Q : R
# Q : S
# 7
# A G
# A Z
# A W
# X W
# X QWE
# A X
# X X
# 1 1
# Q
#
#
#
# Ответы:
#
# Yes
# No
# Yes
# Yes
# No
# No
# Yes
# No
# Yes