import sys
from collections import deque

input = sys.stdin.readline


# 몇 번째(lev) 만에 모든 회원을 순회하는 지 출력
def bfs(x):
    q = deque()
    q.append([x, 0])
    used = [0] * (n + 1)
    used[x] = 1
    while q:
        xx, lev = q.popleft()

        for i in arr[xx]:
            if used[i] == 1: continue
            used[i] = 1
            q.append([i, lev + 1])

        if 0 not in used[1:]:
            return lev


n = int(input())
arr = [[] for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1: break
    arr[a].append(b)
    arr[b].append(a)

ret = []
for i in range(1, n + 1):
    ret.append(bfs(i))

minn = min(ret)
cnt = 0
ans = []
for idx, k in enumerate(ret, start=1):
    if k == minn:
        cnt += 1
        ans.append(idx)

print(minn + 1, cnt)  # 회장 점수: 최소 lev+ 1
print(*ans)