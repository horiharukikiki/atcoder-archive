import string
abc = list(string.ascii_lowercase)
ans = ""

print(ans.join(abc[int(i)-1] for i in input().split()))