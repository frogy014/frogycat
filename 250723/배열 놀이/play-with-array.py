n,q = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(q):
    qustionarr = list(map(int,input().split()))
    if qustionarr[0]==1:
        print(arr[qustionarr[1]-1])
    elif qustionarr[0]==2:
        for i in range(n):
            if arr[i]==qustionarr[1]:
                print(i+1)
                break
            if i==n-1:
                print(0)
    elif qustionarr[0]==3:
        for i in range(qustionarr[1]-1,qustionarr[2]):
            print(arr[i],end=" ")
        print()