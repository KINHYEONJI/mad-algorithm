from math import sqrt
n = int(input())

def prime(x):
    if x < 2: return -1
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0: return 0
    return 1

i = n
while 1:
    st = list(str(i))
    st1 = st.copy()
    st.reverse()
    if st == st1:
        if prime(i) == 1: print(i); break   
        else: i += 1
    else: i += 1