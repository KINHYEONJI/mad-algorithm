import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dy = [0, 0, 0, 1, -1]
dx = [0, 1, -1, 0, 0]
rotate = {1: [3, 4], 2: [3, 4], 3: [1, 2], 4: [1, 2]}

col, row = map(int, input().split())
# arr 외곽을 1 로 둘러 쌓아줘서 arr의 좌표값과 문제의 좌표값을 일치시킨다.
arr = [[1] * (row + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(col)] + [
    [1] * (row + 2)]
sy, sx, st = map(int, input().split())
ey, ex, et = map(int, input().split())
cnt = 0
used = [[[0] * 5 for _ in range(row + 1)] for _ in range(col + 1)]
used[sy][sx][st] = 1

q = deque()
q.append([sy, sx, st, cnt])

while q:
    y, x, tilt, cnt = q.popleft()
    if y == ey and x == ex and tilt == et:
        print(cnt)
        break

    # 움직이고 큐에 넣기
    for k in range(1, 4):
        ny = y + (dy[tilt] * k)
        nx = x + (dx[tilt] * k)
        if 1 <= ny <= col and 1 <= nx <= row:
            if arr[ny][nx] == 1: break  # 벽에 부딪칠 때 방향전환해서 움직일 수 없으므로 continue가 아니라 break 를 건다.
            if used[ny][nx][tilt] == 0:
                used[ny][nx][tilt] = 1
                q.append([ny, nx, tilt, cnt + 1])

    # 머리 돌린 뒤 큐에 넣기
    for next_head in rotate[tilt]:
        if used[y][x][next_head] == 0:
            used[y][x][next_head] = 1
            q.append([y, x, next_head, cnt + 1])



# import sys
# from collections import deque
# def input():
#     return sys.stdin.readline().rstrip()
#
#
# dx = [0, 1, -1, 0, 0]
# dy = [0, 0, 0, 1, -1]
# rotate = {1:[3,4], 2:[3,4], 3:[1,2], 4:[1,2]}
#
# col, row = map(int, input().split())
# arr = [[1] * (row + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(col)] + [
#     [1] * (row + 2)]
#
# used = [[[False] * 5 for _ in range(row + 2)] for _ in range(col + 2)]
# sy, sx, st = map(int, input().split())
# ey, ex, et = map(int, input().split())
# used[sy][sx] = 1
# q = deque()
# q.append((sy, sx, st))
#
# while q:
#     y, x, tilt = q.popleft()
#     if y == ey and x == ex: break
#     for i in range(1, 5):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 1 <= ny <= col and 1 <= nx <= row:
#             if used[ny][nx] == 1: continue
#             used[ny][nx] = 1
#             if i == tilt:
#                 arr[ny][nx] = arr[y][x]
#                 q.append((ny, nx, i))
#             elif ((((i == 1) or (i == 2)) and (tilt == 1 or tilt == 2)) or
#                   (((i == 3) or (i == 4)) and (tilt == 3 or tilt == 4))):
#                 arr[ny][nx] = arr[y][x] + 3
#                 q.append((ny, nx, i))
#             else:
#                 arr[ny][nx] = arr[y][x] + 2
#                 q.append((ny, nx, i))
#
# if tilt == et:
#     print(arr[y][x])
# elif ((((et == 1) or (et == 2)) and (tilt == 1 or tilt == 2)) or
#       (((et == 3) or (et == 4)) and (tilt == 3 or tilt == 4))):
#     print(arr[y][x] + 2)
# else:
#     print(arr[y][x] + 1)
#
# for lst in arr:
#     print(*lst)
