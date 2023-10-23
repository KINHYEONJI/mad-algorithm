n = int(input())

if n == 0:
    print(0)
    print(0)

else:
    fibo = [0]*(abs(n)+1)
    fibo[1] = 1
    i = 2
    while i < abs(n)+1:
        fibo[i] = (fibo[i-1] + fibo[i-2])%(10**9)
        i += 1
    if n < 0 and abs(n)%2 == 0:
        print(-1)
        print(fibo[abs(n)])
    else:
        print(1)
        print(fibo[abs(n)])