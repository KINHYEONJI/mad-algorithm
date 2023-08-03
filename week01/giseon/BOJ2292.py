a=int(input())
# if a==1: #초기 수학식으로 접근 실패식
#     b=-1
# else:
#     b=int(abs(2*((a-1)/6)-6)**(1/2))

# print(b+2)

if a==1: #1일때 1출력
    print(1)
else:
    r=1 #테두리 개수
    c=1 #시작점 1
    while True:
        c+=6*r 
        if a <= c: #7부터시작
            print(r +1)
            break
        r+=1