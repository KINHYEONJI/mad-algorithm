N, K, B = map(int, input().split())
lst = [i for i in range(1, N + 1)]
for i in range(B):  # 고장난 신호등을  0 으로 바꾸기
    idx = int(input()) - 1
    lst[idx] = 0

cnt = lst[:K].count(0)
minn = cnt
for i in range(N - K):
    if lst[i + K] == 0 and lst[i] != 0:
        cnt += 1
    elif lst[i + K] != 0 and lst[i] == 0:
        cnt -= 1
    # 둘 다 0 이거나 0이 아닐 때는, cnt 의 변화 없음.
    minn = min(minn, cnt)

print(minn)
