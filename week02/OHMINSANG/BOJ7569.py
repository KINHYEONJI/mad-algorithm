from collections import deque

col, row, layer = map(int, input().split())
multi_arr = []
used = []

# 3차원 배열 입력 및 3차원 used 배열 생성
for i in range(layer):
    multi_arr.append([list(map(int, input().split())) for _ in range(row)])
    used.append([[0] * col for _ in range(row)])

dz = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]

# 배열에서 1이 등장 할 때마다 큐에 좌표값 입력
q = deque()
for k in range(layer):
    for i in range(row):
        for j in range(col):
            if multi_arr[k][i][j] == 1:
                q.append([k, i, j])

Max = 0
while q:
    zz, xx, yy = q.popleft()
    for i in range(6):
        ny = yy + dy[i]
        nx = xx + dx[i]
        nz = zz + dz[i]

        if 0 <= nx < row and 0 <= ny < col and 0 <= nz < layer:
            Max = max(multi_arr[nz][nx][ny], multi_arr[zz][xx][yy],
                      Max)  # 초기 Max 설정. 모든 배열이 가득 차있어서 아래 코드가 실행 안될 수 있기 때문에 해당 코드 삽입
            if multi_arr[nz][nx][ny] != 0: continue  # 배열 값이 0이 아니면 패스
            if used[nz][nx][ny] == 0:  # used가 0이면 아래 코드 실행
                multi_arr[nz][nx][ny] += multi_arr[zz][xx][yy] + 1
                used[nz][nx][ny] = 1
                q.append([nz, nx, ny])
            Max = max(multi_arr[nz][nx][ny], multi_arr[zz][xx][yy], Max)  # Max 값 갱신

# bfs후 배열 탐색해서 0이 발견되면 안익은 토마토 존재
flag = 0
for k in range(layer):
    for i in range(row):
        for j in range(col):
            if multi_arr[k][i][j] == 0:
                flag = 1
                break
        if flag: break
    if flag: break

# 안익은 토마토 있으면 -1 출력. 아니면 Max-1 출력. -1 하는 이유는 며칠 걸리는지 구하는 문제라서.
if flag:
    print(-1)
else:
    print(Max - 1)
