from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
danji = [[0] * n for _ in range(n)]

diry = [-1, 0, 1, 0]
dirx = [0, 1, 0, -1]
c = 1


def bfs(a, b):
    global c
    q = deque()
    q.append([a, b])
    danji[a][b] = c
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        arr[y][x] = 0
        for i in range(4):
            dy = y + diry[i]
            dx = x + dirx[i]
            if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1: continue
            if arr[dy][dx] == 1 and danji[dy][dx] == 0:
                danji[dy][dx] += c
                q.append([dy, dx])
    c += 1
    lst.append(cnt)


lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i, j)
lst.sort()

print(c - 1)
print(*lst, sep='\n')