ctr=0
arr=[]
while True:
    a=input()
    if a=='0':
        break
    arr.append(a)
    ctr+=1
print(ctr)
for i in range(0,ctr,2):
    print(arr[i])