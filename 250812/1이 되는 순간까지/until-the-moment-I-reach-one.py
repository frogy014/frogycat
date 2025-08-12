N = int(input())

# Please write your code here.
def cnt(n):
    if n==1:
        return 0
    if n%2==0:
        return cnt(n//2)+1
    else:
        return cnt(n//3)+1
    
print(cnt(N))