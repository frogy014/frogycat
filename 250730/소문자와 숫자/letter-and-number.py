a=input()
for i in a:
    if i>='A' and i<='Z':
        print(i.lower(),end="")
    elif (i>='a' and i<='z') or (i>='0' and i<='9'):
        print(i,end="")