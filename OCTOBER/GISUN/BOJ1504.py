# 문제 접근 다익스트라 최단거리 구하는 함수 제작 구간마다 구할 예정 result 함수 내부에 제작
# 타겟 1,2 꼭 가야함으로 1>t1>t2>n 2>t1>t2>n 구하여 최소값 프린트
#1

import heapq
n,m=map(int,input().split())
inf=int(21e8)

def dijstra(start,end):
    result=[inf]*(n+1)
    heap_lst=[]
    heapq.heappush(heap_lst,[0,start])                  #값과 위치 넣어주기
    result[start]=0
    while heap_lst:
        ps,w=heapq.heappop(heap_lst)
        if ps>result[w]:continue                       
        for i in arr[w]:
            cost=ps+i[1]                                 
            if cost<result[i[0]]:
                result[i[0]]=cost
                heapq.heappush(heap_lst,[cost,i[0]])    # 경유지까지의 값과 경유지 인덱스 추가
    return result[end]   

    


#인접리스트제작
arr=[[]for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])

target_1,target_2=map(int,input().split())

rs_1=dijstra(1,target_1)+dijstra(target_1,target_2)+dijstra(target_2,n)
rs_2=dijstra(1,target_2)+dijstra(target_2,target_1)+dijstra(target_1,n)
if min(rs_1,rs_2)>21e8:
    print(-1)
else: print(min(rs_1,rs_2))

