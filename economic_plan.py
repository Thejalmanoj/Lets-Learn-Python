#Customer wants to compare which plan is more effective based on their usage.
#Silver plan: 6am - 6 pm => 1st 20 minutes are free then 0.30 Rs per min.
            # 6 pm - 10 pm => 0.20 per minute
            # 10 pm - 6 am => 0.15 per minute
#Gold plan: 6am - 6 pm => 1st 200 minutes are free then 0.40 Rs per min.
            # 6 pm - 10 pm => 0.30 per minute
            # 10 pm - 6 am => 0.20 per minute

day=int(input()) #daytime usage in minutes
eve=int(input()) #evening usage in minutes
night=int(input()) #nighttime usage in minutes
s=(eve*0.20)+(night*0.15) #Amount as per silver plan
g=(eve*0.30)+(night*0.20) #Amount as per Golden plan
if(day>120):
    s+=(day-120)*0.30
if(day>200):
    g+=(day-200)*0.40
print(f"Total cost for silver:{s:.2f}")
print(f"Total cost for gold:{g:.2f}")
if(s>g):
    print("Gold is effective")
elif(g>s):
    print("Silver is effective")
else:
    print("Both are same")

