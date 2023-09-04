N, M = map(int, input().split()) #N*M 배열 입력

numbers = [list(map(int, input().split())) for _ in range(N)]
# 테스트 케이스 갯수 입력
K = int(input())

for i in range(K):
    sum_ = 0
    test_case = list(map(int, input().split())) # x1,y1,x2,y2 순서로 입력
    for y1 in range(test_case[1]-1, test_case[3]):
        for x1 in range(test_case[0]-1, test_case[2]):
            sum_ += numbers[x1][y1]
    print(sum_)