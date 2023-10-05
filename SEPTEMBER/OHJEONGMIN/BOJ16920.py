from collections import deque


n,m,p = map(int,input().split())
s_lst = input().split()

lst = []
for i in range(n):
    lst.append(input())
dry,drx = [],[]
for i in range(p):
    arr_y = []
    arr_x = []
    d_y = [1,-1,0,0]
    d_x = [0,0,-1,1]
    for k in range(4):
        arr_y.append(d_y[k]*int(lst[i]))
        arr_x.append(d_x[k] * int(lst[i]))
    dry.append(arr_y)
    drx.append(arr_x)
