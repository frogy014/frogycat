N = int(input())

# Please write your code here.
def pow_sum(n):
    if n<10:
        return n*n
    return pow_sum(n//10)+(n%10)*(n%10)
print(pow_sum(N))