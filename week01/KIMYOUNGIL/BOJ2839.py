n = int(input())

lst = [2,3,4,3,4,3,4,5,4,5]
if n >= 10:
    print(lst[n%10]+2*((n//10)-1))
elif n in [1,2,4,7]:
    print(-1)
elif n in [3,6,9]:
    print(n//3)
elif n == 5:
    print(1)
else:
    print(2)