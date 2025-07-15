arr = map(int,input().split())
answer=1
for i in arr:
    if i%3!=0:
        answer=0
print(answer)
