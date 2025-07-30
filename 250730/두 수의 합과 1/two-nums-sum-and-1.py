a,b = map(int,input().split())
c=str(a+b)
cnt_1=0
for i in c:
    if i=='1':
        cnt_1+=1
print(cnt_1)