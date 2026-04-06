arr=list(map(int,input().strip().split(" ")))
climb=0
if(len(arr)<3):
    climb=0
#Step-up
while(climb+1<len(arr) and arr[climb]<arr[climb+1]):
    climb+=1 
    
#Step-down
while(climb+1<len(arr) and arr[climb]>arr[climb+1]):
    climb+=1 
    
if(climb==len(arr)-1):
    print("Valid")
else:
    print("Not valid")
    
