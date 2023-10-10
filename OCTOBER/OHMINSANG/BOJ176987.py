"""
23 / 10 / 10 알고 스터디
계란으로 계란치기
다시 풀어보기...
"""
import sys
def input(): return sys.stdin.readline().rstrip()


def DFS(lv):
    global Max

    # 계란 전부 다 사용 했을 때
    if lv == n:
        Sum = 0
        for i in range(n):
            if S_W[i][0] <= 0:  # 깨진거 나올 때마다 +1
                Sum += 1
        Max = max(Max, Sum)
        return

    # 들고 있는 계란이 깨져있으면 다음 계란으로
    if S_W[lv][0] <= 0:
        DFS(lv + 1)
        return

    # 계란 안깨지는거 있는지 체크
    flag = 1
    for i in range(n):
        if i == lv: continue  # 현재 들고 있는 계란은 무시
        if S_W[i][0] > 0:
            flag = 0
            break

    # lv 계란 빼고 싹 다 깨져있으면
    if flag:
        Max = max(Max, n - 1)

    # 계란으로 계란치기. 왼쪽부터. (무게 - 쉴드)가 0 이하면 깨짐
    for i in range(n):
        if i == lv or S_W[i][0] <= 0: continue  # 자기 자신은 제외, 이미 깨진 계란은 제외

        # 서로 데미지 입으니까 둘 다 계산
        S_W[lv][0] -= S_W[i][1]
        S_W[i][0] -= S_W[lv][1]

        DFS(lv + 1)

        # 리턴 될 때는 다시 원상복구
        S_W[lv][0] += S_W[i][1]
        S_W[i][0] += S_W[lv][1]


n = int(input())
S_W = [list(map(int, input().split())) for _ in range(n)]
Max = 0
DFS(0)
print(Max)
