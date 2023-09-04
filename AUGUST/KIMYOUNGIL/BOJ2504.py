st = list(input())
n = len(st)

if st[0] == ']' or st[0] == ')':
    print(0)

else:
    arr = [0]
    r = 0
    ans = 0
    res = 0
    for i in range(n):
        if st[i] == '(' or st[i] =='[':
            arr.append(st[i])
            ans += r
            r = 0

        elif st[i] == ']':
            if arr[-1] == '[':
                arr.pop()
                if arr == [0]:
                    if r == 0:
                        res += 3
                    else:
                        res += (ans+r)*3
                        r = 0
                        ans = 0
                elif r == 0:
                    r += 3
                else:
                    r *= 3
            else:
                res = 0
                break

        elif st[i] == ')':
            if arr[-1] == '(':
                arr.pop()
                if arr == [0]:
                    if r == 0:
                        res += 2
                    else:
                        res += (ans+r)*2
                        r = 0
                        ans = 0
                elif r == 0:
                    r += 2
                else:
                    r *= 2
            else:
                res = 0
                break
    if len(arr) >= 2:
        res = 0
    print(res)


# 테스트 케이스만 30개는 돌린거 같은데 왜 틀렸지?
# 질문게시판도 다 돌았는데 왜 틀렸지?
# ????