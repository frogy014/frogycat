a,b,c = map(int,input().split())
exi = "NO"
for i in range(a,b+1):
    if i%c==0:
        exi="YES"
print(exi)