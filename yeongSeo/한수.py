import sys

n = sys.stdin.readline()

count = 0

if int(n) >= 100:
    count += 99

    for i in range(100, int(n)+1):
        hundred = i // 100
        ten     = (i // 10) % 10
        one     = i % 10

        if hundred - ten == ten - one:
            count += 1

else:
    count = int(n)

print(count)