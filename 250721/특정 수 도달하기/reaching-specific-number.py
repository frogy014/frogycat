arr = map(int, input().split())
sum_arr=0
cnt=0
for i in arr:
    if i>=250:
        break
    sum_arr+=i
    cnt+=1
print(f"{sum_arr} {sum_arr/cnt:.1f}")