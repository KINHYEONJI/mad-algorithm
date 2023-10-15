'''
각 칸에서 갈 수 있는 최대 길이를 memo에 기록함
각 칸에서 dfs를 돌리는데 이미 memo로 기록되어 있는 곳은 방문하지 않는다1
'''

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
distance = [[0]*n for _ in range(n)]

diy = [-1,1,0,0]
dix = [0,0,-1,1]

def dfs(y,x):
    global max_v

    # 방문했던 적이 있으면 그 값 리턴
    if distance[y][x] != 0:
        return distance[y][x]

    # 이번 dfs 탐색으로 처음 방문하는 경우 길이 1 기록
    distance[y][x] = 1

    for i in range(4):
        dy = y + diy[i]
        dx = x + dix[i]
        if dy<0 or dx<0 or dy>=n or dx>=n: continue

        # 다음 탐색은 지금보다 더 많은 값인 경우만 들어간다
        if arr[dy][dx] > arr[y][x]:
            # distance에는 지금까지 기록 중 더 큰 값을 기록한다
            # 다음 칸으로 탐색했다는건 조건을 만족했다는 뜻
            # 조건을 만족하면서 갔던 칸들을 다시 처음칸으로 회수할건데
            # 갈 때마다 늘어나는게 1이니까
            # 회수할 때 리턴값에 1을 더해서 회수하며 기록한다
            distance[y][x] = max(distance[y][x], dfs(dy,dx)+1)


    return distance[y][x]

max_v = -21e8
for i in range(n):
    for j in range(n):
        if not distance[i][j]: # 한번이라도 방문한 적 없는 칸만 탐색
            max_v = max(max_v, dfs(i,j))

print(max_v)
