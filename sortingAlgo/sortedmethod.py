# link - https://www.programiz.com/python-programming/methods/built-in/sorted
# Sorted() method

list1=[20,0,1,8,9,10]
print(sorted(list1))
print(sorted(list1,reverse=True))

tuple1=((3,8),(2,9),(1,10),(4,7))
def comp(a):
    return a[1]
print(sorted(tuple1,key=comp))

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)

sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)


