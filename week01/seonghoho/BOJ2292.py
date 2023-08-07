# 1, 2~7, 8~19, 20~37, 38~61
# += 6의 크기로 증가함
N = int(input())
num = 1
cnt = 1
while num < N:
    num += cnt*6
    cnt += 1

print(cnt)