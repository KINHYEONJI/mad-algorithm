n,m = map(int,input().split())
a,b = 0,0
result= []
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
Sum = 0
while 1:
    Sum = lst[a]-lst[b]
    if Sum>=m or a==len(lst)-1 :
        b+=1
    elif Sum<m:
        a+=1
    if abs(Sum)>=m:
        result.append(abs(Sum))
    if b == len(lst):
        break
print(min(result))