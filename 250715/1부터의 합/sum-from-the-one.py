n=int(input())
sum_var=0
for i in range(1,100):
    sum_var+=i
    if sum_var>=n:
        break
print(i)