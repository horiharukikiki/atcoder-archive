contests = ["ABC","ARC","AGC","AHC"]

s = [input() for i in range(3)]

for a in contests:
    if a not in s:
        print(a)