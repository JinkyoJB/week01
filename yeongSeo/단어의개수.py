import sys

given = sys.stdin.readline()

count = 0
for i in given.strip():
    if i == " ":
        count += 1

if count == 0 and given.strip() != "":
    print(1)
elif count == 0 and given.strip() == "":
    print(0)
else:
    print(count+1)

