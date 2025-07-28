arr=[]
for i in range(10):
    arr.append(input())
a=input()
isnull=True
for i in range(10):
    if arr[i][-1]==a:
        isnull=False
        print(arr[i])
if isnull==True:
    print("None")
