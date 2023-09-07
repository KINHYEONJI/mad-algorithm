from collections import deque
import sys


def bfs():
    global minn
    q = deque()
    q.append([n, 0])

    used = [0] * 100001

    while q:
        x, cnt = q.popleft()
        used[x] = 1

        if x == k:
            minn = min(minn, cnt)

        if 0 <= x + 1 <= 100000 and used[x + 1] == 0:
            q.append([x + 1, cnt + 1])
        if 0 <= x - 1 <= 100000 and used[x - 1] == 0:
            q.append([x - 1, cnt + 1])
        if 0 <= 2 * x <= 100000 and used[2 * x] == 0:
            q.append([2 * x, cnt])


n, k = map(int, input().split())
minn = sys.maxsize
bfs()
print(minn)