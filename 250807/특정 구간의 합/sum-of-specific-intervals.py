n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sumprint():
    sumd=0
    for i in range(m):
        for j in range(queries[i][0]-1,queries[i][1]):
            sumd+=arr[j]
        print(sumd)
        sumd=0
sumprint()