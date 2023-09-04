from collections import deque

def bfs(toma):
    global lst, used    # 함수 안에서 값 변경 되는 리스트 global 처리
    q = deque(toma)     # deque에 바로 toma 넣어서 한번에 추가
    drh = [1, -1, 0, 0, 0, 0]   # 상, 하, 왼, 오, 위, 아래 direct 배열 생성
    dry = [0, 0, 0, 0, -1, 1]
    drx = [0, 0, -1, 1, 0, 0]

    while q:
        nowh, nowy, nowx, cnt = q.popleft() # 하나씩 꺼내 쓰기
        for i in range(6):
            dh = nowh + drh[i]
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if 0 <= dh < H and 0 <= dy < N and 0 <= dx < M: # 범위 체크
                if lst[dh][dy][dx] == 0:    # 0인 곳 이라면
                    lst[dh][dy][dx] = 1     # 1로 바꾸기
                    q.append([dh,dy,dx, cnt+1])
    ret = cnt   # cnt값 리턴
    return ret

M, N, H = map(int, input().split())  # 가로 M, 세로 N, 높이 H
lst = [[list(map(int, input().split())) for _ in range(N)] for Q in range(H)]   # 3차원 배열 lst 생성
toma = []   # 처음 토마토가 들어있는 곳의 인덱스를 저장할 리스트

for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 1:   # 토마토가 존재한다면
                toma.append([i, j, k, 0])   # toma 리스트에 넣기, 네 번째에 cnt 추가

if toma:    # 처음에 익은 토마토가 없어서 배열이 비어 있을 때를 위한 예외 처리
    res = bfs(toma)
else:       # 비어 있으면 0 출력
    res = 0
Flag = True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 0:   # 0이 있으면 Flag false
                Flag= False

if Flag:    # 0이 없으면 출력
    print(res)
else:       # 0 있으면 -1 출력
    print(-1)