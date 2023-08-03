t = int(input())
for _ in range(t):
    floor_lst = []
    k = int(input())
    n = int(input())
    row=[]
    for i in range(n): #0층 배열 구해주기
        row.append(i+1)
    floor_lst.append(row)
    SUM=0

    for floor in range(0,k):    #1층부터 나머지 층 배열 구해주기
        Sum_lst=[]
        Sum=0
        for room in range(n):
            Sum+=floor_lst[floor][room]
            Sum_lst.append(Sum)

        floor_lst.append(Sum_lst)
    print(floor_lst[k][n-1])