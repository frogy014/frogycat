N = int(input())

# Please write your code here.
def muldiv100(n):
    if n==1:
        return 2
    elif n==2:
        return 4
    else:
        return (muldiv100(n-2)*muldiv100(n-1))%100
print(muldiv100(N))