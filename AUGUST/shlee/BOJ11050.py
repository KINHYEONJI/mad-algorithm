n,k = map(int,input().split())
def fact(num):
    if num > 1:
        return num*fact(num-1)
    else:
        return 1
comb = fact(n)//(fact(n-k)*fact(k))
print(comb)