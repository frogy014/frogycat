cnt_ee=0
cnt_eb=0
arr=input()
for i in range(len(arr)-1):
    if arr[i]=='e' and arr[i+1]=='e':
        cnt_ee+=1
    if arr[i]=='e' and arr[i+1]=='b':
        cnt_eb+=1
print(cnt_ee,cnt_eb)