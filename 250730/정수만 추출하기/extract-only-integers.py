a,b=input().split()
num_a=""
num_b=""
for i in a:
    if i<'0' or i>'9':
        break
    num_a+=i
for i in b:
    if i<'0' or i>'9':
        break
    num_b+=i
print(int(num_a)+int(num_b))