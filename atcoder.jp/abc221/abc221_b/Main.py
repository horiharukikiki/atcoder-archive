S = input()
T = input()

if S == T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    tmp = S[i:i+2][::-1]
    if S.replace(S[i:i+2],tmp) == T:
        print("Yes")
        exit()
print("No")