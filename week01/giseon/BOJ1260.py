from collections import deque



N, M, V=map(int,input().split()) #N은 노드개수 M은 간선개수 V시작 정점
lst=[[] for i in range(N+1)]  #노드개수만큼 리스트를 만들어주기
lst_r=[i for i in range(1,N)]
used=[0]*(N+1) #노드 기준으로 작성되니 N만큼 작성해준다

for i in range(M):

    s,e=map(int,input().split())

    lst[s].append(e) #양방향이니깐 반대로도 받아준다
    lst[e].append(s)

for i in range(1,M):
    lst[i].sort()

def dfs(now):

    print(now,end=' ')
    

    for i in lst[now]:

        if used[i]==1:continue
        used[i]=1
        dfs(i)


def BFS(now):
    q=deque()

    q.append(now)

    while q:
        now=q.popleft()
        print(now,end=' ')

        for i in lst[now]:
            if used[i]==1:continue
            used[i]=1
            q.append(i)
        


used[V]=1
dfs(V)
print()
used=[0]*(N+1) 
used[V]=1
BFS(V)