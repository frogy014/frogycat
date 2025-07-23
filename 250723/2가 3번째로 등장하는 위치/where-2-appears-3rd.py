n = int(input())
arr = list(map(int,input().split()))
count_2 =0
for i in range(len(arr)):
    if arr[i]==2:
        count_2+=1
        if count_2==3:
            print(i+1)
