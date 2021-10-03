N = int(input())
plan = [[0,0,0]]
for i in range(N):
    plan.append(list(map(int,input().split())))
ans = "Yes"
for i in range(1,N+1):
    span = plan[i][0] - plan[i-1][0]
    dist = abs(plan[i][1]-plan[i-1][1]) + abs(plan[i][2]-plan[i-1][2])
    if span-dist<0 or (span-dist)%2 == 1:
        ans = "No"
        break
print(ans)