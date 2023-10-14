# import sys
# sys.stdin = open('woo2zza/SSAFY/Boj/silver/input.txt','r')
# def input(): return sys.stdin.readline().rstrip()   
from collections import deque


N = int(input())
lst = [list(input())  for _ in range(N)]
used = [[0]*N for _ in range(N)]
directy = [0,0,-1,1]
directx = [1,-1,0,0]

def Map(i, j):
    cnt = 1
    deq = deque()
    deq.append((i, j))

    while deq:
        new = deq.popleft()
        sy, sx = new
        for q in range(4):
            dy = sy + directy[q]
            dx = sx + directx[q]
            if dx < 0 or dx > N-1 or dy < 0 or dy > N-1:continue
            if used[dy][dx] == 1: continue
            if lst[dy][dx] == '1':
                used[dy][dx] = 1
                deq.append((dy,dx))
                cnt += 1
    return cnt
cnt2 = 0
result = []
for i in range(N):
    for j in range(N):
        if used[i][j] == 1: continue
        if lst[i][j] == '1':
            used[i][j] = 1
            cnt2 += 1
            ret = Map(i, j)
            result.append(ret)

print(cnt2)
result.sort()
for i in result:
    print(i)

