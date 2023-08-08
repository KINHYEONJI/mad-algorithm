def canto(x,st):
    if x == 0:
        print("-",end="")
        return
    
    canto(x-1,st)
    print(" "*((3**x)//3),end="")
    canto(x-1,st)


while 1:
    try:
        n = int(input())
        canto(n,"")
        print()
    except EOFError:
        break