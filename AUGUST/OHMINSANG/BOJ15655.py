"""
백준 15655
n, m 입력 --> n은 브렌치 수, m은 레벨
n개의 수 입력(리스트 입력받음)
n개의 자연수에서 m개를 고른 수열
근데 오름차순임. 즉 조합을 출력해야함. 순열 코드에서 조건 추가해서 구현
path, used 사용
"""

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
path = [0] * m
used = [0] * n


def C(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for j in range(n):                                      # 브렌치 수 만큼 loop
        if used[j] == 1: continue                           # 중복순열로 출력되지 않게 하기 위해 used 사용
        if lv > 0 and path[lv - 1] > lst[j]: continue      # path 리스트가 오름차순으로 입력받아야 해서 조건문 추가
        used[j] = 1
        path[lv] = lst[j]
        C(lv + 1)
        used[j] = 0


C(0)
