n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def change_m():
    global m
    if m%2==0:
        m//=2
    else:
        m-=1

sumA=0
for i in range(n): 
    sumA+=A[m-1]
    if m==1:
        break
    change_m()
print(sumA)