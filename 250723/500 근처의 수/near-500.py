arr = list(map(int,input().split()))
under500 = 1
upper500 = 1000
for i in arr:
    if upper500 > i >500:
        upper500 = i
    elif under500< i < 500:
        under500 = i
print(under500,upper500)