import sys
import heapq
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    p,d = map(int,input().split())
    lst.append([p,d])
money = [0]*10001
lst.sort(key=lambda x:(-x[0],x[1]))
for i in lst:
    pay,day = i
    for k in range(day,0,-1):
        if money[k]==0:
            money[k]=pay
            break

print(sum(money))