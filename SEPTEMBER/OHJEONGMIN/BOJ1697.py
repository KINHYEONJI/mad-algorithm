from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global num,m,cnt
    while q:
        x = q.popleft()
        if x==m:
            return visited[x]
        for i in (x-1,x+1,x*2):
            if 0<=i<=100000 and visited[i]==0:
                visited[i] = visited[x]+1
                q.append(i)





n,m = map(int,input().split())
visited = [0]*100001
cnt = 1
num=0
q = deque()
q.append(n)
ret = bfs()
print(ret)
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