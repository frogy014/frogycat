n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
if n==1:
    print(0)
else:
    max_price=price[1]-price[0]
    for i in range(0, n-1):
        for j in range(i,n):
            if max_price<price[j]-price[i]:
                max_price = price[j]-price[i]
    print(max_price)