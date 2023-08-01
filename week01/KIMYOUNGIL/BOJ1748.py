n = int(input())

if n//10 == 0:
    print(n)

else:
    l = len(str(n))
    a = int("1"*(l-1))

    sum = 9
    for i in range(2,l):
        sum += i*(9*(10**(i-1)))
    sum += (n-9*a)*l

    print(sum)



    

    

