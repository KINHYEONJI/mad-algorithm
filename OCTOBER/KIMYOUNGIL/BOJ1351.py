n,p,q = map(int,input().split())
dic = {0:1}
def abc(x):
    if dic.get(x,-1) != -1: return dic[x]
    dic[x] = abc(x//p) + abc(x//q)
    return dic[x]
abc(n)
print(dic[n])