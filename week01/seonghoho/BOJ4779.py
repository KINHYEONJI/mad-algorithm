def line(n, i, j): # n번 반복, i 시작점, j 끝점
    if n==0 :
        return
    
    #3등분
    cnt = (j-i+1)//3
    #왼쪽
    line(n-1, i, i+cnt-1)
    #가운데 -> 공백으로 바꾸기
    for k in range(i + cnt, i+ cnt * 2):
        lst[k] = ' '
    #오른쪽
    line(n-1, i + cnt*2, i + cnt * 3 -1)

while True:
    try:
        N = int(input())
        lst = ['-']*(3**N)
        line(N,0,3**N-1)
        print(''.join(lst))
    except:
        break