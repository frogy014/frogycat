N = int(input())

# Please write your code here.

def req_sum(n):
    if n==1:
        return 1
    return req_sum(n-1)+n

print(req_sum(N))