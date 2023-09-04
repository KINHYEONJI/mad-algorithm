computer = int(input())
couple = int(input())

lst = [[] for _ in range(computer+1)]
for i in range(couple):
    start,end = map(int,input().split())
    lst[start].append(end)  # (1,3) (2,3) 처럼 양방향으로 찾아야 하기 때문에 둘다 append
    lst[end].append(start)

visited = [0]*(computer+1)

def dfs(now):
    visited[now]=1
    for i in lst[now]:
        if visited[i]==0:
            dfs(i)

dfs(1)
print(visited.count(1)-1)       #1을 제외한 컴퓨터의 수 count

