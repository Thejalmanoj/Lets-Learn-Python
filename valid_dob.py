def isLeap(year):
    if(year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
        
def validDob(d,m,y):
    validy=True
    validm=True
    validd=True
    if(y<1600 or y>2025):
        validy=False
    if(m<1 or m>12):
        validm=False
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    maxdays=days[m-1]
    if(validy==True and validm==True):
        if(m==2):
            leap=isLeap(y)
            if(leap==True):
                maxdays=29
        if(d>=1 and d<= maxdays):
            validd=True
    if(validd==True and validm==True and validy==True):
        return True
    else:
        return False
            
if __name__=="__main__":
    d=int(input())
    m=int(input())
    y=int(input())
    res=validDob(d,m,y)
    if(res==True):
        print("DOB is valid")
    else:
        print("DOB is not valid")
            
