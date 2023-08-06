papers = int(input()) # 색종이 크기는 10*10 
set_papers = []

area = [[0]*100 for _ in range(100)] # 100*100 영역

for i in range(papers):
    x,y = list(map(int,input().split()))  # 사각형 왼쪽 아래 꼭짓점 좌표 
  
    # 0인 area에 색종이 너비만큼 1로 채움
    # 겹쳐도 1이므로 1의 갯수가 색종이 너비
    for i in range(x,x+10):
        for j in range(y,y+10):
            area[i][j] = 1

cnt = 0 # area에서 1의 갯수    
for row in area:
    cnt += row.count(1)
print(cnt)
    

    
     
    
    