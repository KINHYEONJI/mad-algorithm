import sys
input = sys.stdin.readline
N=int(input())

lst = []

for i in range(N):
    a,b = map(int,input().split())
    lst.append([a,b])

lst.sort()

s, e = lst[0]
length = e-s

for i in range(1,N):
    a,b = lst[i]

    if e < a:
        length += b-a
        s,e =a,b
    elif e <b:
        length += b-e
        e=b

print(length)