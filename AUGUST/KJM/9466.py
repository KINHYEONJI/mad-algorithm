from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt','r')
def dfs(start,here):

    if visit[here]: # 모든 노드를 다 탐색하고나서 (한번 다 돌고)
        if start == here: #시작과 마지막이 같으면
            return 1 # 싸이클이 있다고 리턴

        # 아니면 싸이클 없다고 판단
        return 0

    visit[here] = True
    for node in graph[here]:
        # 싸이클 정보를 돌아오면서도 유지하기 위해 마지막 리턴이 1이면 1, 0이면 0
        if dfs(start,node):
            return 1
    visit[here] = False
    return 0

T = int(input())

for _ in range(T):
    N = int(input())
    picked = [0]+list(map(int,input().split()))
    graph = defaultdict(list)

    for i in range(1,N+1):
        graph[i].append(picked[i])

    visit = [False] * (N+1)
    made_team = []
    # 이미 방문한 노드를 피하기 위한 메모이제이션

    for i in range(1,N+1):
        # 시작점과 끝점을 자기 자신으로 설정해서
        # 돌아올 수 있으면 싸이클
        # 못 돌아오면 노싸이클
        if dfs(i,i):
            made_team.append(i) # True면 싸이클이라 팀 있으니 따로 저장

    ans = N - len(made_team)
    print(ans)
