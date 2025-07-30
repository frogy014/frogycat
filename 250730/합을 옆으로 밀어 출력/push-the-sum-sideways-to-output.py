n=int(input())
sum_n=0
for i in range(n):
    sum_n+=int(input())
s = str(sum_n)
print(s[1:]+s[0])