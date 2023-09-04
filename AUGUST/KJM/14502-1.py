from collections import deque
import copy

# 메인
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 위치 저장 1
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append([i, j])

# bfs 탐색
diy = [-1, 1, 0, 0]
dix = [0, 0, -1, 1]


def bfs(get_virus):
    # 벽 건설된 arr 백업
    test_arr = copy.deepcopy(arr)
    q = deque(get_virus)

    while q:
        y, x = q.popleft()

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
            if test_arr[dy][dx] == 0:
                test_arr[dy][dx] = 2
                q.append([dy, dx])

    # 바이러스 다 퍼뜨리고 0갯수 세기
    # 그렇게 센 갯수는 안전지대 수 -> 리턴으로 넘기기
    safe = 0
    for i in range(N):
        safe += test_arr[i].count(0)

    return safe


# 벽 3개 세우기
max_v = -21e8


def build(cnt):
    # 벽 3개 지어진 맵으로 탐색
    global max_v
    if cnt == 3:
        max_v = max(max_v, bfs(virus))
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                build(cnt + 1)
                arr[i][j] = 0


build(0)
print(max_v)