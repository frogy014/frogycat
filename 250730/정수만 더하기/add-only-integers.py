a=input()
sum_d=0
for i in a:
    if i>'0' and i<'9':
        sum_d+= ord(i)-ord('0')
print(sum_d)
