n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    sumc=0
    for i in range(a,b+1):
        if i%2==0:
            sumc+=i
    print(sumc)