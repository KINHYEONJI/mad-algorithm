"""
백준 15652
n,m  주어졌을 때 1부터 n까지 자연수중에서 충복 허용 오름차순 순열
n = 브렌치 수
m = 레벨
중복순열인데 오름차순만
"""
n, m = map(int, input().split())
lst = []
for i in range(1, n + 1):
    lst.append(i)
path = [0] * n


def D_P_up(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for j in range(len(lst)):                               # range를 n으로 해도 되지만 좀 더 명시적으로 표현하기 위해 len(lst) 사용
        if lv > 0 and path[lv - 1] > lst[j]: continue      # path 리스트가 오름차순으로 입력받아야 해서 조건문 추가. 이때 같은 숫자는 중복 허용이기 때문에 등호는 뺌
        path[lv] = lst[j]
        D_P_up(lv + 1)


D_P_up(0)
