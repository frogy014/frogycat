n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min1,min2 = a[0],a[1]
if min1<min2:
    min1,min2 = min2, min1
for i in range(2,len(a)):
    if min1<a[i]:
        min1, min2 = a[i],min1
    else:
        if min2<a[i]:
            min2=a[i]

print(min1,min2)