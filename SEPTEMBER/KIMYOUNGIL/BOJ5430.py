import sys
from collections import deque
input = sys.stdin.readline

def abc():
    global st
    cnt = 0
    while q:
        p = q.popleft()
        if p == 'R':
            cnt += 1
        elif p == 'D':
            if not st or st[0] == "":
                return print('error')
            else:
                if cnt%2:
                    st.pop()
                else:
                    st.popleft()
    if cnt%2:
        st.reverse()
    return print("["+",".join(st)+"]")

for _ in range(int(input())):
    q = deque(input())
    n = int(input())
    arr = input()

    st = deque(arr[1:-2].split(','))
    abc()