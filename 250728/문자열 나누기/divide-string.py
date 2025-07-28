n=int(input())
arr=input().split()
str_s=""
for i in range(n):
    str_s+=arr[i]
for i in range(len(str_s)):
    if (i+1)%5==0:
        print(str_s[i])
    else:
        print(str_s[i],end="")