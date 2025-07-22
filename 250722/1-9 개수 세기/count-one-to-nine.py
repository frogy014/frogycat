n = int(input())
arr=list(map(int,input().split()))
arr_count = [0]*9
for i in arr:
    arr_count[i-1]+=1
for i in arr_count:
    print(i)