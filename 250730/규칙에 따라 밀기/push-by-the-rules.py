arr=input()
command=input()
for i in command:
    if i == 'L':
        arr=arr[1:]+arr[0]
    elif i=='R':
        arr=arr[-1]+arr[:-1]        
print(arr)