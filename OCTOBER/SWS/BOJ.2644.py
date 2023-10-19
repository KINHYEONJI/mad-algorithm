import sys
sys.stdin = open('input.txt')

# 부모 자식간의 관계인 st, ed를 인접리스트로 받는데
# 서로 방향이 정해지지 않았기 때문에 양방향 그래프로 만들어준다
N = int(input())
people1, people2 = map(int, input().split())
m = int(input())
lst = [[] for _ in range(N+1)]
for i in range(m):
    st, ed = map(int, input().split())
    lst[st].append(ed)
    lst[ed].append(st)

# 연결이 없으면 Flag = 0 / 있으면 cnt를 출력
def dfs(people1, cnt):
    global used, Flag
    if people1 == people2:
        Flag = 1
        print(cnt)
        return
    
    for i in lst[people1]:
        if used[i] == 1: continue
        used[i] = 1
        dfs(i, cnt+1)
        used[i] = 0

Flag = 0
used = [0] * (N+1)
cnt = 0
dfs(people1, 0)
if Flag == 0: print(-1)