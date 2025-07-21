arr = list(map(int,input().split()))
cnt=0
sun_arr=0
for i in arr:
    if i==0:
        break
    else:
        cnt+=1
        sun_arr+=i
print(f"{sun_arr} {sun_arr/cnt:.1f}")