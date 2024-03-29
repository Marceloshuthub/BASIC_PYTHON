import os

while True:
    print("1.Check Value Error")
    print("2.Check File Not Found Error")
    print("3.Check Type Error")
    print("4.Check IOError")
    print("5.Check File Exist Error")
    print("6.Attribute error")
    print("0.Exit")
    n=int(input("Enter Choice:"))
    if n==1:
        try:
            f = open('abc.txt')
            f.write("Sample")  #modes dependent
            print("VALID OPERATION")
        except ValueError:
            print("Value Error!")
    elif n==2:
        try:
            f = open('cc.txt', 'r') # whenever abc.txt will not there then it will FileNotFoundError
            print("FILE EXISTS")
        except FileNotFoundError:
            print("File Not Found error!")
    elif n==3:
        try:
            f = open('abc.txt', 'r', 'w') # when one parameter w is removed then it will print SUCESS
            print("SUCESS")
        except TypeError:
            print("Type Error")
    elif n==4:
        try:
            f = open('abc.txt', 'w+')
            f.write("Sample")
            f1 = open('cc.txt', 'r') # when i will replace cc.txt to abc.txt then it will print Successfully
            print("Successfully")
        except IOError:
            print("IO Error")
    elif n==5:
        try:
            f=os.path.exists('abc4.txt') # if file abc4.txt is exists then it will raise FileExistsError
            if f > 0:
                raise FileExistsError
            print("THE FILE EXISTS IN THE PATH")
        except FileExistsError:
            print("File Exist Error")
    elif n==6:
        try:
            f=open('abc2.txt','a')
            #f.open('abc2.txt', 'r') #When i will comment this line it will be show AttributeError
            print("NO ATTRIBUTE MISMATCH")
        except AttributeError:
            print("AttributeError!")
    elif n==0:
        break
    else:
        print("Invalid input Please try again ")
