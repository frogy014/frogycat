start, end = map(int, input().split())

# Please write your code here.
cnt=0
for i in range(start,end+1):
    dcnt =0
    for j in range(1,i+1):
        if i%j==0:
            dcnt+=1
            if dcnt>3:
                break
    if dcnt==3:
        cnt+=1
print(cnt)