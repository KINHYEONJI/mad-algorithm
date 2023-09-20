import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
start=int(input())

#인접리스트 만들기
arr=[[]for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    arr[a-1].append([b-1,c])

#result 만들기
inf=int(21e8)
result=[inf]*(n)


def dijsktra(start):
    heap_lst=[]
    heapq.heappush(heap_lst,(0,start)) # 인덱스 비용
    result[start]=0

    while heap_lst:
        sk,k=heapq.heappop(heap_lst) #경유지비용,선택경유지
        if result[k]<sk:continue
        for i in arr[k]:
            cost=sk+i[1]                         #인접리스트 1인덱스에 비용들어있음
            if cost<result[i[0]]:               #인접리스트 0인덱스에는 들어가는 위치 들어있고 그걸 리절트에 넣어서 문제푸
                result[i[0]]=cost
                heapq.heappush(heap_lst,(cost,i[0]))

dijsktra(start-1)
for i in range(len(result)):
    if result[i]==21e8:
        print('INF')
    else:
        print(result[i])