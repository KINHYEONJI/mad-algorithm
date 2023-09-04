# 솔직히 말하면 
# 3문제 다 못 풀었습니다
# 그나마 별찍기 규칙은 몇개 찾았는데
# 재귀로 구현을 못해서..
# 블로그에 있는 코드 보고
# 분석했습니다..... .... ... .. . 

n = int(input())
len = 4*n-3 # 1,5,9씩 늘어남 
star = [[' '] * len for _ in range(len)] # 별 그릴 도화지 만들고

def draw(n, idx):
    if n == 1:     # n이 1일땐 별 하나 찍고 탈출
        star[idx][idx] = '*'     
        return
    a = 4*n - 3

    for i in range(idx, a+idx): 
        #위아래
        star[idx][i] = '*'
        star[idx+a-1][i] = '*'
        
        #양옆
        star[i][idx] = '*'
        star[i][idx+a-1] = '*'

    return draw(n-1, idx+2)   # n이 1 줄 때마다 상하좌우 2칸씩 증가해서 별찍음 

draw(n,0)
for i in range(len):
    for j in range(len):
        print(star[i][j], end="")
    print()