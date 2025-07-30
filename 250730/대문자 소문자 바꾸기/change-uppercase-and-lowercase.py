a = input()
for i in a:
    if i >='A' and i<='Z':
        print(i.lower(),end="")
    elif i>='a' and i<='z':
        print(i.upper(),end="")
    