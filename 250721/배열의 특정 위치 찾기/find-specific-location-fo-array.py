arr = list(map(int,input().split()))
arr_2 = arr[1::2]
arr_3 = arr[2::3]

print(f"{sum(arr_2)} {sum(arr_3)/3:.1f}")