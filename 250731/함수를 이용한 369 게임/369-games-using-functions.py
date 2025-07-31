a, b = map(int, input().split())

# Please write your code here.
def is369(i):
    if i%3==0:
        return 1
def isone(i):
    if i//10==0:
        return is369(i)
    else:
        return(isone(i//10) or is369(i%10))
def game369(i):
    return i%3==0 or isone(i)

ctr=0
for i in range(a,b+1):
    if game369(i):
        ctr+=1
print(ctr)