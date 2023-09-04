color_num = int(input())
color_paper = [[0]*100 for _ in range(100)]

def color (x,y):
    for i in range(100):
        for k in range(100):
            if y <= k <= y + 9 and x <= i <= x+9:
                color_paper[i][k] = 1     
for i in range(color_num):
    x,y = map(int,input().split())
    color(x,y)
cnt=0
for i in range(100):
    for k in range(100):
        if color_paper[i][k] == 1 :
            cnt+=1
print(cnt)