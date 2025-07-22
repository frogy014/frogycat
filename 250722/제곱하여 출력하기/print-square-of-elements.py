n=int(input())
arr = list(map(int,input().split()))
pow_arr = [i**2 for i in arr]

for i in range(n):
    print(pow_arr[i],end=" ")