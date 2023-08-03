N,M=map(int,input().split())
arr=[] 
lst_y=[]
for i in range(N): # 조건 받아서 배열 선언
    lst_y=list(map(int,input().split()))
    arr.append(lst_y)

K=int(input())


def asum(y,x,a,b): #함수 선언 ij 배열을 기준으로 xy까지 사이의 공간을 높이 a,가로 b로 대입하여 ab영역의 합구하기
    sum=0
    for i in range(a): #높이
        for j in range(b): #가로
            sum+=arr[y+i][x+j]
    return sum


for i in range(K):     #i,j받고 x,y받아서 ij기준으로 xy까지의 범위의 직사각형 함수에 넣어구하기
    i,j,x,y = map(int,input().split())
    a=asum(i-1,j-1,x-i+1,y-j+1)
    
    print(a)

    #시간 제한으로 인하여 실패^ 오드비 작은 식을쓰자..