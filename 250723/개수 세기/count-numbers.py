n,m = map(int,input().split())
m_count=0
arr=list(map(int,input().split()))
for i in arr:
    if i==m:
        m_count+=1
print(m_count)