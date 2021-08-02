while True:
    print("Press 1 to check max value in ")
    print("Press 2 to check min value")
    print("Press 3 to find length")
    print("Press 4 to add lists ")
    print("Press 5 to sort list")
    print("Press 6 to slice list from position 0 to 4")
    print("Press 7 to find index of 'x' in list ")
    print("Press 8 to check if 'a' is in list")
    print("Press 9 to reverse list")
    print("Press 10 to find number of p's in list ")
    print("Press 0 to exit")
    print("While entering elements, do not use any space or commas")

    choice = int(input("Enter option\n"))
    if choice == 1:
        l = list(input("Enter list elements\n"))
        print(max(l))
    elif choice == 2:
        l = list(input("Enter list elements\n"))
        print(min(l))
    elif choice == 3:
        l = list(input("Enter list elements\n"))
        print(l)
    elif choice == 4:
        l1 = list(input("Enter list t1 elements\n"))
        l2 = list(input("Enter t2 elements\n"))
        print(l1 + l2)
    elif choice == 5:
        l = list(input("Enter list elements\n"))
        print(sorted(l))
    elif choice == 6:
        l = list(input("Enter list elements\n"))
        print(l)
    elif choice == 7:
        l = list(input("Enter list elements\n"))
        print(l.index('x'))
    elif choice == 8:
        l = list(input("Enter list elements\n"))
        print("a" in l)
    elif choice == 9:
        l = list(input("Enter list elements\n"))
        print(l[::-1])
    elif choice == 10:
        l = list(input("Enter list elements\n"))
        print(l.count('p'))
