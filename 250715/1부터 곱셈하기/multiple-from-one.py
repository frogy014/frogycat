n = int(input())
proc=1
for i in range(1,11):
    proc*=i
    if proc>=n:
        print(i)
        break