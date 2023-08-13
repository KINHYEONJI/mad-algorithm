"""
백준 15655
n, m 입력 --> n은 브렌치 수, m은 레벨
n개의 수 입력(리스트 입력받음)
n개의 자연수에서 m개를 고른 수열
중복 가능 --> 중복순열
"""

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
path = [0] * m


def D_P(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for j in range(n):          # 브렌치 수 만큼 loop
        path[lv] = lst[j]
        D_P(lv + 1)


D_P(0)
