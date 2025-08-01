a, b = map(int, input().split())

# Please write your code here.
def prior(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def evensum(n):
    esum= n%10
    while n//10!=0:
        n=n//10
        esum+=n%10
    if esum%2==0:
        return True
    else:
        return False
ctr=0
for i in range(a,b+1):
    if evensum(i) and prior(i):
        ctr+=1

print(ctr)