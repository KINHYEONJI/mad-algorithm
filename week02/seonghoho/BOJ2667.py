# bfs 사용해서 푸는 문제

from collections import deque                           # bfs를 위한 deque import 받기

def bfs(y, x):                                          # 주어진 배열에서 1인 곳의 좌표 입력
    global visited                                      # 방문했는지 체크하기 위한 global 처리
    q = deque()                                         # q를 deque 자료형으로 생성
    q.append([y, x])                                    # 해당 좌표를 0번째 자리에 추가
    dry = [0, 0, -1, 1]                                 # 조건에 맞는 상하좌우로 이동할 예정이라 direct 좌표 생성
    drx = [-1, 1, 0, 0]
    size = 0                                            # 아파트 동 갯수 지정

    while q:                                            # q 배열에 자료가 존재한다면 실행
        y, x = q.popleft()                              # q의 맨 처음에 있는 [y,x] pop해서 y,x에 입력
        size += 1                                       # 아파트 동 갯수 +1
        for i in range(4):                              # 상하좌우 갈 수 있나 보기
            dy = y + dry[i]
            dx = x + drx[i]
                                                        # 인덱스를 벗어나면 건너띄기
            if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1: continue
            if visited[dy][dx] == 1: continue           # 이미 방문했으면 건너띄기
            if lst[dy][dx] == 0: continue               # 아파트 동이 존재하지 않으면 건너띄기
            visited[dy][dx] = 1                         # 조건에 통과한 좌표 방문표시하기
            q.append([dy,dx])                           # 조건에 통과한 좌표 q에 넣고 반복
    return size                                         # 아파트 동 갯수 리턴


n = int(input())                                        # NxN 배열의 크기 정하기 위한 n 입력
lst = [list(map(int, input())) for _ in range(n)]       # NxN 배열 생성
visited = [[0] * n for _ in range(n)]                   # NxN 배열과 같은 크기의 방문 배열 생성
islands = []                                            # 얻어진 아파트 단지의 크기 입력할 island  
cnt = 0                                                 # 아파트 단지가 몇 개 인지 입력할 cnt
for i in range(n):                                      # for 문 사용해서 1이고, 방문하지 않은 좌표를 찾아 bfs돌리기
    for j in range(n):
        if lst[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1                           # 조건에 해당하는 좌표에 방문표시하기 
            cnt+= 1                                     # 아파트 단지 갯수 올리기
            islands.append(bfs(i, j))                   # bfs의 return값을 island 리스트에 넣기

islands.sort()                                          # 오름차순으로 정렬

print(cnt)                                              # 아파트 단지 갯수 출력
for i in islands:               
    print(i)                                            # 아파트 크기를 오름차순으로 출력
