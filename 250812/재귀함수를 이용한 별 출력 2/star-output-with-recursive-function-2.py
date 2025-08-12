n = int(input())

# Please write your code here.
def star_r(n):
    if n>0:
        for i in range(n):
            print("*",end=" ")
        print()
        star_r(n-1)
        for i in range(n):
            print("*",end=" ")
        print()
star_r(n)