from collections import deque

N = int(input())
lst = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt1 = 0
cnt2 = 0

directy = [0,0,-1,1]
directx = [1,-1,0,0]

def bfs(y, x):
    # bfs로 앞으로 이동할 좌표와 전에 있던 좌표의 값이 같으면
    # deq에 추가
    deq = deque()
    deq.append((y,x))
    while deq:
        now = deq.popleft()
        new_y, new_x = now
        
        for i in range(4):
            dy = new_y + directy[i]
            dx = new_x + directx[i]
            if dx>N-1 or dx<0 or dy>N-1 or dy<0 : continue
            if visited[dy][dx] == 1: continue
            if lst[dy][dx] != lst[new_y][new_x]: continue
            visited[dy][dx] = 1
            deq.append((dy,dx))

# 일반인이 보는 색깔의 갯수
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1: continue
        visited[i][j] = 1
        cnt1+=1
        bfs(i, j)

# 적록색약은 green과 red가 같으므로 G를 R로 초기화
for i in range(N):
    for j in range(N):
        if lst[i][j] == 'G':
            lst[i][j] = 'R'

# 적록색약이 보는 색깔의 갯수
# visited를 전부 0으로 초기화
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1: continue
        visited[i][j] = 1
        cnt2 += 1
        bfs(i,j)
print(cnt1, cnt2)