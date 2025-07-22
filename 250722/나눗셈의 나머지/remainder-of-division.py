n, prod = map(int,input().split())
r_arr = [0]*prod

while n>1:
    r_arr[n%prod]+=1
    n //=prod
sum_result=0

for i in range(prod):
    sum_result += r_arr[i]**2
print(sum_result)