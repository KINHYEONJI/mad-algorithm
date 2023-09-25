#1,2,3,4 분면으로 나누어서 좁혀들어가며 수를 더해가는 구조로 문제를 접근했습니다.
N,r,c=map(int,input().split()) #n을 배열 r은 행 c는 열
N=2**N                                  #2의 제곱으로 사이즈를 키워줍니다
def jague(r,c,sum):                     #행렬과 sum을 구해줍니다.
    global N                            #N은 한번에 구하기 때문에 글로벌 해서 사용해도 무관
    N=N//2

    if r<N and c<N:                     #1사분면에 해당하면 rc 변동 값 없고 sum도 무관
        if N==1:                        #사이즈가 8을 예시로 들면 8 4 2 1 마지막 값은 1이 나오므로 1나올경우 조건에 맞추어 결과 출력
            print(sum)
            exit(0)                     #함수종료
        jague(r,c,sum)
    
    elif r<N and c>=N:                  #2사분면일 경우 C에 N값을 빼주어 또 다음 사분면 판별을 위한 세티 완료
        if N==1:
            print(sum+1)
            exit(0)
        jague(r,c-N,sum+N**2)

    elif r>=N and c<N:                  # 이하 동일
        if N==1:
            print(sum+2)
            exit(0)
        jague(r-N,c,sum+N**2*2)

    elif r>=N and c>=N:
        if N==1:
            print(sum+3)
            exit(0)
        jague(r-N,c-N,sum+N**2*3)

jague(r,c,0)