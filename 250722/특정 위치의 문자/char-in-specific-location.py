idx=-1
word = ['L','E','B','R','O','S']
c=input()
for i in range(len(word)):
    if word[i]==c:
        idx=i
if idx<0:
    print("None")
else:
    print(idx)