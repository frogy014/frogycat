a = list(input())
first_a = a[0]
second_a = a[1]
for i in range(len(a)):
    if a[i]==first_a:
        a[i]= second_a
    elif a[i]==second_a:
        a[i] = first_a
s = ''.join(a)
print(s)