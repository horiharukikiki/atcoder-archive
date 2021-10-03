s = [input() for i in range(3)]
T = input()

ans = ""
for t in T:
    ans+=s[int(t)-1]
print(ans)