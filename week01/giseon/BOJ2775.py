t= int(input())

for i in range(t):
    k = int(input())    # 층선언
    n= int(input())     # 호선언
    lst=[i for i in range(1,n+1)]
    
    arr=[]
    arr.append(lst)
    
    for i in range(1,k+1): #층만큼반복
        lst=[]
        for j in range(n): #호만큼반복
            if j==0: #0일 때 1넣기 김영일?
                lst.append(1)

            else:
                lst.append(sum(arr[i-1][:j+1]))
        arr.append(lst)
    print(arr[k][n-1]) #값뽑기
