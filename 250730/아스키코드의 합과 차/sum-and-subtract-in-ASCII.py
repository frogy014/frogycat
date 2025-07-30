a,b=input().split()
if b>a:
    a,b=b,a
print(ord(a)+ord(b),ord(a)-ord(b))