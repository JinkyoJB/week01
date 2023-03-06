import sys
n = int(sys.stdin.readline())
outputs = [];

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        outputs.append(f"{from_pos} {to_pos}")
        return 1

    s1 = hanoi(n-1, from_pos, aux_pos, to_pos) 
    outputs.append(f"{from_pos} {to_pos}")
    s2 = hanoi(n-1, aux_pos, to_pos, from_pos)
    return s1 + s2 + 1

print(hanoi(n, 1, 3, 2))
for output in outputs:
    print(output)

# print(f"{n}번째 원반을 {from_pos}에서 {to_pos}로 이동")



