M, D = map(int, input().split())

# Please write your code here.
def day30(n):
    if n>30:
        return False
    return True
def day31(n):
    if n>31:
        return False
    return True
def day28(n):
    if n>28:
        return False
    return True
def daymonth(m,n):
    if m>12:
        return False
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return day31(n)
    elif m==2:
        return day28(n)
    else:
        return day30(n)
if daymonth(M,D):
    print("Yes")
else:
    print("No")