"""
백준 15654
n, m 입력 --> n은 브렌치 수, m은 레벨
n개의 수 입력(리스트 입력받음)
n개의 자연수에서 m개를 고른 수열
그냥 순열 출력
path, used 사용
"""

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
path = [0] * m
used = [0] * n


def P(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for j in range(n):                  # 브렌치 수 만큼 loop
        if used[j] == 1: continue       # 중복순열로 출력되지 않게 하기 위해 used 사용
        used[j] = 1
        path[lv] = lst[j]
        P(lv + 1)
        used[j] = 0


P(0)
