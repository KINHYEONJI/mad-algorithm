from collections import deque

N,M = map(int, input().split())

graph = []

for i in range(M):
    graph.append(list(map(int,input())))



dist = [[-1] * N for _ in range(M)]


dxl = [1, -1, 0, 0]
dyl = [0 , 0, 1, -1]

def bfs(a, b):
    q = deque()
    q.append([a,b])
    dist[0][0] = 0

    while q:
        y,x = q.popleft()

        for i in range(4):
            dx = x + dxl[i] #열 이동
            dy = y + dyl[i] #행 이동
            
            if -1<dx<N and -1< dy < M:

                if dist[dy][dx] == -1:

                    if graph[dy][dx] == 0:
                        dist[dy][dx] = dist[y][x]
                        q.appendleft([dy,dx])

                    else:
                        dist[dy][dx] = dist[y][x] +1
                        q.append([dy,dx])



bfs(0,0)
print(dist[M-1][N-1])