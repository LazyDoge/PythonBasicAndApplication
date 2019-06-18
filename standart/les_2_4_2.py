import os
import os.path
result = set()

for curr_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            result.add(curr_dir)

result = list(result)
result.sort()
print("\n".join(result))
