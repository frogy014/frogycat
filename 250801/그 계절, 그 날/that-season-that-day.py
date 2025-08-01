Y, M, D = map(int, input().split())

# Please write your code here.

def isYun(year):
    if year%4!=0:
        return False
    if year%100!=0:
        return True
    if year%400==0:
        return True
    return False 
def season(month):
    if month>11 or month<3:
        print("Winter")
    elif month<6:
        print("Spring")
    elif month<9:
        print("Summer")
    else:
        print("Fall")
def isday28(day):
    if day>28:
        return False
    return True
def isday29(day):
    if day>29:
        return False
    return True
def isday30(day):
    if day>30:
        return False
    return True
def isday31(day):
    if day>31:
        return False
    return True
def isday(year,month,day):
    if month==2:
        if isYun(year):
            return isday29(day)
        else:
            return isday28(day)
    elif month==1 or month==3 or month ==5 or month ==7 or month ==8 or month==10 or month==12:
        return isday31(day)
    elif month>12:
        return False
    else:
        return isday30(day)

if isday(Y,M,D):
    season(M)
else:
    print(-1)

