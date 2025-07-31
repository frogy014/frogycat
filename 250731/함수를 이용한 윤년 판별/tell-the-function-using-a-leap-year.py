y = int(input())

# Please write your code here.
def yun(year):
    if year%4!=0:
        return 'false'
    if year%100==0 and year%400!=0:
        return 'false'
    return 'true'

print(yun(y))