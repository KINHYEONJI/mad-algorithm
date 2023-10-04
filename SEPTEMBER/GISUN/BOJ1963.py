import math
end=int(math.sqrt(10000))
used=[0]*10001                              #에라토스테네스의 체

for i in range(2,end+1):                    #2부터 end까지 확인
    if used[i]==1:continue                  #범위 안에 소수의 배수를 제거
    for j in range(2*i,10001,i):            #i보다 큰수 부터 배수 제거 편의상 2아이부터시작
        used[j]=1

from collections import deque
def bfs():                                  #간선의 비용이 1인 경우 최단거리 bfs 사용 추천
    global visited,m
    while q:
        x,cnt=q.popleft()
        if x==m:                            #x의 값이 해당하는 값이 나오면 함수 끝
            return print(cnt)
        
        for i in range(4):                  #4자리수
            for j in range(10):             #10개 변경
                new_x=list(str(x))
                new_x[i]=str(j)
                a=''.join(new_x)
                if int(a)>=1000 and used[int(a)]==0 and visited[int(a)]==0:     #세자리수이고 소수이고 방문하지 않은 경우
                    visited[int(a)]=1
                    q.append([int(a),cnt+1])                                    #q에 담아 cnt로 분류해준다
    return -1


T=int(input())
for tc in range(T):
    n,m=map(int,input().split())
    visited=[0]*10000               #매번 배열 새로 만들어주기
    q=deque()
    q.append([n,0])
    ret=bfs()
    if ret==-1:
        print('Impossible')

##4자리수 소수 리스트구하기
#dfs 접근 실패
# 모든 간선의 비용이 1인 그래프에서 최단거리를 구하는 문제는 BFS로 풀어요.

# import math
# end=int(math.sqrt(10000))
# lst_decimal=[]
# check=[0]*10001

# for i in range(2,end):
#     if check[i]==1:continue
#     for j in range(2*i,10001,i):
#         check[j]=1
# for i in range(1000,10001):
#     if check[i]==0:
#         lst_decimal.append(i)


# def threeck(x,y):
#     x=str(x)
#     y=str(y)
#     cnt=0
#     for i in range(4):
#         if x[i]==y[i]:
#             cnt+=1
    
#     if cnt==3:
#         return 1
#     else:
#         return 0



# def dfs(x,target,cnt):
#     global min


#     if x==target:
#         if min>cnt:
#             min=cnt
#         return

#     if cnt>=min:
#         return

    
#     for i in range(len(lst_decimal)):
#         if used[lst_decimal[i]]==1:continue
#         if threeck(lst_decimal[i],x)==1:
#             used[lst_decimal[i]]=1
#             x=lst_decimal[i]
#             dfs(x,target,cnt+1)
#             used[lst_decimal[i]]=0



# T=int(input())
# for tc in range(T):
#     num_1,num_2=map(int,input().split())
#     used=[0]*10001
#     min=30
#     used[num_1]=1
#     dfs(num_1,num_2,0)
#     if min==21e8:
#         print('Impossible')
#     else:
#         print(min)
