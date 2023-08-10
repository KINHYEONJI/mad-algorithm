import sys
sys.stdin = open('week01/KJM/input.txt','r')
'''
인접행렬 만들어서 DFS해보기
1. n대의 컴퓨터니까 n*n만큼 인접행렬 생성
2. 좌표를 입력받고 해당 인접행렬 값 1로 바꾸기
3. 
'''
n = int(input()) # 컴퓨터 대수
matrix = [ [0] * n for _ in range(n) ] # n*n 인접행렬

pairs = int(input()) # 서로 얽혀있는 노드쌍 개수...이게 뭐지?

# 입력 받은 좌표에 있는 값 1로 바꾸기
for _ in range(pairs):
    y,x = map(int,input().split())
    matrix[y-1][x-1] = 1 # 인덱스니까 -1씩 
    matrix[x-1][y-1] = 1 # 인덱스니까 -1씩 

cnt = 0
visited = [0] * n

def dfs(now):
    global cnt
    
    for i in range(n): # 인접행렬 순회
        if matrix[now][i] == 1 and visited[i] == 0: # now 노드행이 지목하고있는 i노드가 있다면
            cnt += 1
            visited[i] = 1 
            dfs(i)   # now 포인터를 그 지목당한 i 노드의 행으로 옮긴다(그 행은 지목당한 i노드가 지목하고 있는 정보가 있다(자식 노드의 정보가 있다)
            
visited[0] = 1
dfs(0)   
print(cnt)