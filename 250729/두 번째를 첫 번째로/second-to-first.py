a=list(input())
second_a = a[1]
for i in range(1,len(a)):
    if a[i]==second_a:
        a[i]=a[0]
s = ''.join(a)
print(s)