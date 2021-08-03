while True:
    print("Press 1 to check if A is superset of B ")
    print("Press 2 to check if A subset of B")
    print("Press 3 to perform Union Operation")
    print("Press 4 to perfrom Intersection Operation")
    print("Press 5 to perform A - B")
    print("Press 6 to perform B - A")
    print("Press 7 to check if sets are disjoint")
    print("Press 8 to find length of set")
    print("Press 9 to find max value in set")
    print("Print 10 to find min value in set")
    print("While entering elements, do not use any space or commas")

    choice = int(input("Enter option\n"))

    if choice == 1:
        A = set(input("Enter Elements of set A :\n"))
        B = set(input("Enter Elements of set B :\n"))
        if not (any(A) or any(B)):
            print("Please Enter elements for both sets")
            continue
        print(A.issuperset(B))
    elif choice == 2:
        A = set(input("Enter Elements of set A :\n"))
        B = set(input("Enter Elements of set B :\n"))
        print(A.issubset(B))
    elif choice == 3:
        A = set(input("Enter Elements of set A :\n"))
        B = set(input("Enter Elements of set B :\n"))
        print(A | B)
    elif choice == 4:
        A = set(input("Enter Elements of set A :\n"))
        B = set(input("Enter Elements of set B :\n"))
        print(A & B)
    elif choice == 5:
        A = set(input("Enter Elements of set A :\n"))
        B = set(input("Enter Elements of set B :\n"))
        print(A - B)
    elif choice == 6:
        A = set(input("Enter Elements of set A :\n"))
        B = set(input("Enter Elements of set B :\n"))
        print(B - A)
    elif choice == 7:
        A = set(input("Enter Elements of set A :\n"))
        B = set(input("Enter Elements of set B :\n"))
        print(A.isdisjoint(B))
    elif choice == 8:
        A = set(input("Enter Elements of set A :\n"))

        print(len(A))
    elif choice == 9:
        A = set(input("Enter Elements of set A :\n"))

        print(max(A))
    elif choice == 10:
        A = set(input("Enter Elements of set A :\n"))

        print(min(A))
    elif choice == 0:
        print("Exiting")
        break
