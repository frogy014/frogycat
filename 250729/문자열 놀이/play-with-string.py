s, n= input().split()
arr = list(s)
for _ in range(int(n)):
    rule, first,second = input().split()
    if rule=='1':
        arr[int(first)-1],arr[int(second)-1]=arr[int(second)-1],arr[int(first)-1]
    elif rule=='2':
        for i in range(len(arr)):
            if arr[i]==first:
                arr[i]=second
    s=''.join(arr)
    print(s)