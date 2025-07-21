arr = input().split()
arr = arr[::-1]
if arr[0]=="0":
    for i in arr[1:]:
        if i!="0":
            print(i,end=" ")
        else:
            break
else:
    for i in arr:
        if i!="0":
            print(i,end=" ")
        else:
            break