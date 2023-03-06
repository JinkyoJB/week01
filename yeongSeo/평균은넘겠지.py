import sys

c = int(sys.stdin.readline())

classes = []

for i in range(c):
    oneclass = list(map(int, sys.stdin.readline().strip().split()))
    classes.append(oneclass)

for each in classes:
    number = each[0]
    average = int(sum(each[1:]) / number)

    well = 0
    for i in each[1:]:
        if i > average:
            well += 1
    
    ratio = (well / number) * 100
    print("{:.3f}".format(ratio) + "%")



