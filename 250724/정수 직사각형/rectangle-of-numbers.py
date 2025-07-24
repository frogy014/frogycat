n,m=map(int,input().split())
arr = [[0 for i in range(m)] for i in range(n)]

cnt=1
for i in range(n):
    for j in range(m):
        arr[i][j] = cnt
        cnt+=1
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ") 
    print()  