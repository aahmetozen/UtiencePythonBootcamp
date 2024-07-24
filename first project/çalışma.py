"""list = [5, 3, 8, 6, 7, 2]


def artanl(list):
    list = [5, 3, 8, 6, 7, 2]
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                t = list[j]
                list[j] = list[j + 1]
                list[j + 1] = t
    print ("artan şekilde sıralanmış liste: {}".format(list))

artanl(list)"""
numbers=[2,6,4,8,9]
for n in numbers:
    print(n)