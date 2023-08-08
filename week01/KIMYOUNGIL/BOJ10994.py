n = int(input())

def star(x):
    if x == 1:
        return '*'

    a = 4*(x-1)+1
    b = 4*(x-1)-1
    res = star(x-1)
    lst = ['']*a

    lst[0] += '*'*a
    lst[1] += '*' + ' '*b + '*'
    lst[-2] += '*' + ' '*b + '*'
    lst[-1] += '*'*a
    
    for i in range(2,b):
        lst[i] = '* ' + res[i-2] + ' *'

    return lst

ret = star(n)
print(*ret,sep='\n')