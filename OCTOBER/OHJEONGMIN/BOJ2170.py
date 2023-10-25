import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:x[1])
right = lst[-1][1]
lst.sort(key=lambda x:x[0])
left = lst[0][0]


result = right-left
distance=0
flag =1
target = lst[0][0]
for i in lst:
    if target==right:
        break
    if target<=i[0]:
        if target<i[0]:
            distance+=i[0]-target
        target = i[1]
    elif target>i[0] and i[1]>target:
        target = i[1]



print(result-distance)