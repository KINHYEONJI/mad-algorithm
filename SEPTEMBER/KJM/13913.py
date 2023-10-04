from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(visited[v])
            ans = []
            # path에 저장된 경로 값을 통해 거슬러올라가면서 ans에 저장
            while v != n:
                ans.append(v)
                v = path[v]
            ans.append(n)
            ans.reverse()  # 역순으로 저장되어 있으므로 순서를 바꿈
            print(' '.join(map(str, ans)))
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not visited[next_step]:
                visited[next_step] = visited[v] + 1
                q.append(next_step)
                path[next_step] = v  # 최종 경로 출력 시 next_step 값을 통해 이전 위치를 알아낼 수 있도록 저장함

n, k = map(int, input().split())
MAX = 100001
visited = [0] * MAX
path = [0] * MAX
bfs()