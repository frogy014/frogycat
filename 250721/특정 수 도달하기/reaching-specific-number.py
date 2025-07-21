arr = map(int, input().split())
sum_arr=0
cnt=0
for i in arr:
    sum_arr+=i
    if sum_arr>=250:
        sum_arr-=i
        break
    cnt+=1
print(f"{sum_arr} {sum_arr/cnt:.1f}")