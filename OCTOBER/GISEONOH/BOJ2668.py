# N=int(input())
# import copy
# import sys
# input = sys.stdin.readline
# cnt=0

# visit_lst=[0]*(N+1)
# visit_lst[0]=1
# path_1=[] # 인덱스 넣기
# path_2=[] # 리스트 안에 값 넣기
# cnt=0
# rs_lst=[]

# def dfs():
#     global path_1, path_2,visit_lst,cnt,lst,rs_lst

#     if len(path_2)>0 and set(path_1)==set(path_2):
#         if cnt<len(path_1):
#             cnt=len(path_1)
#             rs_lst=copy.deepcopy(path_1)


#     for i in range(len(lst)):
#         if visit_lst[lst[i][0]]==0:
#             visit_lst[lst[i][0]]=1
#             path_1.append(lst[i][0])
#             path_2.append(lst[i][1])
#             dfs()
#             path_1.pop()
#             path_2.pop()
#             visit_lst[lst[i][0]]=0




# lst=[]
# lst_e=[]
# for i in range(1, N+1):
#     x=int(input())
#     if i==x:
#         lst_e.append(x)
#         visit_lst[i]=1
#         continue
#     lst.append([i,x])



# dfs()
# rs_lst.extend(lst_e)
# rs_lst.sort()


# print(len(rs_lst))
# for i in range(len(rs_lst)):
#     print(rs_lst[i])
# 실패코드 백트래킹 실패
# 인접리스트로 받고 사이클 찾아서 구현


import sys
input = sys.stdin.readline

n = int(input())
link = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(1,n+1):
    link[int(input())].append(i)

ans = set()
def dfs(v,stack):
    for i in link[v]:
        if visited[i]:
            while stack: # 사이클에 해당하는 모든 정점을 답에 넣음
                a = stack.pop()
                ans.add(a)
                if i == a:
                    break
            return
        
        visited[i] = 1
        dfs(i,stack+[i])
        visited[i] = 0
            
for i in range(1,n+1):
    dfs(i,[])
ans = sorted(list(ans))
print(len(ans),*ans,sep='\n')


