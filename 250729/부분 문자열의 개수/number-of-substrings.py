input_str=input()
target_str=input()
ctr=0
for i in range(len(input_str)-1):
    if input_str[i]==target_str[0] and input_str[i+1]==target_str[1]:
        ctr+=1
print(ctr)        