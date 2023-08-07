n_str = input()
n = int(n_str)

if n % 15 == 0:
    num = n // 5
elif n< 15:
    num = (((n // 5) * 5) // 5) + ((n - ((n // 15) * 15)) // 3)
elif (n - ((n // 15) * 15)) % 3 != 0:
    num = -1
else:
    num = (((n // 15) * 15) // 5) + ((n - ((n // 15) * 15)) // 3)
print(num)
