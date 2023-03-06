a = int(input())
b = int(input())

c = list(str(b))

for i in range(len(c),0,-1):
    print(a * int(c[i-1]))

print(a * b)


# str은 list 안붙여도 됨!!