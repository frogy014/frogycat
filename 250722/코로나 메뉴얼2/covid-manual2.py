arr = [0]*4
for _ in range(3):
    s,t = input().split()
    if s=="Y":
        if int(t)>=37:
            arr[0]+=1
        else:
            arr[2]+=1
    else:
        if int(t)>=37:
            arr[1]+=1
        else:
            arr[3]+=1
for i in range(4):
    print(arr[i],end=" ")
if arr[0]>=2:
    print("E")