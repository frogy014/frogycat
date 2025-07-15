sum_var=0
cnt=0
while True:
    n=int(input())
    if n>=30 or n<20:
        break
    sum_var+=n
    cnt+=1
print(f"{sum_var/cnt:.2f}")