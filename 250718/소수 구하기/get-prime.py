n=int(input())
for i in range(1,n+1):
    for j in range(2,i//2+2):
        if j==i//2+1:
            print(i,end=" ")
        if i%j==0:          
            break
