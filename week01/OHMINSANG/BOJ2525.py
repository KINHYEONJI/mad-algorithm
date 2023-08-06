'''
lst[0], [1] == 현재 시, 현재 분
num = 소모 시간(분)
lst[1] // 60 --> lst[0] + alpha
lst[1] % 60 --> lst[1]
'''
lst = list(map(int, input().split()))
num = int(input())

lst[0] = (lst[0] + ((lst[1] + num) // 60)) % 24
lst[1] = (lst[1] + num) % 60
print(*lst)
