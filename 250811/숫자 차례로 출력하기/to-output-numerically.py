n = int(input())

# Please write your code here.
def line(n):
    if n>0:
        line(n-1)
        print(n,end=" ")
def line_r(n):
    if n>0:
        print(n,end=" ")
        line_r(n-1)

line(n)
print()
line_r(n)