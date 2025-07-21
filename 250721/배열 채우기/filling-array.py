arr = input().split()
cnt=0
for i in arr:
    if i=="0":
        break
    else:
        cnt+=1
for i in arr[cnt-1::-1]:
    print(i, end=" ")