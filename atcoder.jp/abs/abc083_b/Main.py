def digiSum(n):
    s = str(n)
    array = list(map(int,s))
    return sum(array)

N,A,B = map(int, input().split())

ans = 0
for n in range(N+1):
    if (A <= digiSum(n) and digiSum(n) <= B):
        ans += n
print(ans)
