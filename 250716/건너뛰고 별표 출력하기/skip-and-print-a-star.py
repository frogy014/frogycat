n = int(input())
cnt=1
for i in range(n*2-1):
    print("*"*cnt)
    print()
    if i<n-1:
        cnt+=1
    else:
        cnt-=1