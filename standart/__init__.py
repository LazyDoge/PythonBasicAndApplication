def enough(cap, on, wait):
    result = on + wait - cap
    return result if result > 0 else 0


print(enough(10, 5, 5))
print(enough(100, 60, 50))
