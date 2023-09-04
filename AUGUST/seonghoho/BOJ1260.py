from collections import deque # bfs를 위한 deque

def bfs(v):                   # bfs 기본 구조 생성
  q = deque()
  q.append(v)       
  visit_lst[v] = 1            # 사용했던 곳에 1 문자 입력
  while q:
    v = q.popleft()           
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_lst[i] == 0 and lst[v][i] == 1:
        q.append(i)
        visit_lst[i] = 1

def dfs(v):                   # dfs 기본 배열 설명
  visit_lst2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_lst2[i] == 0 and lst[v][i] == 1:
      dfs(i)          

n, m, v = map(int, input().split())

lst = [[0] * (n + 1) for _ in range(n + 1)] # nxn 크기 문자열 생성
visit_lst = [0] * (n + 1)     # n+1 개 0이 들어간 배열 생성
visit_lst2 = [0] * (n + 1)    # n+1 개 0이 들어간 배열 생성

for _ in range(m):
  a, b = map(int, input().split())
  lst[a][b] = lst[b][a] = 1

dfs(v)
print()
bfs(v)