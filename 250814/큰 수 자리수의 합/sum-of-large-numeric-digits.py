a, b, c = map(int, input().split())

# Please write your code here.

def sumnum(a):
    if a!=0:
        return sumnum(a//10)+a%10
    return 0

print(sumnum(a*b*c))