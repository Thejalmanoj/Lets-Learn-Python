n=int(input("Enter the number of players:"))
d=list(map(int,input().strip().split(" ")))
alice=d[0]
count=0
for i in range(1,n):
    if(d[i]!=alice):
        count+=1 
print(count)
