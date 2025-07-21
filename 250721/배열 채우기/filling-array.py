arr = input().split()
if arr[len(arr)-1]=="0":
    for i in arr[len(arr)-2::-1]:
        if i=="0":
            break
        else:
            print(i,end=" ")
else:
    for i in arr[::-1]:
        if i=="0":
            break
        else:
            print(i,end=" ")