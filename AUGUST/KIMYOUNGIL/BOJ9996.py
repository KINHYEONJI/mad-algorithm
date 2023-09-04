N = int(input())
pattern = input()
star_index = pattern.index('*')
pattern1 = pattern.split('*')
equal = pattern.replace('*','')
for _ in range(N):
    files = input()
    if files == equal:
        print("DA")
    else:
        st = files[len(pattern1[0]):len(files)-len(pattern1[1])]
        pattern2 = pattern.replace('*',st)
        if pattern2 == files:
            print("DA")
        else:
            print("NE")