n = int(input())  # 노드 수
k = int(input())  # 간선 수
arr = [[] for _ in range(n + 1)]
used = [0] * (n + 1)    # 인덱스로 0을 포함할 예정이므로 리스트의 크기를 1 늘려서 생성

for i in range(k):
    a, b = map(int, input().split())
    arr[a].append(b)         # 양방향 연결
    arr[b].append(a)

cnt = 0
def dfs(now):
    global cnt
    used[now] = 1       # 방문한 곳은 1로 바꾸기

    for i in arr[now]:
        if used[i] == 0:      # 아직 방문하지 않은 곳
            dfs(i)
            cnt += 1

dfs(1)      # 시작인덱스 1번
print(cnt)
