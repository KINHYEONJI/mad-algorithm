```python
N, K=map(int,input().split()) #N보다 작거나 같은 수 구해야함 k는 원소개수
arr=list(map(int,input().split()))

max_=0 #맥스 정의
sum_=0 #선언을 해준다 전역변수
a=[]
def abc(level):
    global sum_,a

    if level ==len(str(N)): #우선은 주어진 N자리수 만큼 만들 수 있는 레벨을 설정
        return

    
    for i in range(len(arr)):
        sum_+=arr[i]*10**(level) #1의 자리에 (arr)의 요소를 하나씩 채워나가준다
        abc(level+1)
        a.append(sum_) #11라인 if에서 원하는 값을 어펜드했는데 10000 자리와 같은 경우 원하는 결과 값이 안 나와 위치 수정
        sum_-=arr[i]*10**(level) #sum_은 전역변수여서 다시 꼭 빼주어 원래 상태를 유지해준다

             
abc(0)

for i in range(len(a)):
    if a[i] <=N and a[i] > max_:
        max_=a[i]
print(max_)
```