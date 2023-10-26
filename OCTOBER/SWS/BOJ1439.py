S = list(input())
cnt1 = 0
cnt2 = 0
for i in range(len(S)-1):
    if S[i] == '1' and S[i+1] == '0':
        cnt1 += 1
    elif S[i] == '0' and S[i+1] =='1':
        cnt2 += 1
print(max(cnt1, cnt2))