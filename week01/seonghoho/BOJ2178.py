from collections import deque

N, M = map(int, input().split())            # NxM 배열 크기 설정
lst = [list(input()) for _ in range(N)]     # NxM 배열 만들기
used = [[0] * M for _ in range(N)]          # 지나온 곳 체크

def bfs(sty, stx, edy, edx):                # 시작점, 끝점 좌표 입력한 bfs함수
    q = deque()
    q.append([sty, stx, 1])                 # level == 1부터 시작

    while q:
        nowy, nowx, level = q.popleft()
        dry = [0, 0, -1, 1]
        drx = [-1, 1, 0, 0]
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]              # 인덱스 넘으면 패스
            if dy < 0 or dx < 0 or dy > N - 1 or dx > M - 1: continue
            if used[dy][dx] == 1: continue  # 지나온 곳이면 패스
            if lst[dy][dx] == '0': continue # 0으로 된 벽이면 패스

            used[dy][dx] = 1                # 해당 좌표 지나온 곳으로 변경
            q.append((dy, dx, level + 1))   # level+1 으로 몇 번째 실행인지 확인

            if dy == edy and dx == edx:     # 끝 좌표와 일치하면 level + 1 리턴
                return level + 1

used[0][0] = 1                              # 첫 좌표 지나온 곳으로 체크
n = bfs(0, 0, N-1, M-1)
print(n)