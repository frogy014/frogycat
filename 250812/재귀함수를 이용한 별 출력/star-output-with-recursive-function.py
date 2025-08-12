n = int(input())

# Please write your code here.
def printstar(n):
    if n>0:
        printstar(n-1)
        for i in range(n):
            print("*",end="")
        print()
printstar(n)