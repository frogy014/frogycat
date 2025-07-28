n = int(input())
cnt_a=0
sum_ch=0
for i in range(n):
    a = input()
    if a[0]=='a':
        cnt_a+=1
    sum_ch+=len(a)
print(sum_ch,cnt_a)