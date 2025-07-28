A = input()

# Please write your code here.
a=[]
a.append(A[0])
a.append(1)
cnt=2
cnt_10 =0 #만약에 십의 자리나 백의 자리로 넘어갈때마다 쓰는거
for i in range(1,len(A)):
    if A[i]==a[cnt-2]:
        a[cnt-1]=int(a[cnt-1])+1
        if a[cnt-1]==10 or a[cnt-1]==100 or a[cnt-1]==1000:
            cnt_10+=1
    else:
        a.append(A[i])
        a.append(1)
        cnt+=2

print(cnt+cnt_10)

for i in range(len(a)):
    print(a[i],end="")