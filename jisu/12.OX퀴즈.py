times = int(input());
res = [];

for _ in range(0, times, 1):
    T = list(input())

    cnt = 0

    for i in range(0, len(T), 1):
        j = i;
        while T[j] == 'O' and j >= 0:
            if T[j] == 'O':
                cnt += 1
            j -= 1;

    res.append(cnt)

for i in range(0, times, 1):
    print(res[i])


# 겉으로는 OOXXOXXOOO가 한번에 들어가고 결과도 한 번에 나오는 것 같지만,
# for문 한 번 씩 input이 들어가고, 결과도 한 번 씩 result에 담긴 후 나중에 for문으로 하나씩 출력하게 한 것이다.

# for문 안의 for문은, 이왕이면 다른 문자를 써야 하지만 두 기능이 연관되어있지 않은 경우 같게 써도 됨. 

# list(string): split()은 구분자가 있지만 list()는 걍 다 쪼갬
# list는 메서드 명이므로 변수이름으로 쓰면 안된다. 

# for문은 전체 element를 다 돌게 되어있고, while는 조건이 맞는 동안만 반복한다.  
# 연속된 O를 count 해야하는 경우 
# 조건이 안맞으면 break하는 while이 적합하다.

