"""
백준 15651
n,m  주어졌을 때 1부터 n까지 자연수중에서 중복허용 m개 고르는 수열
n = 브렌치 수
m = 레벨
중복순열 ㄱㄱ
"""
n, m = map(int, input().split())
lst = []
for i in range(1, n + 1):
    lst.append(i)
path = [0] * m


def D_P(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for j in range(len(lst)):       # range를 n으로 해도 되지만 좀 더 명시적으로 표현하기 위해 len(lst) 사용
        path[lv] = lst[j]
        D_P(lv + 1)


D_P(0)
