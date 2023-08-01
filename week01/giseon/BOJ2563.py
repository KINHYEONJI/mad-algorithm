n = int(input())

arr=[[0]*100 for _ in range(100)]
for tc in range(n):
    x, y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

count=0
for i in range(100):
    for j in range(100):
        count +=arr[i][j]
        
print(count)
