n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_n = min(a)
ctr=0
for i in a:
    if min_n==i:
        ctr+=1
print(min_n,ctr)