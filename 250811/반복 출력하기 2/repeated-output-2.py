n = int(input())

# Please write your code here.
def printHello(n):
    if n>0:
        print("HelloWorld")
        printHello(n-1)

printHello(n)