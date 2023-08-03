N, M = map(int, input().split()) #N*M 배열 입력

numbers = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for i in range(K):
    sum_ = 0
    test_case = list(map(int, input().split()))
    for y1 in range(test_case[1]-1, test_case[3]):
        for x1 in range(test_case[0]-1, test_case[2]):
            sum_ += numbers[x1][y1]
    print(sum_)