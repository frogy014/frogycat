n = int(input())

# Please write your code here.
def avg(a):
    sum_a=0
    for i in range(1,a+1):
        sum_a+=i
    return sum_a//10
print(avg(n))