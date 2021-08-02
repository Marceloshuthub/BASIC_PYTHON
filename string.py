while True:
    print("1.THE LENGTH OF THE STRING")
    print("2.CONCATENATION OF THE STRING")
    print("3.MAXIMUM VALUE OF THE STRING")
    print("4.MINIMUM VALUE OF THE STRING")
    print("5.STRING TO LOWERCASE")
    print("6.STRING TO UPPERCASE")
    print("7.CHECK IF ALPHABET OR NOT")
    print("8.RANGE OF STRINGS")
    print("9.SORTED STRINGS")
    print("0.EXIT")
    choice=int(input("ENTER YOUR CHOICE"))
    if choice == 1:
        n = input("ENTER THE STRING")
        print("length of the string is",len(n))
    elif choice == 2:
        n = input("ENTER THE STRING")
        s = input("ENTER THE STRING")
        print("concatenated string is",(n+s))
    elif choice == 3:
        n = input("ENTER THE STRING")
        print("max value of string is",max(n))
    elif choice == 4:
        n = input("ENTER THE STRING")
        print("min value of string is",min(n))
    elif choice == 5:
        n = input("ENTER THE STRING")
        print(n.lower())
    elif choice==6:
        n = input("ENTER THE STRING")
        print(n.upper())
    elif choice == 7:
        n = input("ENTER THE STRING")
        print(n.isalpha())
    elif choice == 8:
        n = input("ENTER THE STRING")
        print(n[2:5])
    elif choice == 9:
        n = input("ENTER THE STRING")
        print(sorted(n))
    elif choice == 0:
        print("EXITING")
        break
    
    


