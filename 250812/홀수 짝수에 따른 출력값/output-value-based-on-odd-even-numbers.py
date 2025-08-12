N = int(input())

# Please write your code here.
def odd_sum(n):
    if n>0:
        return odd_sum(n-2)+n
    return 0
def even_sum(n):
    if n>0:
        return even_sum(n-2)+n
    return 0
if N%2==0:
    print(even_sum(N))
else:
    print(odd_sum(N))