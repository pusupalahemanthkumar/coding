import functools  
  
# ascending order
def mycmp(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
# descending order
def mycmp1(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0
  
print(sorted([1, 2, 4, 2], key=functools.cmp_to_key(mycmp1)))