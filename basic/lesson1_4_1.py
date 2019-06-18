# put your python code here
namespaces = {'global': 'None'}
variables = {'global': []}


def get_namespace(namespace, variable):
    if namespace == "None":
        return "None"
    elif variable in variables[namespace]:
        return namespace
    else:
        return get_namespace(namespaces[namespace], variable)


number = int(input())

# print(number)

for x in range(number):
    cmd, arg1, arg2 = input().split()
    if cmd == "create":
        namespaces[arg1] = arg2
        variables[arg1] = []
    elif cmd == "add":
        variables[arg1].append(arg2)
    elif cmd == "get":
        print(get_namespace(arg1, arg2))

# print(data)
