A = input()
B = input()

# Please write your code here.
i=0
while B in A:
    is_in = True
    for j in range(len(B)):
        if A[i+j]!=B[j]:
            is_in=False
            break
    if is_in:
        A = A[:i]+A[i+len(B):]
        i=0
    else:
        i+=1
print(A)


