"""
백준 15649. N과 M
n,m  주어졌을 때 1부터 n까지 자연수중에서 중복없이 m개 고르는 수열
순열 출력
"""

n, m = map(int, input().split())
lst = []
for i in range(1, n + 1):
    lst.append(i)
path = [0] * m
used = [0] * n


def P(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for j in range(len(lst)):        # range를 n으로 해도 되지만 좀 더 명시적으로 표현하기 위해 len(lst) 사용
        if used[j] == 1: continue    # 중복순열로 출력되지 않게 하기 위해 used 사용
        path[lv] = lst[j]
        used[j] = 1
        P(lv + 1)
        used[j] = 0


P(0)
