n=int(input())
arr=[i*n for i in range(1,11)]
if n%5==0:
    for i in range(2):
        print(arr[i],end=" ")
else:
    for i in range(10):
        print(arr[i],end=" ")
