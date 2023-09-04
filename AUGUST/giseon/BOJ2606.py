k=int(input())#컴퓨터 대수
k_1=int(input())#연결된 컴퓨터 수
lst=[i for i in range(1,k+1)]#[실제값나타내는리스트]
arr=[[0 for i in range(k)] for i in range(k)] #인접행렬이용해서 해결
used=[0]*k #중간에 사이클에 걸려 무한루프 걸리는걸 방지
for i in range(k_1):
    a,b=map(int,input().split()) #양방향이니깐 양쪽으로 추가
    arr[a-1][b-1]=1
    arr[b-1][a-1] = 1 


rs_lst=[]
def dfs(now):
    # print(used) 경로 확인용 
    rs_lst.append(lst[now])
    for i in range(k):
        if arr[now][i]==1 and used[i]==0:
            used[i]=1 #중간에 사이클을 막기위해 used 사용
            dfs(i)




used[0]=1
dfs(0)
print(len(rs_lst)-1)


