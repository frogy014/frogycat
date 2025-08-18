n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
max_num=0
for i in range(n):
    if max_num<nums[i]+nums[-1-i]:
        max_num=nums[i]+nums[-1-i]

print(max_num)