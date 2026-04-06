a,b,n=map(int,input().split(" "))
for r in range(1,n+1):
    if(r%2!=0):
        a*=2
    else:
        b*=2
print(a+b)
