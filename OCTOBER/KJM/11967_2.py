# 딕셔너리를 이용해 실행시간 줄인 버전

import sys
sys.stdin = open('input.txt','r')

'''
#1 bfs로 해당칸에 가서 킬 수 있는 곳에 불을 킨다
#2 갈 수 없었던 곳을 갈 수 있게 되었으니까 예전에 갔던 경로도 다시 갈 수 있게 해줘야한다
#3 아예 방문표시를 안하면 시간초과나고..
'''
from collections import deque,defaultdict

n,m = map(int,input().split())
info = defaultdict(list)
for _ in range(m):
    from_y,from_x,to_y,to_x = map(int,input().split())
    info[(from_y,from_x)].append((to_y,to_x))

arr = [ [0]*(n+1) for _ in range(n+1)] # 0,1 로 구성된 불켜져있는지 확인

diy = [-1,1,0,0]
dix = [0,0,-1,1]

def bfs(sy,sx):
    global cnt

    visit = [[False] * (n+1) for _ in range(n+1)]
    q = deque()
    q.append([sy,sx])
    visit[sy][sx] = True

    while q:
        y,x = q.popleft()

        # 1번 케이스
        # 해당 칸에서 킬 수 있는 다른 칸들의 불을 모두 킨다
        for to_y,to_x in info[(y,x)]:
            # 이미 켰던 곳은 제외한다
            if arr[to_y][to_x] == 0:
                arr[to_y][to_x] = 1
                cnt += 1 # 킨 만큼 갯수증가

                # 불 킨 칸에서 상하좌우를 탐색한다
                # 만약 상하좌우 중 방문했던 곳이 있다면 경로가 연결된 곳이므로
                # 해당 위치에서 다시 탐색할 수 있게끔한다
                for i in range(4):
                    dy = to_y + diy[i]
                    dx = to_x + dix[i]
                    if dy < 1 or dx < 1 or dy >= (n + 1) or dx >= (n + 1): continue
                    if visit[dy][dx]:
                        q.append([dy,dx])


        # 2번 케이스
        # 일반적인 bfs탐색을 돌린다
        for i in range(4):
            dy = y+diy[i]
            dx = x+dix[i]
            if dy<1 or dx<1 or dy>=(n+1) or dx>=(n+1): continue
            if visit[dy][dx]: continue

            # 불이 켜져 있는 곳으로만 이동한다
            if arr[dy][dx] == 1:
                visit[dy][dx] = True
                q.append([dy,dx])


cnt = 1
arr[1][1] = 1
bfs(1,1)

# for a in arr:
#     print(*a)

print(cnt)

