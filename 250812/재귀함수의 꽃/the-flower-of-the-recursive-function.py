N = int(input())

# Please write your code here.
def printn(n):
    if n>0:
        print(n,end=" ")
        printn(n-1)
        print(n,end=" ")
printn(N)