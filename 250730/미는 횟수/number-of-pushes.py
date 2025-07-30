ctr=0
is_same=-1
a = input()
b=input()
for i in range(len(a)):
    if a==b:
        print(ctr)
        is_same=0
    a = a[-1]+a[:-1]
    ctr+=1
if is_same==-1:
    print(is_same)