X = input()
n = int(input())
S = [input() for i in range(n)]

d = {}
for i, xi in enumerate(X):
    d[xi] = i

S2 = []
 
for si in S:
    t = []
    for c in si:
        t.append(d[c])
    S2.append(t)
sortS2 = sorted(S2)

for si in sortS2:
    s = ""
    for pos in si:
        s += X[pos]
    print(s)