n,a,b,c=map(int,input().split())
count=0
while(n>0):
    n-=1
    count+=1
    a+=1 
    if(a%30==0):
        n+=30
    if(n==0):
        break
    n-=1
    count+=1
    b+=1
    if(b%100==0):
        n+=60
    if(n==0):
        break
    n-=1
    count+=1
    c+=1
    if(c%15==0):
        n+=10
print(count)
        
    
        
    