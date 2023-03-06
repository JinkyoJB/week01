import sys

t = int(sys.stdin.readline())

results = []
for i in range(t):
    r, s = sys.stdin.readline().split()
    r = int(r)

    newStr = ""
    for j in s:
        newStr += j*r
    
    results.append(newStr)

for i in results:
    print(i)
