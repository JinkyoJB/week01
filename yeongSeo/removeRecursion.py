"""doit!"""

def recur(n):
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)
recur(3)

print("_________")
def remove_tail(n):
    while n > 0:
        recur(n-1)
        print(n)
        n = n -2
remove_tail(3)
print("_________")


arr = [] #스택으로 활용
def remove_recur(n):
    while True:
        if n > 0:
            arr.append(n)
            n = n -1
            continue
        if len(arr) != 0:
            n = arr.pop()
            print(n)
            n = n -2
            continue

        break


remove_recur(3)
        

        

    