array= ['apple','banana','grape','blueberry','orange']

cha=input()
ctr=0
for i in range(len(array)):
    if array[i][2]==cha or array[i][3]==cha:
        print(array[i])
        ctr+=1
print(ctr)