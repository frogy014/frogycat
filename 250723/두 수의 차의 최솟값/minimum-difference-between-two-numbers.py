n = int(input())
arr=list(map(int,input().split()))
min_di = arr[1]-arr[0]
for i in range(2,n):
    if arr[i]-arr[i-1]<min_di:
        min_di = arr[i]-arr[i-1]
print(min_di)
    