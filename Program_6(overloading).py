class over():
    def hello(self,name,age):
        self.name=name
        self.age=age
        if not(self.age):
            print("Hello",self.name)
        elif (not(self.age) and not(self.name)):
            print("Hello")
        else:
            print("Hello",self.name)
            print("Your age is",self.age)
o=over()
while True:
    print("1:Call the function with both name and age")
    print("2:Call the function with only name")
    print("3:Call the function without both name and age")
    choice=int(input("Enter your choice"))
    if choice==1:
        name=input("Enter your name:")
        if name.isdigit()==True:
            name=input("Enter a valid name:")
        elif name.isalnum()==True:
            name=input("Enter a valid name")
        else :
            print("--------------")
        age=input("Enter your age:")
        if age.isalpha()==True:
            age=input("Enter a valid age:")
        elif age.isalnum()==True:
            age=input("Enter a valid age")
        else :
            print("--------------")
        o.hello(name,age)
    elif choice==2:
        name=input("enter your name")
        o.hello(name,'')
    elif choice==3:
        o.hello('','')
    else:
        break