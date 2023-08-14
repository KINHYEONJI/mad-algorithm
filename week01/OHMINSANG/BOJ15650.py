"""
백준 15650. N과 M
n,m  주어졌을 때 1부터 n까지 자연수중에서 중복없이 m개 고르는 수열
m --> 레벨
n --> 브렌치 수
오름차순 순열만 출력 --> 조합 출력
"""
n, m = map(int, input().split())
lst = []
for i in range(1, n + 1):
    lst.append(i)
path = [0] * m


def C(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for j in range(len(lst)):                               # range를 n으로 해도 되지만 좀 더 명시적으로 표현하기 위해 len(lst) 사용
        if lv > 0 and path[lv - 1] >= lst[j]: continue      # path 리스트가 오름차순으로 입력받아야 해서 조건문 추가
        path[lv] = lst[j]
        C(lv + 1)


C(0)
