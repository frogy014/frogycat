a, b = map(int, input().split())

# Please write your code here.
def mux(a,b):
    return a*b

answer=1
for _ in range(b):
    answer = mux(answer,a)
print(answer)
