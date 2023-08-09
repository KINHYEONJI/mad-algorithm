n,c = map(int,input().split())
k = list(map(int, input().split()))

arr = []
def setnum(x):
    arr.append(x)

    if n < x:
        return
    
    for i in range(c):
        setnum(10*x+k[i])
    
setnum(0)
print(max(arr))