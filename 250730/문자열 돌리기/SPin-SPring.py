a=input()
print(a)
for i in range(len(a)):
    a = a[len(a)-1]+a[:len(a)-1]
    print(a)