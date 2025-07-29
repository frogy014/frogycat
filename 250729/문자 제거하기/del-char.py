arr=list(input())
while len(arr)!=1:
    a=int(input())
    if a>=len(arr):
        arr.pop(len(arr)-1)
    else:
        arr.pop(a)
    s=''.join(arr)
    print(s)