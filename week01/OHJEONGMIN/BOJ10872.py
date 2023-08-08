N = int(input())
def factorial(value):
    if value>1:
        ret = value*factorial(value-1)
        return ret
    else:
        return 1

print(factorial(N))