arr= list(map(int,input().split()))
arr_e = arr[1::2]
arr_o = arr[0::2]
if sum(arr_e)>sum(arr_o):
    print(sum(arr_e)-sum(arr_o))
else:
    print(sum(arr_o)-sum(arr_e))