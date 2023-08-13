N = int(input())                    # 컴퓨터 갯수
tc = int(input())                   # 연결된 갯수
lst=[[] for _ in range(N+1)]        # 리스트 초기화
visited=[0]*(N+1)                   # 방문했는지

for i in range(tc):                 # 그래프 만들기
    s,e=map(int,input().split())
    lst[s]+=[e]                     #양방향 체크
    lst[e]+=[s]

def dfs(now):
    visited[now] = 1
    for i in lst[now]:
        if visited[i]==0:
            dfs(i)
dfs(1)
print(sum(visited)-1)