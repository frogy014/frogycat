n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def ars(n,arr):
    for i in range(n):
        if arr[i] <0:
            arr[i] = -arr[i]
ars(n,arr)
for i in range(n):
    print(arr[i],end=" ")