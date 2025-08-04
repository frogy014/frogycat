A = input()

# Please write your code here.
is_one_chr = True
first=A[0]
for i in A:
    if first!=i:
        is_one_chr=False
        break
if is_one_chr:
    print("No")
else:
    print("Yes")