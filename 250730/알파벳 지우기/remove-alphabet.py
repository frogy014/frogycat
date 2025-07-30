a=input()
b=input()
s_a=""
s_b=""

for i in a:
    if i>='0' and i<='9':
        s_a+=i
for i in b:
    if i>='0' and i<='9':
        s_b+=i
print(int(s_a)+int(s_b))