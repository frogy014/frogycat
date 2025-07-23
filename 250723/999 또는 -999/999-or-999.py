arr =list(map(int,input().split()))
min_num=arr[0]
max_num=arr[0]
for i in arr:
    if i == 999 or i == -999:
        break
    if min_num>i:
        min_num=i
    if max_num<i:
        max_num =i
print(max_num,min_num)