import sys

input = sys.stdin.readline


def dfs(x, cnt):
    global used

    if cnt == 4:
        print(1)
        exit()  # 프로그램 전체 종료

    for i in arr[x]:
        if used[i] == 1: continue
        used[i] = 1
        dfs(i, cnt + 1)
        used[i] = 0


n, m = map(int, input().split())
arr = [[] for _ in range(n)]
used = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 5명의 친구가 연결고리로 이어져있는 경우가 있는지 탐색.
# 즉, 정점 V를 골라 DFS를 진행했을 때 깊이가 4인 경우가 있는지 확인.
for i in range(n):
    used[i] = 1
    dfs(i, 0)
    used[i] = 0

print(0)
