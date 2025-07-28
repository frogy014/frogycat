n = int(input())
arr=[]
for i in range(n):
    arr.append(input())
a=input()
cnt=0
sum_length=0
for i in range(n):
    if arr[i][0] == a:
        cnt+=1
        sum_length+=len(arr[i])
print(f"{cnt} {sum_length/cnt:.2f}")