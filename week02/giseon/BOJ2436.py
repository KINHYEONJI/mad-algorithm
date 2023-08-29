def gcd(a,b):
    while b!=0:
        backup=b
        b=a%b
        a=backup
    return a
a,b=map(int,input().split()) #a는 최대공약수 b는 최소공배수
c=b//a #최대공배수를 최대공약수로 나눈값
lst=[] #약수 담을 리스트 선언
if b%a!=0:
    print(0)
else:
    for i in range(1,c+1):
        if c%i==0:
            lst.append(i)
    if len(lst)%2==0:
        min=21e8
        for i in range(len(lst)-1):
            
            if min>lst[i]+lst[-(i+1)] and gcd(lst[i],lst[-(i+1)])==1:
                min=lst[i]+lst[-(i+1)]
                d=lst[i]
                f=lst[-(i+1)]

    else:
        d,f=lst[len(lst)//2]
    print(a*d,a*f)



