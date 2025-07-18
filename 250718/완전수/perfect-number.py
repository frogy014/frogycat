start, end = map(int, input().split())

# Please write your code here.
cnt=0
for i in range(start,end+1):
    sum_cnt=0
    for j in range(1,i):
        if i%j==0:
            sum_cnt+=j
    if sum_cnt==i:
        cnt+=1
print(cnt)