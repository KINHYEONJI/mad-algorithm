from collections import deque

N, M, V = map(int, input().split())  # N:노드 수, M:간선 수, V:시작 번호

arr = [[] for _ in range(N + 1)]
used = [0] * (N + 1)

def dfs(now):
    print(now, end=' ')
    used[now] = 1       # 현재 노드 방문 처리

    for i in arr[now]:
        if used[i] == 1: continue   # 이미 방문했으면 pass
        dfs(i)


def bfs(now):
    q = deque()
    q.append(now)
    used[now] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in arr[now]:
            if used[i] == 1: continue
            q.append(i)
            used[i] = 1


for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)            # 양방향 연결
    arr[e].append(s)

for row in arr:         # 오름차순 정렬
    row.sort()

dfs(V)
print()
used = [0] * (N + 1)        # bfs 탐색 전 방문 초기화
bfs(V)
