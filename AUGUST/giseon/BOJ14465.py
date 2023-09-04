N,K,B=map(int,input().split()) #N은 총리시트 개수,k는 이을 개수,b는 고장난 개수
lst=[i for i in range(1,N+1)]

bucket=[0]*(N+1)
for i in range(B):
    a=int(input())
    bucket[a]+=1
print(*bucket)

sum=sum(bucket[1:K+1])
min=sum
for i in range(K+1,N+1):
    sum=sum-bucket[i-K]+bucket[i]
    if min>sum:
        min=sum

print(min)


