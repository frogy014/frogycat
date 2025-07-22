one_count = [0]*10
arr= list(map(int,input().split()))
for i in arr:
    if i==0:
        break
    one_count[i//10]+=1
for i in range(1,10):
    print(f"{i} - {one_count[i]}")