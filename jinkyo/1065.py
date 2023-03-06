import sys

input=sys.stdin.readline

a = str(input().rstrip())

def classify(a,b,c):
    interval1 = int(b)-int(a)
    interval2 = int(c)-int(b)
    if interval1==interval2:
        return 1
    else:
        return 0

digit_len = len(a)

if digit_len==1 or digit_len==2:
    print(int(a))

elif digit_len==3:
    num=99
    for i in range(100, int(a)+1):
        target = str(i)
        value = classify(target[0],target[1],target[2])
        num += value
    print(num)

elif digit_len==4:
    print(144)
    
else: pass


