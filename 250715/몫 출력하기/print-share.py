count=3
while True:
    n = int(input())
    if n%2==0:
        n//=2
        print(n)
        count-=1
        if count==0:
            break