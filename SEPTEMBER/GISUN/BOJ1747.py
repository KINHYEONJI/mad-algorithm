import math


def palin(target):                #palin 확인 함수
    x=str(target)

    for i in range(len(x)//2):
        if x[i]!=x[-1-i]:
            return 0
    return 1

n=int(input())
if n==1:                        #n=1일 경우 2나오게 예외처리
    print(2)
    exit(0)
check=[0]*(1100001)              #소수 체크 리스트 생성 n이 1000000만 근접 시 그 이상값이 나올 수 있어 범위를 더 크게 책정 
end=int(math.sqrt(1100001))

for i in range(2,end+1):         #에라토스테네스의 체 로 소수 버킷 세팅
    if check[i]==1:continue
    for j in range(2*i,1100001,i):
        check[j]=1

flag=0
for i in range(n,1100001):        #소수인 경우 palin 함수를 걸어두어 플래그 걸리면 출력후 함수종료
    if check[i]==0:
        flag=palin(i)
        if flag==1:
            print(i)
            exit(0)