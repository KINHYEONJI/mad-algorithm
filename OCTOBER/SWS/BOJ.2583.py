from collections import deque

M, N, K = map(int, input().split())
lst = [list([0] * N) for _ in range(M)]
for i in range(K):
    a, b, c, d = map(int, input().split())
    # 0으로 초기화 된 배열에 사각형 위치에 1넣기
    for j in range(b,d):
        for k in range(a,c):
            lst[j][k] = 1
directy = [0,0,-1,1]
directx = [1,-1,0,0]

# 방문배열
used = [[0]*N for _ in range(M)]

def deq(i,j):
    cnt = 1
    deq = deque()
    deq.append((i,j))
    while deq:
        now = deq.popleft()
        now_y, now_x = now
        for w in range(4):
            dy = now_y + directy[w]
            dx = now_x + directx[w]
            if dx > N-1 or dx < 0 or dy > M-1 or dy < 0: continue
            if used[dy][dx] == 1: continue
            if lst[dy][dx] == 1 : continue  
            used[dy][dx] = 1
            cnt += 1
            deq.append((dy,dx))
    return cnt
new = []
cnt2 = 0
for i in range(M):
    for j in range(N):
        if lst[i][j] == 1: continue
        if used[i][j] == 1: continue
        used[i][j] = 1
        ret = deq(i,j)
        cnt2 += 1
        new.append(ret)
print(cnt2)
new.sort()
for i in new:
    print(i, end = ' ')