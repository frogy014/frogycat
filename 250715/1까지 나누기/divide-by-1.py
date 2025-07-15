n = int(input())
i=1
while True:
    n//=i
    print(n)
    if n<=1:
        break
    i+=1
    