n,k = map(int,input().split())
lst = []
result = 0
for i in range(n):
    a = int(input())
    if a<=k:
        lst.append(a)
cnt = 0
lst.sort(reverse=True)
for i in lst:
    while 1:
        if result+i>k:
            break
        else:
            result+=i
            cnt+=1
    if result ==k:
        break
print(cnt)