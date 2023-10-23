N = int(input())
arr = [0, 1]

for i in range(2, abs(N) + 1):
    arr.append((arr[i-1] + arr[i-2]) % 1000000000)

if N < 0:
    if abs(N) % 2 == 0:
        print(-1)
    else:
        print(1)
elif N > 0:
    print(1)
else:
    print(0)

print(arr[abs(N)])