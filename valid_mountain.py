#Question: Given an array of integers arr, return true if and only if it is a valid mountain array.
#Logic: array length should be greater than or equal to 3. There exists some i with 0 < i < arr.length - 1 such that:
                        # arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
                        # arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

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
    
