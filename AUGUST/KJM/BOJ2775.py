'''
현재 k층의 n호는
k-1층의 n호까지의 누적합임 
처음 시작인 0층은 n호까지
1,2,3,4,5... 선형증가함 

따라서 n호의 값을 받고싶으면
우선 0층 n호까지 배열을 만들고
k층까지 이전층을 참고해서 누적합을 하면된다 

핵심은 
1) 구하려는 n호수까지 0층의 n호수를 만들 것
2) 그리고 k층의 n호수까지 누적합 할 것 
'''

T = int(input())

for tc in range(T):
    

    k = int(input()) # 층 수 
    n = int(input()) # 호 수 
    
    # n호까지 0층 사람 수 배열 만들기
    # if tc <= 0:
    zero_floor = []
    for i in range(1, n+1): # 사람이니까 1명부터 시작 n = 3 / 1,2,3
        zero_floor.append(i)
    
    # k층 까지 누적합
    for i in range(k):
        for j in range(1, n):
            zero_floor[j] += zero_floor[j - 1]

    print(zero_floor[n-1])    
    
    
    