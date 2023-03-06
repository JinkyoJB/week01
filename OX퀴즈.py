import sys

n = int(sys.stdin.readline())

answers = []

for i in range(n):
    tmp = sys.stdin.readline()
    answers.append(tmp)

for answer in answers:
    WholeScore = 0
    curScore = 0
    for res in answer:
        if res == "O":
            curScore += 1
            WholeScore += curScore
        else:
            curScore = 0
    print(WholeScore)