n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def is_same(a,b,ctr):
    if a==b:
        return ctr+1
    else:
        return 0
ctr=0
for i in range(n1-n2+1):
    if is_same(a[i],b[0],ctr):
        ctr=1
        for j in range(1,n2):
            ctr=is_same(a[i+j],b[j],ctr)
            if ctr==0:
                break
if ctr!=0:
    print("Yes")
else:
    print("No")