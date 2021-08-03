import io
while True:
    print("\n1.Write to a file open in read mode")
    print("2.Performing I/O Operations on closed file")
    print("3.Giving invalid mode for opening a file")
    print("4.Opening a non-existent file ")
    print("5.Giving a wrong type of arguments")
    print("6.Using Undefined identifier")
    print("7.Stop Iteration Error\n")

    ch = int(input("Enter Your Choice: "))


    file_name = 'file.txt'

    if ch == 1:
        try:
            with open(file_name, 'r') as f:
                f.write("Hello")
        except io.UnsupportedOperation:
            print("io.UnsupportedOperation Error")
        else:
            print("Pass")
        exit()
    elif ch == 2:
        f = open(file_name,'r')
        content = f.readlines()
        f.close()
        try:
            c = f.readlines()
        except ValueError:
            print("ValueError:I/O operation on closed file")
        else:
            print("Pass")
        exit()
    elif ch == 3:

        try:
            with open(file_name, 'z') as f:
                content = f.readlines()
        except ValueError:
            print("ValueError:invalid mode")
        else:
            print("Pass")
        exit()

    elif ch == 4:
        try:
            with open('sflie.txt', 'r') as f:
                content = f.readlines()
        except FileNotFoundError:
            print("FileNotFoundError")
        else:
            print("Pass")
        exit()

    elif ch == 5:
        try:
            with open(file_name, 'r', 'w') as f:
                content = f.readlines()
        except TypeError:
            print("TypeError")
        else:
            print("Pass")
        exit()

    elif ch == 6:
        try:
            with open(file_name, 'r') as f:
                content = k.readlines()
        except NameError:
            print("NameError")
        else:
            print("Pass")
        exit()
    elif ch == 7:
        def myfunc(i):
            while i < 3:
                yield i
                i += 1

        j = myfunc(2)
        try:
            print(next(j))
            print(next(j))
        except StopIteration:
            print("StopIteration Error")
        exit()
    elif ch == 0:
        exit()

    else:
        print("Enter within the given choices")

