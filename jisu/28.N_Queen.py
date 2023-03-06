pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put() -> None: 
    for j in range(8):
        for i in range(8):
            # print(f'{pos[i]:2}', end='')
            print('■' if pos[i] == j else '□', end ='')
        print()
    print()


def set(i:int) -> None:
    for j in range(8):
        if (not flag_a[j]
            and flag_b[i+j]
            and flag_c[i-j+7]):                    
            pos[i] = j

            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                # 다음 j로 연결. 모든 j행을 다 돌고난 후 i+1열로 재귀.
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True

set(0)