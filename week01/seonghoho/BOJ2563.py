'''
100*100 중에서 for문 사용해서 칠해진 곳 1로 바꾸기, 
전체에서 0이 아닌 곳 빼서 칠해진 곳의 개수 구하기
'''

T = int(input())
white = [[0]*100 for _ in range(100)]

for _ in range(T):
    x_start, y_start = map(int, input().split())
    for x in range(x_start,x_start+10):
        for y in range(y_start, y_start+10):
            white[y][x] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if white[i][j] == 0:
            cnt+= 1
black = 100*100 - cnt
print(black)