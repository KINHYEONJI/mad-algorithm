sugar = int(input())
def Search(sugar):
    cnt = 0
    while sugar>=0:
        if sugar % 5 == 0:
            cnt+=sugar//5
            return cnt
        sugar-=3
        cnt+=1
    return -1
print(Search(sugar))