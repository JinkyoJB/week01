from typing import MutableSequence
import sys 

input=sys.stdin.readline

num = int(input())
x = [int(input()) for i in range(num)]

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:    # 실습 6-10과 같은 while 문
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(a, left, pr)
    if pl < right:
        qsort(a, pl, right)


def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':

    quick_sort(x)      # 배열 x를 퀵 정렬

    for i in range(num):
        print(x[i])
