import random
list = [random.randint(1, 20) for i in range(10)]
print(list)
list2 = [18, 1, 1, 5, 13, 4, 8, 12, 2, 9]
list = [18, 1, 1, 5, 13, 4, 8, 12, 2, 9]
count = 0
c = 0
for i in range(10):
    for j in range(i+1, 10):
        c += 1
        if list[i] > list[j]:
            list[j], list[i] = list[i], list[j]
            count += 1
        #print(list)
print(list, count, c)
list = [18, 1, 1, 5, 13, 4, 8, 12, 2, 9]
count = 0
c = 0
for i in range(10):
    for j in range(i+1, 10):
        c += 1
        minindex = i
        if list[minindex] > list[j]:
            minindex = j
    list[minindex], list[i] = list[i], list[minindex]
    count += 1
        #print(list)
print(list, count, c)