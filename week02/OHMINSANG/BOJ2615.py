import sys

sys.stdin = open('input.txt', 'r')


def bfs():
    for x in range(19):
        for y in range(19):
            if arr[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1
                    while 0 <= nx < 19 and 0 <= ny < 19 and arr[x][y] == arr[nx][ny]:
                        cnt += 1
                        if cnt == 5:
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and arr[nx][ny] == arr[nx + dx[i]][ny + dy[i]]:
                                break
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and arr[x][y] == arr[x - dx[i]][y - dy[i]]:
                                break
                            return arr[x][y], x + 1, y + 1
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1


arr = [list(map(int, input().split())) for i in range(19)]
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]
flag, x, y = bfs()
if not flag:
    print(flag)
else:
    print(flag)
    print(x, y)
