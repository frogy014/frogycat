arr = list(map(int,input().split()))
test_count = [0]*11 #100점도 있으니까
for i in arr:
    if i ==0:
        break
    test_count[i//10]+=1
for i in range(10,0,-1):
    print(f"{i*10} - {test_count[i]}")
