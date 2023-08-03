"""
입력 줄
1. 테스트 케이스
2. 층수
3. 호수
4. 층수 반복
5. 호수 반복
a층 b호에 살려면 (a-1)층의 1 ~ b까지 사람들 합친만큼 살아야해. --> 누적합
따라서, k층이면 누적합을 k번 반복, n번째 인덱스 값 출력
"""
T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    Sum_lst = [0] * (n+1)
    # 누적합 리스트 생성
    for i in range(1, n+1):
        Sum_lst[i] = Sum_lst[i-1] + i
    #누적합을 k번 반복 후 n번째 리스트 출력
    for i in range(k-1):
        for j in range(1, n+1):
            Sum_lst[j] += Sum_lst[j-1]
    print(Sum_lst[n])
