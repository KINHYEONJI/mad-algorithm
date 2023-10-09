"""
23 / 09 / 11 알고 스터디
로봇청소기
"""
import sys
def input(): return sys.stdin.readline().rstrip()


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n, m = map(int, input().split())
y, x, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while 1:
    if arr[y][x] == 0:
        cnt += 1
        arr[y][x] = -1

    # 4방향 탐색 후 청소할 곳 있는지 체크
    flag = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 0:
                flag = 1
                break

    # 청소 할 곳 있다면
    if flag == 1:
        h -= 1 # 반시계 회전하는게 고정값으로 바뀌는거라 변수에 -1
        ny = y + dy[h % 4] # 반시계 회전
        nx = x + dx[h % 4] # 반시계 회전
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 0:
                y, x = ny, nx
                continue

    # 청소 할 곳 없으면
    else:
        # 뒤로 움직이는건 대가리 방향 유지한 채 움직이니까 변수에 직접 -2 하지 않음
        ny = y + dy[(h - 2) % 4]  # 뒤로 이동
        nx = x + dx[(h - 2) % 4]  # 뒤로 이동
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] != 1:  # 뒤로 갔을 때 벽이 아니면
                y, x = ny, nx

            # 4방향 청소할 곳 없어서 뒤로 가려고 하는데 뒤에가 벽이면 멈춰야 하는 문제 조건
            else:
                break

print(cnt)