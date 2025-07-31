a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(a,b):
    return a+b
def mux(a,b):
    return a*b
def minus(a,b):
    return a-b
def mod(a,b):
    return a//b

if o=='+':
    print(a,o,c,'=',add(a,c))
elif o=='*':
    print(a,o,c,'=',mux(a,c))
elif o=='-':
    print(a,o,c,'=',minus(a,c))
elif o=='/':
    print(a,o,c,'=',mod(a,c))
else:
    print(False)