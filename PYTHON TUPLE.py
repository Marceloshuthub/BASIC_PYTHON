while True:
    choice = int(input('''
    Press 1 to find max element in the tuple
    Press 2 to find the min element in the tuple
    Press 3 to repeat the tuple twice
    Press 4 to sort the tuple
    Press 5 to reverse the tuple
    Press 6 to slice the tuple from 0 to 5th element
    Press 7 to check if 'a' is in tuple
    Press 8 to find index of 'a'in tuple
    Press 9 to find length of tuple
    Press 10 to count the number of a's in the tuple
    Press 0 to exit
    '''))
    if choice == 0:
        break
    if choice == 1:
        t = tuple(input("Enter tuple elements"))
        print(max(t))
    if choice == 2:
        t = tuple(input("Enter tuple elements"))
        print(min(t))
    if choice == 3:
        t = tuple(input("Enter tuple elements"))
        print(t*2)
    if choice == 4:
        t = tuple(input("Enter tuple elements"))
        print(sorted(t))
    if choice == 5:
        t = tuple(input("Enter tuple elements"))
        print(t[::-1])
    if choice == 6:
        t = tuple(input("Enter tuple elements"))
        print(t[0:5])
    if choice == 7:
        t = tuple(input("Enter tuple elements"))
        print('a' in t)
    if choice == 8:
        t = tuple(input("Enter tuple elements"))
        print(t.index('a'))
    if choice == 9:
        t = tuple(input("Enter tuple elements"))
        print(len(t))
    if choice == 10:
        t = tuple(input("Enter tuple elements"))
        print(t.count('a'))
