N = int(input())
copy = N
cnt = 0

while True:
    N = (N%10)*10 + (((N//10)+(N%10))%10)
    cnt += 1
    if copy == N:
        break
    
print(cnt)