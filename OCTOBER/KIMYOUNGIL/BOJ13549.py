from collections import deque
n,k = map(int,input().split())
visited = [0]*100001

def bfs():
    q = deque()
    q.append([n,0])
    while q:
        p,c = q.popleft()
        if p == k:
            print(c)
            return

        x = p
        while 0 < 2*x <= 100000:
            if 2*x == k:
                return print(c)
            
            if visited[2*x] == 0:
                visited[2*x] = 1
                q.append([2*x,c])
            x *= 2

        if 0 <= p+1 <= 100000:
            if visited[p+1] == 0:
                visited[p+1] = 1
                q.append([p+1,c+1])

        if 0 <= p-1 <= 100000:
            if visited[p-1] == 0:
                visited[p-1] = 1
                q.append([p-1,c+1])
bfs()