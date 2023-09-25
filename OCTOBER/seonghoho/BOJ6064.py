T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    i = 0
    result = -1  # 기본값을 -1로 두기

    if N == y:  ### N과 y가 같을 때 나머지 값은 0이니, y를 0으로 바꾸고 실행하도록 해야 한다.
        y = 0
    while 1:
        if ((M * i) + x) % N == y:  # M을 i번 곱하고 나머지인 x를 더한 값이 결괏값이고, N에서의 식을 적용하자
            result = (M * i) + x  # 위의 값이 해당되면 (M*i)+x가 결괏값이 된다.
            break
        if (M * i) + x > M*N:  # 출력할 값이 M*N 값보다 크면 범위를 넘은거기 때문에 result값 갱신하지 않고 바로 break
            break
        i += 1  # i값 1씩 올리면서 본다.
    print(result)
