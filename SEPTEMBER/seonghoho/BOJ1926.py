from collections import deque


def bfs(y, x):
    q = deque()
    q.append([y, x])
    dry = [0, 0, -1, 1]  # 다이렉트 배열로 탐색
    drx = [-1, 1, 0, 0]
    g_cnt = 1  # 처음 시작하는 곳 갯수 세고 시작
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if 0 <= dy < N and 0 <= dx < M:  # 범위 체크
                if lst[dy][dx] == 0: continue  # 1인 곳만 들어가기
                if used[dy][dx] == 1: continue  # 사용 안한 곳만 들어가기
                used[dy][dx] = 1  # 사용한 곳 체크
                g_cnt += 1  # 갯수 세기
                q.append([dy, dx])
    ret = g_cnt  # 갯수 리턴
    return ret


N, M = map(int, input().split())  # N,M 받기
lst = [list(map(int, input().split())) for _ in range(N)]  # NxM 도화지 받기
used = [[0] * M for _ in range(N)]  # 이미 갯수 센 곳 체크하기 위한 used 배열
cnt = 0  # 그림의 갯수를 셀 cnt
Max = -21e8  # 그림 넓이의 최댓값을 위한 Max
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:  # lst에 1이 있는 곳을 시작점으로 세기 시작
            if used[i][j] == 0:  # 사용안했다면 세기 시작
                used[i][j] = 1  # 시작점으로 돌아가지 못하게 시작점 사용 체크
                num = bfs(i, j)  # bfs 실행
                cnt += 1  # 실행한 횟수 체크
                if Max < num:  # 섬의 크기의 최댓값 뽑기
                    Max = num
if cnt:
    print(cnt)
    print(Max)
else:  # 섬이 없다면 Max값 0 출력, 사실 Max 초기값을 0으로 두고 조건 안걸어도 된다.
    print(cnt)
    print(0)
