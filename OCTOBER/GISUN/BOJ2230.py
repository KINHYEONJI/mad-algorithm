N,m=map(int,input().split())
lst=[]
for i in range(N):
    lst.append(int(input()))
lst.sort()                          #두개의 각각 포인터로 잡기 때문에 정렬 필요 (키우고 줄이는데 일관성 주기위해)

lst_r=[]
sum=0
a=0
b=0
while 1:                            #투포인트 사용하기
    sum=lst[a]-lst[b]
    if sum>=m or a==len(lst)-1:
        b+=1
    elif sum<m:
        a+=1
    if abs(sum)>=m:
        lst_r.append(abs(sum))

    if b==len(lst):
        break


print(min(lst_r))