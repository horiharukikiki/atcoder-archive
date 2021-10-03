n = int(input())
a = [int(i) for i in input().split()]
x = int(input())

total = sum(a)
count = x//total
temp = count*total
t=0
while temp <= x:
    temp+=a[t]
    t+=1
print(count*n+t)