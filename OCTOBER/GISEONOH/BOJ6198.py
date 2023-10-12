import sys
input=sys.stdin.readline
n=int(input())

lst=[int(input()) for i in range(n)]
# print(lst)


rs=0
for i in range(len(lst)):
    
    # print(i)
    for j in range(i+1,len(lst)):
        if lst[i]<lst[j]:
            break
        else:
            rs+=1

print(rs)