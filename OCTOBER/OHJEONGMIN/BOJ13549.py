from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global m
    while q:
        x,level = q.popleft()
        if x==m:
            result.append(level)
        for i in (2*x,x-1,1+x):
            if 0<=i<=100000:
                if i==2*x and used[i]==0:
                    used[i]=1
                    q.append([i,level])
                    # if i==m:
                    #     used[i]=0
                elif (i==1+x or i==x-1) and used[i]==0:
                    used[i]=1
                    q.append([i,level+1])
                    # if i==m:
                    #     used[i]=0

used = [0]*100001
result=[]
q = deque()
n,m = map(int,input().split())

q.append([n,0])
used[n]=1
bfs()
print(min(result))
