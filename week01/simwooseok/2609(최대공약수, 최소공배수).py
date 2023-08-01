A, B = map(int, input().split())
multi = A * B
while  True:
    rem = A % B

    A, B = B, rem
    if rem == 0 :
        break

print(A)
print((multi) // A )
