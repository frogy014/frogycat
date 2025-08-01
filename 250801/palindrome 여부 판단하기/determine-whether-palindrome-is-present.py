A = input()

# Please write your code here.

def reverse(string):
    s=""
    for i in range(len(string)-1,-1,-1):
        s+=string[i]
    return s
if A ==reverse(A):
    print("Yes")
else:
    print("No")