arr = input().split()
arr = arr[::-1]
if arr[0]=="0":
    for i in arr[1:]:
        print(i,end=" ")
else:
    for i in arr:
        print(i,end=" ")