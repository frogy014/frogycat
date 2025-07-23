n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
while True:
    x = max(a)
    if a[0]==x:
        print(1)
        break
    for i in range(1,len(a)):
        if a[i]== x:
            print(i+1,end=" ")
            a = [a[j] for j in range(0,i)]
            break