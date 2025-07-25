arr=tuple(input().split())
count=0
for i in range(10):
    count+=len(arr[i])
print(count)