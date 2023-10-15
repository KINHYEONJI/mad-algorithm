from collections import deque
import sys

input = sys.stdin.readline
dry = [0, 0, -1, 1]
drx = [-1, 1, 0, 0]


def bfs():
    q = deque()
    # 0,0은 켜져있으니 넣고 시작
    q.append([0, 0])
    on[0][0] = 1
    visited[0][0] = 1
    cnt = 1
    while q:
        ny, nx = q.popleft()
        # 해당 위치의 버튼이 있다면, 킬 수 있는 버튼 num 차례로 꺼내기
        # 만약 꺼져 있다면 키고 cnt+=1
        # 네 방향 중 이미 방문한 곳 이라면 경로 연결 되어 있는 것으로 보고 q에 추가하여 한번 더 탐색한다.
        for num in button[ny][nx]:
            if on[num[0]][num[1]] == 0:
                on[num[0]][num[1]] = 1
                cnt += 1
                for k in range(4):
                    dy = num[0] + dry[k]
                    dx = num[1] + drx[k]
                    if dy < 0 or dy > n - 1 or dx < 0 or dx > n - 1: continue
                    if visited[dy][dx]:
                        q.append([dy, dx])

        # 네 방향 돌아서 켜져있고, 방문 안한 곳이면 q에 넣어 탐색 반복
        for i in range(4):
            dy = ny + dry[i]
            dx = nx + drx[i]
            if dy < 0 or dy > n - 1 or dx < 0 or dx > n - 1: continue
            if on[dy][dx] == 0: continue
            if visited[dy][dx] == 1: continue
            visited[dy][dx] = 1
            q.append([dy, dx])
    # 쌓인 cnt 값 return
    return cnt


n, m = map(int, input().split())
# 2차원 버튼 만들기
button = [[[] for _ in range(n)] for _ in range(n)]
# button 배열의 sy,sx 에 ey,ex 추가하기
for _ in range(m):
    sy, sx, ey, ex = map(int, input().strip().split())
    button[sy-1][sx-1].append([ey-1, ex-1])
# 켜진 위치 체크
on = [[0] * n for _ in range(n)]
# 방문 배열 만들기
visited = [[0] * n for _ in range(n)]

res = bfs()

print(res)
