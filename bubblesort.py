import random

list = [random.randint(1, 20) for i in range(10)]
print(list)
list2 = [18, 1, 1, 5, 13, 4, 8, 12, 2, 9]
list = [18, 1, 1, 5, 13, 4, 8, 12, 2, 9]
count = 0
c = 0
for i in range(len(list)):
    for j in range(len(list) - i - 1):
        c += 1
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            count += 1
    print(list)
print(list, count, c)