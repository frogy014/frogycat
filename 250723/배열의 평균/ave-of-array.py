arr = [list(map(int,input().split())) for i in range(2)]
for i in range(2):
    print(f"{sum(arr[i])/4:.1f}",end=" ")
print()
for j in range(4):
    sum_arr=0
    for i in range(2):
        sum_arr+=arr[i][j]
    print(f"{sum_arr/2:.1f}",end=" ")
print()
sum_arr=0
for i in range(2):
    sum_arr+=sum(arr[i])
print(f"{sum_arr/8:.1f}")