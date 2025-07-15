n = int(input())
answer= "P"
for i in range(2,n//2):
    if n%i==0:
        answer="C"
print(answer)