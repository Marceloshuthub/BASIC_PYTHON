import os
from Program_4_a import*
os.system("clear")
o1=op()
o2=op()
o1.get()
o2.get()
while True:
    print("1:Perform addition")
    print("2:Perform subtracttion")
    print("3:Perform multiplication")
    print("4:Perform division")
    ch=int(input("Enter your choice:"))
    if ch==1:
        o1+o2
    elif ch==2:
        o1-o2
    elif ch==3:
        o1*o2
    elif ch==4:
        o1//o2
    else:
        print("invalid choice")
