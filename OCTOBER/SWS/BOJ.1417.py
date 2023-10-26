N = int(input())  
dasom = int(input())  
if N == 1:
    print(0)
else:
    temp = [] 
    for i in range(N - 1):
        temp.append(int(input()))

    cnt = 0
    while dasom <= max(temp):
        temp[temp.index(max(temp))] -= 1
        dasom += 1
        cnt += 1
    print(cnt)