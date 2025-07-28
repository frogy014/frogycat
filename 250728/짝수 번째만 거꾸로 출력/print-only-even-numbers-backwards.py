a=input()
if len(a)%2==0:
    for i in a[::-2]:
        print(i,end="")
else:
    for i in a[-2::-2]:
        print(i,end="")