T=int(input())
for tc in range(T):
    n = int(input())
    flag=0

    x_1,y_1 = 0,0
    for i in range(n+2):
        x_2, y_2 = map(int,input().split())
        if (x_2-x_1)+(y_2-y_1) <=1000:
            x_1=x_2 
            y_1=y_2
        else:
            flag =1

    if flag == 0:
        print('happy')
    else:
        print('sad')

