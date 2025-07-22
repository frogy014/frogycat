n = int(input())
arr = [1,n]
while True:
    arr.append(arr[-1]+arr[-2])
    if arr[-1]>100:
        break
for i in arr:
    print(i,end=" ")