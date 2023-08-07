st = input().upper()
lst = list(set(st))

cntlst = []

for i in lst:
    cnt = st.count(i)
    cntlst.append(cnt)

if cntlst.count(max(cntlst)) > 1:
    print("?")
else:
    print(lst[(cntlst.index(max(cntlst)))])

