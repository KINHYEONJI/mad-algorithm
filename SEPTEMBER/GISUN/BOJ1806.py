n,s=map(int,input().split()) #수열크기,합기준
lst=list(map(int,input().split()))
a=0
b=0
sum=0
len_rs=21e8

while 1:
    if sum>=s:
        if (a-b)<len_rs:
            len_rs=(a-b)
    if sum>=s or a==n:
        sum-=lst[b]
        b+=1
    elif sum<s:
        sum+=lst[a]
        a+=1

    if b==n:
        break

if len_rs==21e8:
    print(0)
else:
    print(len_rs)
