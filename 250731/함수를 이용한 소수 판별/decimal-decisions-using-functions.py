a, b = map(int, input().split())

# Please write your code here.
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

sum_prime=0
for i in range(a,b+1):
    if isprime(i):
        sum_prime+=i
print(sum_prime)