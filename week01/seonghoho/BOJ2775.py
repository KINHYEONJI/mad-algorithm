T = int(input())
for testcase in range(1, T+1):
    k = int(input()) #k층   
    n = int(input()) #n호
    
    lst = []
    for i in range(1,n+1):
        lst.append(i)

    for i in range(k):
        for j in range(1,n):
            lst[j] += lst[j-1]
    print(lst[-1])