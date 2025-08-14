N = int(input())

# Please write your code here.

def isan(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return isan(n//3)+isan(n-1)

print(isan(N))