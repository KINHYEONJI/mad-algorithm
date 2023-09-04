def abc(result,y,x):

    for i in range(4):
        cnt=1
        dy = y+directy[i]
        dx = x+directx[i]
        if dy>18 or dx>18 or dx<0 or dy<0:
            continue

        while 0<=dy<19 and 0<=dx<19 and omok[dy][dx]==result:
            cnt+=1

            if cnt==5:
                if 0 <= dx - directx[i] < 19 and 0 <= dy - directy[i] < 19 and omok[y - directy[i]][x - directx[i]] == result:
                    break
                if 0 <= dx + directx[i] < 19 and 0 <= dy + directy[i] < 19 and omok[dy + directy[i]][dx + directx[i]] == result:
                    break
                return omok[y][x]
            dy+=directy[i]
            dx+=directx[i]

    return 0
omok = [list(map(int,input().split())) for _ in range(19)]
directx = [0,1,1,1]
directy = [1,1,0,-1]
flag = 0
for i in range(19):
    for k in range(19):
        if omok[i][k] == 1 or omok[i][k]==2:
            ret = abc(omok[i][k],i,k)
            if ret == 0:
                continue
            print(ret)
            print(i+1,k+1)
            exit(0)

else:
    print(0)