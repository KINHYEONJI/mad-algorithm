import heapq
import sys
input=sys.stdin.readline
n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x:(x[1],x[2]))
# print(lst)

h_lst=[]

max_1=0
for i in range(0,len(lst)):
    # print(h_lst)
    while h_lst and h_lst[0] <= lst[i][1]:
        heapq.heappop(h_lst)
        # print(h_lst)
    heapq.heappush(h_lst,lst[i][2])
    max_1=max(max_1,len(h_lst))

print(max_1)