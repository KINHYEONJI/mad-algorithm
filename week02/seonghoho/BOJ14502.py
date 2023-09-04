'''
0의 인덱스를 zero에 저장
zero에서 3개 뽑아서 1로 바꾸기
그 때 bfs 돌려서 2가 인접하지 않은 부분이 최대가 되는 인덱스를 뽑기
'''
from collections import deque
import sys

def bfs(y, x):
    global used, Flag
    q = deque()
    q.append([y, x])
    dry = [0, 0, -1, 1]
    drx = [-1, 1, 0, 0]
    used[y][x] = 1
    Flag = True
    cnt = 1
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if 0 <= dy < N and 0 <= dx < M:
                if lst[dy][dx] == 2:  # 주변에 바이러스 있으면 Flag false
                    Flag = False
                if used[dy][dx] == 1: continue  # 이미 지나온 길은 continue
                if lst[dy][dx] == 1: continue  # 벽일 때 continue
                used[dy][dx] = 1  # 사용 체크
                cnt += 1    # 0의 갯수 구하는 문제라서 while 안에서 count
                q.append([dy, dx])

    if Flag:    # 2에 인접하지 않으면 cnt 리턴
        res = cnt
        return res
    else:       # 2에 인접하면 0 리턴
        return 0


N, M = map(int, sys.stdin.readline().split())  # 세로 N, 가로 M
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
zero = []

for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:  # 0인 곳의 인덱스를 zero 리스트에 저장
            zero.append([i, j])

zz = len(zero)
Max = -21e8

for i in range(zz - 2):     # 0인 곳 세 개씩 뽑아서 1로 바꾸고 bfs 실행
    for j in range(i + 1, zz - 1):
        for k in range(j + 1, zz):
            safe = 0
            lst[zero[i][0]][zero[i][1]], lst[zero[j][0]][zero[j][1]], lst[zero[k][0]][zero[k][1]] = 1, 1, 1
            used = [[0] * M for _ in range(N)]
            for m in range(N):
                for n in range(M):  # 사용된 위치는 안돌아도 되니 continue 처리
                    if used[m][n] == 1: continue
                    if lst[m][n] == 0:
                        safe += bfs(m, n)
            if Max < safe:
                Max = safe
            lst[zero[i][0]][zero[i][1]], lst[zero[j][0]][zero[j][1]], lst[zero[k][0]][zero[k][1]] = 0, 0, 0
            #1로 바꾼 곳 다시 0으로 바꾸고 for문 반복 실행
print(Max)
