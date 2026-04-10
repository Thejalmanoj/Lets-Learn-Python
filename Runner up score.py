#Question: Given the participants’ score sheet for your University Sports Day, you are required to find the runner-up score.
#Input Format : The first line contains n (Number of participants).The second line contains an array A[] of n integers each separated by a space.
#Output format : Print the runner-up score.
# ( Logic: Store the scores in ascending order. Runner up score is the 2nd largest element) 

if __name__ == '__main__':
    n=int(input())
    arr=set(map(int, input().split()))
    arr=sorted(arr)
    print(arr[-2])
