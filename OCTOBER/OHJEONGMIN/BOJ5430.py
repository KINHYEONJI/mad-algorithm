from collections import deque
import sys
input = sys.stdin.readline
def abc():
    global func
    cnt =0
    while func:
        x = func.popleft()
        if x=='R':
            cnt+=1
        elif x=='D':
            if not st or st[0]=='':
                return print('error')
            if cnt%2:
                st.pop()
            else:
                st.popleft()
    if cnt%2:
        st.reverse()
    return print('['+",".join(st)+']')

tc = int(input())
for i in range(tc):
    func = deque(input())
    n = int(input())
    num =input()
    st = deque(num[1:-2].split(','))

    abc()
