day=int(input())
eve=int(input())
night=int(input())
s=(eve*0.20)+(night*0.15)
g=(eve*0.30)+(night*0.20)
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

