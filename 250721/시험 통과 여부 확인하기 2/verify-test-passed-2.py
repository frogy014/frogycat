n = int(input())
passman=0
for i in range(n):
    arr = list(map(int,input().split()))
    if sum(arr)/4>=60:
        passman+=1
        print("pass")
    else:
        print("fail")
print(passman)