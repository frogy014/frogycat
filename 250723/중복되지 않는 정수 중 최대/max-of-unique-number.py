n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
same_nums=[]
for i in range(n):
    for j in range(i+1,n):
        if nums[i]==nums[j]:
            same_nums.append(nums[i])
            break
max_num=-1
is_same=False
for i in nums:
    for j in same_nums:
        if i==j:
            is_same=True
            break
    if is_same==False:
        if max_num<i:
            max_num=i
    is_same=False
print(max_num)