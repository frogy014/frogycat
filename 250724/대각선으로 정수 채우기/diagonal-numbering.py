n, m = map(int, input().split())

# Please write your code here.
arr = [[0 for _ in range(m)] for _ in range(n)]
cnt=1
start_m = 0 #기준은 오른쪽으로 올라감
start_n = 0 #기준은 초반엔 0에서 고정될거임 m이 끝까지 갔을때,
running_m = 0 #왼쪽으로 움직임
running_n = 0 #아래로 움직임
while True:
    if running_m<0 or running_n>n-1: #기준갱신
        if start_m !=m-1:
            start_m+=1
        else:
            start_n+=1
        running_m=start_m
        running_n=start_n
    arr[running_n][running_m] = cnt
    cnt+=1
    if running_m==m-1 and running_n==n-1: #끝일때
        break
    running_m-=1
    running_n+=1
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
